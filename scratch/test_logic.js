// Unit test simulating main.js form and password validation logic

function testValidation() {
  console.log("=== RUNNING JAVASCRIPT VALIDATION LOGIC TESTS ===");

  var nameRegex = /^[a-zA-ZÀ-ÿ\u0600-\u06FF\u0750-\u077F\u0900-\u097F\s'.\-]{2,}$/;

  function validateName(val) {
    var trimmed = (val || '').trim();
    return trimmed.length >= 2 && nameRegex.test(trimmed);
  }

  // Test name cases
  const nameCases = [
    { input: 'a', expected: false, desc: 'Single letter "a"' },
    { input: 'A', expected: false, desc: 'Single letter "A"' },
    { input: ' a ', expected: false, desc: 'Single letter with whitespace' },
    { input: '', expected: false, desc: 'Empty name' },
    { input: '12', expected: false, desc: 'Digits only' },
    { input: 'Ab', expected: true, desc: 'Two letters "Ab"' },
    { input: 'John Doe', expected: true, desc: 'Full name "John Doe"' },
    { input: "Dr. O'Connor-Smith", expected: true, desc: 'Special chars in name' },
    { input: 'राजेश शर्मा', expected: true, desc: 'Hindi/Devanagari name' },
    { input: 'عمران خان', expected: true, desc: 'Arabic/Urdu name' }
  ];

  let namePassCount = 0;
  for (let c of nameCases) {
    let result = validateName(c.input);
    if (result === c.expected) {
      console.log(`  [PASS] ${c.desc}: ${c.input} => ${result}`);
      namePassCount++;
    } else {
      console.error(`  [FAIL] ${c.desc}: ${c.input} => got ${result}, expected ${c.expected}`);
    }
  }

  console.log("\n=== RUNNING PASSWORD EVALUATION LOGIC TESTS ===");

  function evaluatePassword(val) {
    if (!val) return { level: 0, label: '—', passLength: false, passCases: false, passNumSym: false };
    var passLength = val.length >= 8;
    var passCases = /[a-z]/.test(val) && /[A-Z]/.test(val);
    var passNumSym = /[0-9!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?`~]/.test(val);

    var score = 0;
    if (val.length >= 6) score++;
    if (passLength) score++;
    if (passCases) score++;
    if (passNumSym) score++;

    var level = 1;
    if (score === 3) {
      level = 2;
    } else if (score >= 4) {
      if (val.length >= 10 || (/[0-9]/.test(val) && /[^a-zA-Z0-9]/.test(val))) {
        level = 4;
      } else {
        level = 3;
      }
    }

    var labels = { 1: 'Weak', 2: 'Fair', 3: 'Good', 4: 'Strong' };

    return {
      level: level,
      label: labels[level],
      passLength: passLength,
      passCases: passCases,
      passNumSym: passNumSym,
      isValidForSubmit: passLength && passCases && passNumSym
    };
  }

  const pwdCases = [
    { input: 'abc', expectedLabel: 'Weak', isValid: false, desc: 'Short password' },
    { input: 'password', expectedLabel: 'Fair', isValid: false, desc: 'Lowercase only length 8' },
    { input: 'Password', expectedLabel: 'Fair', isValid: false, desc: 'Mixed case length 8 no digits' },
    { input: 'Password1', expectedLabel: 'Good', isValid: true, desc: 'Mixed case + digit length 9' },
    { input: 'Password@2026', expectedLabel: 'Strong', isValid: true, desc: 'Mixed case + digit + symbol length 13' }
  ];

  let pwdPassCount = 0;
  for (let c of pwdCases) {
    let res = evaluatePassword(c.input);
    let ok = res.label === c.expectedLabel && res.isValidForSubmit === c.isValid;
    if (ok) {
      console.log(`  [PASS] ${c.desc}: "${c.input}" => level=${res.level} (${res.label}), valid=${res.isValidForSubmit}`);
      pwdPassCount++;
    } else {
      console.error(`  [FAIL] ${c.desc}: got ${res.label}/${res.isValidForSubmit}, expected ${c.expectedLabel}/${c.isValid}`);
    }
  }

  if (namePassCount === nameCases.length && pwdPassCount === pwdCases.length) {
    console.log("\n>>> ALL VALIDATION UNIT TESTS PASSED! <<<");
  } else {
    process.exit(1);
  }
}

testValidation();
