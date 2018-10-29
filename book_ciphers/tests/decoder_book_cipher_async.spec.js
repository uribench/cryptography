const decode = require('../src/decoder_book_cipher_async');
const secret_1 = require('../src/secrets/secret_1');
const secret_2 = require('../src/secrets/secret_2');

describe('decoder_book_cipher_async', function () {
  it('should decode the secret object successfully', () => {
    let result = 'Remove';

    decode(secret_1).then((res) => {
      expect(res).toBe(result);
    });
  });
});
