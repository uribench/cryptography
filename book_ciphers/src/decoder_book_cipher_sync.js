// Sync version of the book cipher decoder

function decode({ words, keys }) {
  let value = '';

  while (words.length) {
    value += words.shift()[keys.splice(0, 10).reduce((a, b) => a ^ b, 0)];
  }

  return value;
}

module.exports = decode;
