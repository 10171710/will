import glob
import re

files = glob.glob('*.html') + glob.glob('docs/**/*.html', recursive=True)
print("Checking files for name and password inputs...")
for f in sorted(files):
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    name_matches = re.findall(r'<input[^>]*name=[\"\'](?:name|first|last)[\"\'][^>]*>', content, re.IGNORECASE)
    pwd_matches = re.findall(r'<input[^>]*type=[\"\']password[\"\'][^>]*>', content, re.IGNORECASE)
    if name_matches or pwd_matches:
        print(f"File: {f}")
        for m in name_matches:
            print(f"  NAME: {m}")
        for m in pwd_matches:
            print(f"  PWD:  {m}")
