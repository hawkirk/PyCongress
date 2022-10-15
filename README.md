# PyCongress

[![PyPI version](https://badge.fury.io/py/pycongress.svg)](https://badge.fury.io/py/pycongress)
[![Python version](https://img.shields.io/badge/python-3.x-brightgreen.svg)](https://pypi.org/project/pycongress/)


Python client for [Congress.gov's API](https://api.congress.gov/).

## Setup

[Sign up for an API Key from Congress.Gov](https://api.congress.gov/sign-up/)
prior to using the library.

Store your key as an environment variable named `CONGRESS_API_KEY` and it will automatically be passed through the client for authentication.

You may also manually declare your key:

```python
congress = Congress(api_key="Insert key here")
```

## Misc.

`pycongress` currently only supports the `bill`, `member`, and `congress` endpoints. Support for more endpoints is planned in the future.

This project was inspired by [propublica-congress](https://github.com/eyeseast/propublica-congress).

The Congress.Gov API is currently in beta. Visit the Library of Congress [blog](https://blogs.loc.gov/law/2022/09/introducing-the-congress-gov-api/) or [GitHub page](https://github.com/LibraryOfCongress/api.congress.gov/) for more information.

## License

[MIT](LICENSE)
