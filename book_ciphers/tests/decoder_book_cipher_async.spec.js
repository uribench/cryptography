const decode = require('../src/decoder_book_cipher_async');
const secret = require('../src/secrets/secret_1');

describe('decoder_book_cipher_async', function () {
  it('should decode the secret object successfully', () => {
    let result = 'Remove';
    // let secret_module = '../src/secrets/secret_1'

    // delete require.cache[require.resolve(secret_module)]
    // var secret = require(secret_module);

    decode(secret).then((res) => {
      expect(res).toBe(result);
    });
  });
});
