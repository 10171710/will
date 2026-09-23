import glob
import re

print("=== VERIFYING NAME FIELDS ===")
files = glob.glob('*.html')
name_issues = []
for f in sorted(files):
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    # Find all inputs with name/first/last
    inputs = re.findall(r'<input[^>]*name=[\"\'](?:name|first|last)[\"\'][^>]*>', content)
    for inp in inputs:
        has_minlength = 'minlength="2"' in inp or "minlength='2'" in inp
        has_pattern = 'pattern=' in inp
        if not (has_minlength and has_pattern):
            name_issues.append((f, inp))
        else:
            print(f"  [OK] {f} -> {inp}")

print("\n=== VERIFYING PASSWORD RECOMMENDATIONS & STRENGTH METER ===")
with open('register.html', 'r', encoding='utf-8') as fp:
    reg_content = fp.read()

assert 'password-strength-container' in reg_content, "Missing password strength container in register.html"
assert 'pwd-rule-length' in reg_content, "Missing pwd-rule-length in register.html"
assert 'pwd-rule-cases' in reg_content, "Missing pwd-rule-cases in register.html"
assert 'pwd-rule-num-sym' in reg_content, "Missing pwd-rule-num-sym in register.html"
assert 'pwd-seg-1' in reg_content, "Missing pwd-seg-1 in register.html"
assert 'data-password-strength' in reg_content or '#reg-password' in reg_content, "Missing password strength trigger"
print("  [OK] register.html contains all strength meter & recommendation checklist elements.")

print("\n=== VERIFYING MAIN.JS ===")
with open('assets/js/main.js', 'r', encoding='utf-8') as fp:
    js_content = fp.read()

assert 'isNameField' in js_content, "Missing isNameField in main.js"
assert 'nameVal.length < 2' in js_content, "Missing length < 2 check in main.js"
assert 'passNumSym' in js_content, "Missing passNumSym in main.js"
assert 'updateRule' in js_content, "Missing updateRule in main.js"
print("  [OK] main.js contains complete name and password strength logic.")

if name_issues:
    print("\n[FAIL] Name issues found:")
    for f, inp in name_issues:
        print(f"  {f}: {inp}")
else:
    print("\n>>> ALL CHECKS PASSED PERFECTLY! <<<")
