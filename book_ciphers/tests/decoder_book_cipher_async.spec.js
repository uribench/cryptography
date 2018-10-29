const decode = require('../src/decoder_book_cipher_async');
const secret = require('../src/secrets/secret_1');

describe('decoder_book_cipher_async', function () {
  it('* secret object should be decoded successfully', () => {
    let result = 'Remove';

    decode(secret).then((res) => {
      expect(res).toBe(result);
    });
  });
});
