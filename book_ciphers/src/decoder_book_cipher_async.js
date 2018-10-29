// Async version of the book cipher decoder

function decode({ words, keys }) {
  let step = gen({ words, keys }), goal = step.next(), value = '';

  return new Promise(resolve => {
    while (!goal.done) {
      value += goal.value;
      goal = step.next();
    }
    return resolve(value);
  });
}

function* gen({ words, keys }) {
  let splice_size = keys.length/words.length;

  while (words.length) {
    yield words.shift()[keys.splice(0, splice_size).reduce((a, b) => a ^ b, 0)];
  }
}

module.exports = decode;
