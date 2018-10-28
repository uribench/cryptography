function decode({ words, keys }) {
  let value = '';

  while (words.length) {
    value += words.shift()[keys.splice(0, 10).reduce((a, b) => a ^ b)];
  }

  return value;
}

const secret = {
  words: [
    'Redundant', 'comments', 'merely', 'collect', 'deceptive', 'descriptions'],
  keys: [
    4, 2, 3, 4, 5, 2, 3, 5, 2, 2,
    1, 0, 2, 7, 3, 4, 2, 4, 7, 6,
    0, 1, 6, 2, 4, 6, 4, 1, 6, 4,
    1, 0, 6, 2, 7, 3, 7, 6, 1, 0,
    0, 0, 1, 4, 3, 3, 5, 0, 1, 6,
    0, 5, 4, 6, 7, 0, 6, 2, 1, 4]
};

// decode(secret);

module.exports = { decode, secret };
