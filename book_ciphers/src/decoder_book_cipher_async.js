// Async version of the book cipher decoder

function decode(secret) {
  let step = gen(secret), goal = step.next(), value = '';

  return new Promise(resolve => {
    while (!goal.done) {
      value += goal.value;
      goal = step.next();
    }
    return resolve(value);
  });
}

function* gen({ words, keys }) {
  while (words.length) {
    yield words.shift()[keys.splice(0, 10).reduce((a, b) => a ^ b, 0)];
  }
}

module.exports = decode;
