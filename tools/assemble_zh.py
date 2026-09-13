#!/usr/bin/env python3
"""合稿：把 drafts/ 里比 book/ 更新的章节合入，并统一收尾小节与待核标注。

用法：python3 tools/assemble_zh.py [--dry-run]
幂等：可重复运行；不含 [[待核 的文件跳过结构化。
"""
import os, re, glob, shutil, sys, time

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK, DRAFTS = f"{BASE}/book", f"{BASE}/drafts"
CH_NUM = {f"{i:02d}": i for i in range(1, 18)}


def cjk(t):
    return len(re.findall(r"[\u4e00-\u9fff]", t))


def looks_complete(text):
    """完整性闸门：小节齐全、无明显截断。"""
    if not all(k in text for k in ("本章三问", "本章来源", "本章我不确定")):
        return False
    if re.search(r"\[\[待核[^\]]*$", text.strip()):      # 未闭合的待核标记 → 截断
        return False
    if text.strip()[-1] not in "。！？）】》”\n\"'":
        return False
    return True


def book_target(num):
    hits = glob.glob(f"{BOOK}/{num}-第*章-*.md")
    return hits[0] if hits else None


def main():
    dry = "--dry-run" in sys.argv
    print("== 1) 合稿（drafts 较新且完整者胜）==")
    for d in sorted(glob.glob(f"{DRAFTS}/*.md")):
        name = os.path.basename(d)
        num = name[:2]
        if num not in CH_NUM:
            continue
        tgt = book_target(num)
        if not tgt:
            print(f"  ⚠ {name}: book/ 无对应章节文件，跳过")
            continue
        dt, bt = open(d, encoding="utf-8").read(), open(tgt, encoding="utf-8").read()
        d_newer = os.path.getmtime(d) > os.path.getmtime(tgt)
        if not d_newer:
            print(f"  = {name}: book 版本较新，保留（{cjk(bt)}字）")
            continue
        if not looks_complete(dt):
            print(f"  ⛔ {name}: drafts 较新但完整性检查不通过（疑截断），保留 book 版本（{cjk(bt)}字）")
            continue
        if cjk(dt) < 0.85 * cjk(bt):
            print(f"  ⛔ {name}: drafts 较新但字数缩水 {cjk(bt)}→{cjk(dt)}（>15%），保留 book 版本")
            continue
        if not dry:
            shutil.copy2(d, tgt)
        print(f"  ↑ {name}: drafts 较新且完整（{cjk(dt)}字）→ 覆盖 book 版本")

    print("\n== 2) 收尾小节统一 ==")
    for f in sorted(glob.glob(f"{BOOK}/*.md")):
        t = open(f, encoding="utf-8").read(); o = t
        t = re.sub(r"^## [一二三四五六七八九十]+、本章三问", "## 本章三问", t, flags=re.M)
        t = re.sub(r"^## [一二三四五六七八九十]+、本章来源", "## 本章来源", t, flags=re.M)
        t = re.sub(r"^## [一二三四五六七八九十]+、本章我不确定的地方", "## 本章我不确定的地方", t, flags=re.M)
        t = t.replace("## 待核清单", "## 本章我不确定的地方")
        if t != o and not dry:
            open(f, "w", encoding="utf-8").write(t)
            print("  ✓", os.path.basename(f))

    print("\n== 3) 待核标注结构化 ==")
    for f in sorted(glob.glob(f"{BOOK}/*.md")):
        t = open(f, encoding="utf-8").read()
        if "[[待核" not in t:
            continue
        notes = []

        def repl(m):
            note = m.group(1).replace("待核", "").strip(" ：:说明")
            notes.append(note or "（原稿标注为待核，未附说明）")
            return f"〔待核 {len(notes)}〕"

        t2 = re.sub(r"\[\[(待核[^\]]*?)\]\]", repl, t)
        block = "\n".join(f"{i}. {n}" for i, n in enumerate(notes, 1))
        hdr = "\n\n**本章待核条目**（未核到原始出处的项目，读者请勿单独引用）：\n"
        if "## 本章我不确定的地方" in t2:
            t2 = t2.replace("## 本章我不确定的地方", "## 本章我不确定的地方" + hdr + block + "\n", 1)
        else:
            t2 = t2.rstrip() + "\n\n## 本章我不确定的地方\n" + hdr + block + "\n"
        if not dry:
            open(f, "w", encoding="utf-8").write(t2)
        print(f"  ✓ {os.path.basename(f)}: {len(notes)} 处")

    print("\n== 4) 全书体检 ==")
    tot = 0
    for f in sorted(glob.glob(f"{BOOK}/*.md")):
        n = os.path.basename(f)
        if not n[0].isdigit() or n.startswith(("19-", "20-", "21-", "22-")):
            continue
        t = open(f, encoding="utf-8").read()
        c = cjk(t); tot += c
        ok = ("本章三问" in t) and ("我不确定" in t)
        red = sum(t.count(w) for w in ["补记", "Added in", "New in", "新增于此"])
        print(f"  {n[:26]:<28}{c:>7}字  结构{'✓' if ok else '✗'} 红线{red} 链接{len(re.findall(r'https?://', t)):>3}")
    print(f"\n正文合计：{tot} 汉字（{tot/10000:.1f} 万字）")
    if dry:
        print("[dry-run] 未写入任何文件")


if __name__ == "__main__":
    main()
