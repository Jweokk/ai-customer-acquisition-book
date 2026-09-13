#!/usr/bin/env python3
"""后台补跑 deepseek 通道（今日限流严重，串行+长退避）。"""
import os, json, ssl, time, urllib.request, urllib.error, sys

D = "/home/ubuntu/airtap_ai_answers/aihuoke-2026-09-12/实测/实测1-候选集多模型"
Q = json.load(open(f"{D}/../问题集.json", encoding="utf-8"))
E = {}
for p in ("~/.hermes/tokens.env", "~/.hermes/.env"):
    for ln in open(os.path.expanduser(p), encoding="utf-8"):
        ln = ln.strip()
        if "=" in ln and not ln.startswith("#"):
            k, v = ln.split("=", 1)
            E[k.strip().replace("export ", "")] = v.strip().strip('"\'')
ctx = ssl.create_default_context(); ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE

outp = f"{D}/raw_deepseek.json"
done = json.load(open(outp, encoding="utf-8")) if os.path.exists(outp) else []
have = {(d["rep"], d["qid"]) for d in done if d.get("ok")}

for rep in (1, 2):
    for qid, prompt in Q.items():
        if (rep, qid) in have:
            continue
        for attempt in range(5):
            try:
                body = json.dumps({"model": "deepseek-flash", "messages": [{"role": "user", "content": prompt}],
                                   "max_tokens": 8000}).encode()
                req = urllib.request.Request("https://api.deepseek.com/v1/chat/completions", data=body,
                    headers={"Content-Type": "application/json",
                             "Authorization": f"Bearer {E['DEEPSEEK_API_KEY']}"}, method="POST")
                with urllib.request.urlopen(req, timeout=300, context=ctx) as r:
                    d = json.loads(r.read().decode())
                    msg = d["choices"][0]["message"]
                    txt = msg.get("content") or ""
                    fr = d["choices"][0].get("finish_reason")
                    rt = (d.get("usage") or {}).get("completion_tokens_details", {}).get("reasoning_tokens")
                if txt.strip():
                    done.append({"ok": True, "text": txt, "rep": rep, "qid": qid, "model": "deepseek"})
                    json.dump(done, open(outp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
                    print(f"OK {qid} rep{rep} {len(txt)}c reasoning={rt}", flush=True)
                    break
                print(f"EMPTY {qid} rep{rep} finish={fr} reasoning={rt} retry", flush=True)
                time.sleep(8 * (attempt + 1))
            except urllib.error.HTTPError as e:
                wait = 20 * (attempt + 1)
                print(f"HTTP {e.code} {qid} rep{rep} sleep {wait}", flush=True)
                time.sleep(wait)
            except Exception as e:
                wait = 15 * (attempt + 1)
                print(f"{type(e).__name__} {qid} rep{rep} sleep {wait}", flush=True)
                time.sleep(wait)
        time.sleep(5)

print("DONE", len([d for d in done if d.get('ok')]), flush=True)
