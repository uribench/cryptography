# Book Ciphers Tests

## Tests Eco-System

The tests here for the book ciphers sample code were written for [Jasmine][1].
Jasmine is an open source behavior-driven development (BDD) framework for testing JavaScript code.

Jasmine had to be installed locally for development, and remotely on the build server, which is
Travis CI in our case. The installation on both locations was done using [yarn][2], instead of the
most popular package manager [npm][3].

Yarn is a new open source package manager that replaces the existing workflow for the npm client or 
other package managers while remaining compatible with the npm registry. Yarn is a collaboration of 
facebook, Exponent, Google, and Tilde. With Yarn, engineers still have access to the npm registry, 
but can install packages more quickly and manage dependencies consistently across machines or in 
secure offline environments.

When dealing with large projects [npm suffers from consistency, security, and performance][4].

Installation instructions for various environments are available on [yarnpkg official site][5].

## Executing the Tests

Depending on your local installation, you can use either yarn or npm interchangeably as follows:

```bash
$ cd cryptography/book_ciphers
$ yarn test
```

or

```bash
$ cd cryptography/book_ciphers
$ npm test
```

Both yarn and npm are using the same configuration files and are executing the below script in:

`cryptography/book_ciphers/package.json`

```json
  "scripts": {
    "test": "node ./tests/spec_runner.js"
  }
```

The execution of the tests will use the following configuration file, including the custom reporter: 
`cryptography/book_ciphers/tests/spec_runner.js`

---

[1]: https://jasmine.github.io/
[2]: https://yarnpkg.com/en/
[3]: https://www.npmjs.com/
[4]: https://code.fb.com/web/yarn-a-new-package-manager-for-javascript/
[5]: https://yarnpkg.com/en/docs/install#debian-stable
