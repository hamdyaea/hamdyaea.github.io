// Developer: Hamdy Abou El Anein
// Contact: hamdy.aea@protonmail.com
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
for (const reduced of [false, true]) {
  let calls = 0;
  const intro = { offsetHeight: 100, style: {} };
  vm.runInNewContext(fs.readFileSync('js/demo.js', 'utf8'), {
    window: { matchMedia: () => ({ matches: reduced }) },
    document: {
      addEventListener: (_, fn) => fn(),
      getElementById: () => intro,
    },
    particleground: () => { calls++; },
  });
  assert.equal(calls, reduced ? 0 : 1);
  assert.equal(intro.style.marginTop, '-50px');
}
console.log('Both motion preferences passed');
