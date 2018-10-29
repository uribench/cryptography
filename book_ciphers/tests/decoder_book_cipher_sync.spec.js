const decode = require('../src/decoder_book_cipher_sync');
const secret = require('../src/secrets/secret_2');

describe('decoder_book_cipher_sync', function () {
  it('should decode the secret object successfully', () => {
    let result = 'Pass';

    expect(decode(secret)).toBe(result);
  });
});
