const { decode, secret } = require('../../src/book_cipher_async/book_cipher_async');

describe('book_cipher_async', function () {
  it('* secret object should be decoded successfully', () => {
    let result = 'Remove';

    decode(secret).then((res) => {
      expect(res).toBe(result);
    });
  });
});
