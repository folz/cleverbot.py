# Changelog

## v2.0.0

* Incompatible Changes
  * `CleverbotAPIException` is renamed to `CleverbotServiceException`.

## v1.1.1

* Bugfix
  * [#38](https://github.com/folz/cleverbot.py/pull/38) - Update webservicemin resource URL.

## v1.1.0

* Bugfix
  * [#33](https://github.com/folz/cleverbot.py/pull/33) - Convert incoming responses from latin-1 to utf-8

## v.1.0.0

🎉🎈🎊!

## v0.9.0

* Enhancement
  * Update documentation to prepare for a 1.0.0 release.
  * Improved classifiers and metadata in setup.py.
  * Python 3.5 support.

## v0.2.1

* Enhancement
  * Add Python 3 language classifier to setup.py

## v0.2.0

* Enhancement
  * [#17](https://github.com/folz/cleverbot.py/issues/17) - Python 3 is now supported

* Incompatible Changes
  * [#19](https://github.com/folz/cleverbot.py/issues/19) - Underlying HTTP errors are no longer swallowed
  * [#19](https://github.com/folz/cleverbot.py/issues/19) - CleverbotAPIError is now thrown when the API request is denied
  * [#19](https://github.com/folz/cleverbot.py/issues/19) - Cleverbot response is now unescaped for HTML entities


## v0.1.5

TODO: Backport changelog to 0.1.5 and earlier. (Changelog was started in v0.2.0)
