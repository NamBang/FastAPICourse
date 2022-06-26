Especially the case for user models:
- input model needs to be able to have a password
- output model should not have a password
- database model would probably need to have a hashed password

Note: Never store user's plaintext passwords. Always store a "secure hash" that you can the verify.

**dict_object
unwrapping a dict.
