import os, time

workspace = r"c:\Users\HP\Downloads\willbridge-estate-template"
files = []
for root, dirs, filenames in os.walk(workspace):
    if "scratch" in root or ".git" in root:
        continue
    for f in filenames:
        p = os.path.join(root, f)
        mtime = os.path.getmtime(p)
        files.append((p, mtime, time.ctime(mtime)))

files.sort(key=lambda x: x[1], reverse=True)
print("Recently modified workspace files:")
for p, mtime, ctime in files[:15]:
    print(f"{ctime}: {p}")
