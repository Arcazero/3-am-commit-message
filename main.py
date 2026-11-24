import os

msg = "fix: rolled back my 3am deploy — tests passed in my head, prod disagreed, and my confidence interval did not include the outage"
folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(folder, exist_ok=True)
target = os.path.join(folder, "entry.txt")
open(target, "w", encoding="utf-8").write(msg + "\n")
