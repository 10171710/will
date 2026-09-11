import os, glob

root = r"c:\Users\HP\Downloads\willbridge-estate-template"
for dirpath, dirnames, filenames in os.walk(root):
    for f in filenames:
        fp = os.path.join(dirpath, f)
        if fp.endswith(('.html', '.js', '.css')):
            with open(fp, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
                if "1 2 3 4" in content or "1) Medical" in content:
                    print(f"Found remaining test text in: {fp}")
print("Check completed.")
