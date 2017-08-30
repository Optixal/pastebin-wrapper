# Pastebin Python Wrapper

A lightweight Pastebin wrapper written in Python 3 using the Requests library.

Functions Available:
  * paste (both anonymous and authenticated)
  * login (for authenticated pastes)

Dependencies:
  * requests

A dev key is required to use Pastebin's API. Export your dev key as an environment variable, optionally you can pass it to pastebin.py's functions as an argument, or you can also hardcode it into pastebin.py.

```sh
export PASTEBIN_DEV_KEY=abc123def456ghi789
```

Create an anonymous paste:

```python
>>> import pastebin
>>> url = pastebin.paste('Hello World!')
>>> url
'https://pastebin.com/znMDYswm'
```

Create a paste associated with your username:

```sh
export PASTEBIN_USER_NAME=abc
export PASTEBIN_USER_PASSWORD=123
```

```python
>>> import pastebin
>>> user_key = pastebin.login()
>>> url = pastebin.paste('Hello World!', user_key=user_key)
>>> url
'https://pastebin.com/abc123'
```

