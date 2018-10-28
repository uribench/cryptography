const { decode, secret } = require('../../src/book_cipher_sync/book_cipher_sync');

describe('book_cipher_sync', () => {
  it('* secret object should be decoded successfully', () => {
    let result = 'Remove';

    expect(decode(secret)).toBe(result);
  });
});
