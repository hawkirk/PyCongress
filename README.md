# PyCongress
Python client for [Congress.gov's API](https://api.congress.gov/).

## Setup
`pycongress` is supported on Python 3.8+ and it can be installed using [pip]().

```bash
$ pip install pycongress
```

Prior to using the library you'll need to [sign up for an API Key from Congress.Gov](https://api.congress.gov/sign-up/).

Store your key as an environment variable named `CONGRESS_API_KEY` and it will automatically be passed through the client for authentication.

You may also manually declare your key:

```python
congress = Congress(api_key="Insert key here")
```

## Usage



## Misc.

`pycongress` currently only supports the `bill`, `member`, and `congress` endpoints. Support for more endpoints is planned in the future. Feel free to contribute if there are features you'd like to see!

This project was inspired by [propublica-congress](https://github.com/eyeseast/propublica-congress).

The Congress.Gov API is currently in beta. Visit the Library of Congress [blog](https://blogs.loc.gov/law/2022/09/introducing-the-congress-gov-api/) or [GitHub page](https://github.com/LibraryOfCongress/api.congress.gov/) for additional information.