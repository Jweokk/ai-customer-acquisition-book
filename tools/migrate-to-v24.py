#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""一次性迁移：把 book/ 从最初的 17 章编号迁到 v8 的 24 章编号。
做四件事：① 文件改名 ② 正文"第 N 章"互引重映射 ③ 文件路径引用同步 ④ H1 章号/章名同步。
可回滚：git checkout -- book/ && git checkout -- mkdocs.yml
用法：python3 tools/migrate-to-v24.py          # 干跑，只打印
      python3 tools/migrate-to-v24.py --apply  # 真跑
"""
import os, re, sys, shutil

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK = os.path.join(BASE, "book")
APPLY = "--apply" in sys.argv

# 旧章号 -> 新章号（单趟替换，禁止顺序替换）
NUM = {1: 1, 2: 1, 3: 3, 4: 2, 5: 8, 6: 14, 7: 6, 8: 4, 9: 5,
       10: 13, 11: 18, 12: 17, 13: 7, 14: 20, 15: 21, 16: 23, 17: 24}

# 文件改名表
RENAME = {
 "00-序-入口迁移.md": "00-序-客户找供应商的方式变了.md",
 "01-第1章-买家换了入口.md": "01-第1章-先看清战场.md",
 "02-第2章-决策在暗漏斗里完成.md": "01b-待并入第1章-暗漏斗.md",
 "03-第3章-候选集机制.md": "03-第3章-挤进客户的第一份名单.md",
 "04-第4章-让AI在回答里提到你.md": "02-第2章-让AI在回答里提到你.md",
 "05-第5章-两套规则.md": "08-第8章-中文市场要多做三件事.md",
 "06-第6章-一手数据与验证经济.md": "14-第14章-做出别人抄不走的内容.md",
 "07-第7章-机器可读.md": "06-第6章-让机器读懂你.md",
 "08-第8章-第三方信源与人类痕迹.md": "04-第4章-让第三方替你说话.md",
 "09-第9章-风险话题即入口.md": "05-第5章-先讲自己的坑.md",
 "10-第10章-触达军备竞赛.md": "13-第13章-外联-从发得多到发得准.md",
 "11-第11章-外联外呼与合规.md": "18-第18章-电话和私域.md",
 "12-第12章-五档标签与账户智能.md": "17-第17章-用AI找客户管线索跑销售.md",
 "13-第13章-当客户是机器.md": "07-第7章-让买家的AI代理选中你.md",
 "14-第14章-怎么知道有用.md": "20-第20章-怎么知道有没有用.md",
 "15-第15章-入口依赖与对冲.md": "21-第21章-别把命押在一个入口.md",
 "16-第16章-谁来做.md": "23-第23章-谁来干花多少钱.md",
 "17-第17章-边界与失败档案.md": "24-第24章-别踩这些线-六份失败档案.md",
 "19-附录A-案例索引与资料出处.md": "90-附录A-案例索引与资料出处.md",
 "20-附录B-手段平台索引与指标字典.md": "91-附录B-手段平台索引与指标字典.md",
 "21-附录C-版本历史与更新说明.md": "92-附录C-版本历史与更新说明.md",
 "22-附录D-行业差异矩阵.md": "93-附录D-行业差异矩阵.md",
}

# 新章号 -> (文件名, 章名)
TITLE = {
 1: ("01-第1章-先看清战场.md", "先看清战场：客户现在怎么挑供应商"),
 2: ("02-第2章-让AI在回答里提到你.md", None),   # ★已定稿：只改章号，不动章名
 3: ("03-第3章-挤进客户的第一份名单.md", "挤进客户的第一份名单"),
 4: ("04-第4章-让第三方替你说话.md", "让第三方替你说话"),
 5: ("05-第5章-先讲自己的坑.md", "先讲自己的坑"),
 6: ("06-第6章-让机器读懂你.md", "让机器读懂你"),
 7: ("07-第7章-让买家的AI代理选中你.md", "让买家的 AI 代理选中你"),
 8: ("08-第8章-中文市场要多做三件事.md", "中文市场要多做三件事"),
 13: ("13-第13章-外联-从发得多到发得准.md", "外联：从“发得多”到“发得准”"),
 14: ("14-第14章-做出别人抄不走的内容.md", "做出别人抄不走的内容：一手数据与真实案例"),
 17: ("17-第17章-用AI找客户管线索跑销售.md", "用 AI 找客户、管线索、跑销售"),
 18: ("18-第18章-电话和私域.md", "电话和私域：哪些还能用，哪些碰了就出事"),
 20: ("20-第20章-怎么知道有没有用.md", "怎么知道有没有用：三套账本和一次停投实验"),
 21: ("21-第21章-别把命押在一个入口.md", "别把命押在一个入口：依赖体检与对冲"),
 23: ("23-第23章-谁来干花多少钱.md", "谁来干、花多少钱：三档最小配置"),
 24: ("24-第24章-别踩这些线-六份失败档案.md", "别踩这些线：六份失败档案"),
}

def old_num(fn):
    m = re.search(r"第(\d+)章", fn)
    if m: return int(m.group(1))
    m = re.match(r"(\d+)-", fn)          # 无"第N章"的：00-序 / 19..22-附录
    return int(m.group(1)) if m else None

def remap_refs(text, self_old=None):
    def sub(m):
        head, tail = m.group(1), m.group(2) or ""
        nums = [head] + re.findall(r"\d{1,2}", tail)
        out = []
        for n in nums:
            i = int(n)
            if self_old is not None and i == self_old and len(nums) == 1:
                out.append("本章")
            else:
                out.append(str(NUM.get(i, i)))
        if "本章" in out:
            return "本章"
        return "第 " + "、".join(out) + " 章"
    return re.sub(r"第\s*(\d{1,2})((?:\s*[、,，]\s*\d{1,2})*)\s*章", sub, text)

report = []

# 已经按新编号写的文件，不许再重映射（它们引用的就是新章号）
NO_REMAP = {"09-第9章-投广告.md"}

# 例外的 H1（不走映射表）
H1_OVERRIDE = {
 "00-序-客户找供应商的方式变了.md": "# 序 · 客户找供应商的方式变了",
 "01b-待并入第1章-暗漏斗.md": "# 待并入第 1 章 · 决策在暗漏斗里完成",
}

# ---------- ① 改名（两阶段，避免互撞） ----------
if APPLY:
    tmp = {}
    for old, new in RENAME.items():
        p = os.path.join(BOOK, old)
        if not os.path.exists(p): report.append(f"跳过(缺文件): {old}"); continue
        t = os.path.join(BOOK, ".tmp__" + new)
        shutil.move(p, t); tmp[t] = os.path.join(BOOK, new)
    for t, final in tmp.items():
        shutil.move(t, final)
    report.append(f"改名完成: {len(tmp)} 个文件")

# ---------- ② 正文互引重映射 + ③ 路径引用同步 ----------
def content_files():
    out = [os.path.join(BOOK, f) for f in sorted(os.listdir(BOOK)) if f.endswith(".md")]
    out += [os.path.join(BASE, "llms.txt")]
    return [p for p in out if os.path.exists(p)]

ref_hits = 0
for p in content_files():
    t = orig = open(p, encoding="utf-8").read()
    fn = os.path.basename(p)
    if fn in NO_REMAP:
        report.append(f"  跳过重映射（已为新编号）: {fn}")
        continue
    self_old = old_num(fn) if p.startswith(BOOK) else None
    t = remap_refs(t, self_old)
    n = len(re.findall(r"第\s*\d{1,2}\s*章", orig))
    ref_hits += n
    for old, new in RENAME.items():                 # 路径引用（含 slug）
        t = t.replace(old, new).replace(old[:-3], new[:-3])
    if APPLY and t != orig:
        open(p, "w", encoding="utf-8").write(t)
    if n: report.append(f"  互引 {n:>3} 处 <- {fn}")

# ---------- ④ H1 同步 ----------
for fn, h1 in H1_OVERRIDE.items():
    p = os.path.join(BOOK, fn)
    if not os.path.exists(p): continue
    lines = open(p, encoding="utf-8").read().split("\n")
    report.append(f"  H1 {fn}: {lines[0][:30]}  ->  {h1[:44]}")
    if APPLY:
        lines[0] = h1
        open(p, "w", encoding="utf-8").write("\n".join(lines))

for num, (fn, title) in TITLE.items():
    p = os.path.join(BOOK, fn)
    if not os.path.exists(p): continue
    t = open(p, encoding="utf-8").read()
    lines = t.split("\n")
    old_h1 = lines[0]
    if title is None:                                # ★已定稿：只改章号
        new_h1 = re.sub(r"^#\s*第\s*\d+\s*章", f"# 第 {num} 章", old_h1)
    else:
        new_h1 = f"# 第 {num} 章 {title}"
    if APPLY and new_h1 != old_h1:
        lines[0] = new_h1
        open(p, "w", encoding="utf-8").write("\n".join(lines))
    report.append(f"  H1 {fn}: {old_h1[:34]}  ->  {new_h1[:44]}")

print("\n".join(report))
print(f"\n共处理互引 {ref_hits} 处 | APPLY={APPLY}")
