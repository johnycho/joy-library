#!/usr/bin/env python3
# 로컬에서 폴더 구성을 manifest/registry 에 반영할 때 사용.
#   python3 tools/build.py
# (GitHub에 올리면 .github/workflows/build.yml 이 같은 일을 자동으로 합니다.)
import os, json

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sysroot = os.path.join(root, "systems")
registry = []

for name in sorted(os.listdir(sysroot)):
    d = os.path.join(sysroot, name)
    if not os.path.isdir(d):
        continue
    if os.path.isfile(os.path.join(d, "index.html")):
        registry.append(name)
    sounds = os.path.join(d, "sounds")
    if os.path.isdir(sounds):
        out = {}
        for cat in sorted(os.listdir(sounds)):
            cd = os.path.join(sounds, cat)
            if not os.path.isdir(cd):
                continue
            files = sorted(f for f in os.listdir(cd) if f.lower().endswith(".mp3"))
            if files:
                out[cat] = files
        with open(os.path.join(sounds, "manifest.json"), "w", encoding="utf-8") as fp:
            json.dump(out, fp, ensure_ascii=False, indent=2)

with open(os.path.join(sysroot, "registry.json"), "w", encoding="utf-8") as fp:
    json.dump(registry, fp, ensure_ascii=False, indent=2)
print("updated:", registry)
