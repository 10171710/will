import subprocess
import re

out = subprocess.check_output(['git', 'log', '-p', '--stat'], text=True, encoding='utf-8')
commits = out.split('commit ')
print(f"Total commits: {len(commits)}")

theme_icons = set()
for c in commits:
    matches = re.findall(r'<button id="theme-toggle".*?</button>', c, re.DOTALL)
    for m in matches:
        theme_icons.add(re.sub(r'\s+', ' ', m.strip()))

for t in theme_icons:
    print("Found theme icon in commit history:")
    print(" ", t)
