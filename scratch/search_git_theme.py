import subprocess

out = subprocess.check_output(['git', 'log', '-p', '--all'], text=True, encoding='utf-8')
lines = out.splitlines()
for i, l in enumerate(lines):
    if 'theme-toggle' in l or 'ri-moon' in l or 'ri-sun' in l or 'contrast' in l:
        print(f"{i}: {l}")
        for j in range(max(0, i-2), min(len(lines), i+3)):
            print(f"   {lines[j]}")
        print("-" * 40)
