# Substitution Ciphers Tests

## Tests Eco-System

The tests here for the substitution ciphers sample code were written for [Pytest][1].
Pytest is an open source framework for testing Python code. It is a no-boilerplate alternative to 
Python’s standard unittest module.

Pytest had to be installed locally for development, and remotely on the build server, which is
Travis CI in our case. The installation on both locations was done using [pip][2] package manager
for Python packages. Pip is used with the list of dependencies in: `cryptography/requirements.txt`:

```bash
$ pip install -r requirements.txt
```

Installation instructions of pip for various environments are available on [pip official site][3].

## Executing the Tests

To run the tests locally, use the following commands:

```bash
$ cd cryptography
$ pytest
```

---

[1]: https://pytest.org/
[2]: https://pypi.org/project/pip/
[3]: https://pip.pypa.io/en/stable/installing/
