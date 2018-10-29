// Sync version of the book cipher decoder

function decode({ words, keys }) {
  let value = '';
  let splice_size = keys.length/words.length;

  while (words.length) {
    value += words.shift()[keys.splice(0, splice_size).reduce((a, b) => a ^ b, 0)];
  }

  return value;
}

module.exports = decode;
