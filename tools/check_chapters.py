#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""章节一致性自检（写稿/统稿后运行）。

检查五件事：
1. 【硬错误】正文"第 N 章"互引是否越界（N 必须落在 1–24）
2. 【硬错误】语言红线词（排比字段化、作者腔、空转句、过程性文字、研究装置）
3. 【硬错误】引用的章号对应的章文件是否存在
4. 【警告】章节文件是否齐（24 章 + 序）
5. 【警告】有稿章是否已改为办法体（有"## 办法 N"）、办法数是否在 5–12、字数是否够 3,000 汉字

用法：python3 tools/check_chapters.py
退出码：0 = 通过（可带警告）；1 = 有硬错误
"""
import re, os, sys, glob

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK = os.path.join(BASE, "book")

RED_LINES = [
    "其一", "其二", "其三", "本章将", "上一章我们", "上一章讲过", "我们看",
    "随着 AI 的发展", "在这个时代", "值得注意的是", "这是本章最重要的",
    "本章字数", "字数：", "不确定清单", "本章三问", "行业落点表",
    "下一轮补采", "补采建议", "写作说明", "待核清单",
]
# 附录只查这几条（附录本来就是台账与版本说明，允许"未采用口径""来源分档"这类写法）
RED_LINES_APPENDIX = ["本章三问", "本章字数", "下一轮补采", "待核清单"]

APPENDIX_PREFIX = ("90-", "91-", "92-", "93-")

CHAPTER_RE = re.compile(r"^(\d{2})-第(\d{1,2})章-(.+)\.md$")

# ★已定稿：用户确认过的成稿。不受篇幅下限约束，也不参与改写待办统计。
FINAL_DRAFT = {"02-第2章-让AI在回答里提到你.md"}


def chapters():
    out = {}
    for p in glob.glob(os.path.join(BOOK, "*.md")):
        m = CHAPTER_RE.match(os.path.basename(p))
        if m:
            out[int(m.group(2))] = p
    return out


def hanzi(t):
    return len(re.findall(r"[\u4e00-\u9fff]", t))


def main():
    errors, warnings = [], []
    ch = chapters()

    # 4. 章文件齐全性
    missing = [n for n in range(1, 25) if n not in ch]
    if missing:
        warnings.append(f"尚未落盘的章：{missing}")

    # 1/3. 互引越界 + 目标章存在性
    for p in sorted(glob.glob(os.path.join(BOOK, "*.md"))):
        t = open(p, encoding="utf-8").read()
        fn = os.path.basename(p)
        for m in re.finditer(r"第\s*(\d{1,2})((?:\s*[、,，]\s*\d{1,2})*)\s*章", t):
            for n in [m.group(1)] + re.findall(r"\d{1,2}", m.group(2) or ""):
                n = int(n)
                if not 1 <= n <= 24:
                    errors.append(f"[越界引用] {fn}: 第 {n} 章")
                elif n not in ch:
                    warnings.append(f"[指向未落盘章] {fn}: 第 {n} 章")

        # 2. 语言红线（附录只查少数几条）
        words = RED_LINES_APPENDIX if fn.startswith(APPENDIX_PREFIX) else RED_LINES
        hit = [w for w in words if w in t]
        if hit:
            errors.append(f"[语言红线] {fn}: {hit}")

    # 5. 办法体规格（只查已有"## 办法"的章）
    for n, p in sorted(ch.items()):
        t = open(p, encoding="utf-8").read()
        fn = os.path.basename(p)
        cnt = len(re.findall(r"^## 办法 \d+", t, flags=re.M))
        if cnt == 0:
            warnings.append(f"[未改办法体] 第 {n} 章 {fn}")
            continue
        if not 5 <= cnt <= 12:
            errors.append(f"[办法数越界] 第 {n} 章 {fn}: {cnt} 个")
        if "## 本章注意" not in t:
            errors.append(f"[缺章末节] 第 {n} 章 {fn}: 缺 本章注意")
        if not re.search(r"^## 本章数据来源|^## 本章来源", t, flags=re.M):
            errors.append(f"[缺章末节] 第 {n} 章 {fn}: 缺 本章数据来源")
        h = hanzi(t)
        if h < 3000 and fn not in FINAL_DRAFT:
            warnings.append(f"[篇幅偏短] 第 {n} 章 {fn}: {h} 汉字（目标 ≥3000）")

    print("=" * 62)
    print(f"章节一致性自检 ｜ 已有章文件 {len(ch)}/24")
    print("=" * 62)
    for e in errors:
        print(f"❌ {e}")
    for w in warnings:
        print(f"⚠️  {w}")
    if not errors and not warnings:
        print("✅ 全部通过")
    print()
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
