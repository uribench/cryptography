const decode = require('../src/decoder_book_cipher_sync');
const secret = require('../src/secrets/secret_2');

describe('decoder_book_cipher_sync', () => {
  it('* secret object should be decoded successfully', () => {
    let result = 'Remove';

    expect(decode(secret)).toBe(result);
  });
});
