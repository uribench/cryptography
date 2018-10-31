const decode = require('../src/decoder_book_cipher_sync');
const secret_1 = require('../src/secrets/secret_1');
const secret_2 = require('../src/secrets/secret_2');

describe('decoder_book_cipher_sync', function () {

  it('should decode secret_1 successfully', () => {
    let result = 'Remove';

    expect(decode(secret_1)).toBe(result);
  });

  it('should decode secret_2 successfully', () => {
    let result = 'Pass';

    expect(decode(secret_2)).toBe(result);
  });

});
