Encryption
==========

.. _encrypt_dtl_function:

``encrypt``
-----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   KEY(string{1})
       |   VALUES(value-expression{1})
       |
       | Encrypts the VALUES using the key in KEY
       | the data wil be encrypted using a symmetric Fernet algorithm with the key as the password. Note that this
       | function by itself does not offer an end-to-end secure system of encryption
       | as the key is stored along with the encrypted data. This applies even when using a ``$SECRET(secret key)`` via
       | the secrets manager.
       |
     - | ``["encrypt", "secret", ["list", "a", "b", "c"]]``
       |
       | Returns an encrypted bytes object.

.. _encrypt_pki_dtl_function:

``encrypt-pki``
---------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   PUBLIC_KEY(string{1})
       |   VALUES(value-expression{1})
       |
       | Encrypts the strings in VALUES using the public key in PUBLIC_KEY
       |
       | Note that this function requires the VALUES parameter to either be a string or a list of strings so
       | if you want to encrypt some property that is not a string or a list of strings,
       | you must convert it this form first, for example using the ``json`` or ``json-transit`` serialize functions.
       |
       | The PUBLIC_KEY parameter must be a RSA public key in PEM format (PKCSv8, which starts with the header
       | "-----BEGIN PUBLIC KEY-----"). The input is encrypted using an asymmetric RSA 2048 bits
       | encryption algorithm - to decrypt the data you must use the corresponding private key. See ``decrypt-pki``.
       |
       | Note that this function can't encrypt large strings, it is intended to encrypt shorter passphrases or similar
       | identifiers. Use the ``encrypt-pgp`` function instead if you need to encrypt larger blocks of data.
       |
     - | ``["encrypt-pki", "RSA_PEM_public_key", ["json-transit", ["list", "a", "b", "c"]]]``
       |
       | Returns a list of bytes objects: ``["~bDHAERS..", "~bHDURKSS..", "~bXYSERS.."]``
       |
       | ``["encrypt-pki", "RSA_PEM_public_key", "secret-passphrase"]``
       |
       | Returns a single bytes object: ``"~bDHAERS.."``
       |
       | ``["encrypt-pki", "$SECRET(key-secret-name)", "$SECRET(secret-passphrase-name)"]``
       |
       | Returns a single bytes object: ``"~bDHAERS.."``

.. _encrypt_pgp_dtl_function:

``encrypt-pgp``
---------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   PUBLIC_KEY(string{1})
       |   VALUES(value-expression{1})
       |
       | Encrypts the strings in VALUES in OpenPGP format using the PGP public key in PUBLIC_KEY
       |
       | Note that this function requires the VALUES parameter to either be a string or a list of strings so
       | if you want to encrypt some property that is not a string or a list of strings,
       | you must convert it this form first, for example using the ``json`` or ``json-transit`` serialize functions.
       |
       | The PUBLIC_KEY parameter must be a PGP public key which starts with the header
       | "-----BEGIN PGP PUBLIC KEY-----"). The resulting encrypted data is stored in OpenPGP form (RFC4880, https://tools.ietf.org/html/rfc4880)
       | To decrypt the data you must use the corresponding private key and associated password. See ``decrypt-pgp``.
       |
       |
     - | ``["encrypt-pgp", "OpenPGP_public_key", ["json-transit", ["list", "a", "b", "c"]]]``
       |
       | Returns a list of strings in OpenPGP ASCII format:
       | ``["----BEGIN PGP MESSAGE..", "----BEGIN PGP MESSAGE..", "----BEGIN PGP MESSAGE.."]``
       |
       | ``["encrypt-pgp", "OpenPGP_public_key", "secret-message"]``
       |
       | Returns a single OpenPGP message in ASCII format: ``"----BEGIN PGP MESSAGE.."``
       |
       | ``["encrypt-pgp", "$SECRET(key-secret-name)", "secret-message"]``
       |
       | Returns a single OpenPGP message in ASCII format: ``"----BEGIN PGP MESSAGE.."``

.. _decrypt_dtl_function:

``decrypt``
-----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   KEY(string{1})
       |   VALUES(value-expression{1})
       |
       | The key is assumed to be a matching password used by a previous ``encrypt``
       | function, i.e. it is symmetric with ``encrypt`` if the same key is used:
       |
     - | ``["decrypt", "secret", ["encrypt", "secret", ["list", "a", "b", "c"]]]``
       |
       | Returns ``["a", "b", "c"]``
       |
       | ``["decrypt", "$SECRET(secret-name)", ["encrypt", "$SECRET(secret-name)", ["list", "a", "b", "c"]]]``
       |
       | Returns ``["a", "b", "c"]``
       |

.. _decrypt_pki_dtl_function:

``decrypt-pki``
---------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   PRIVATE_KEY(string{1})
       |   VALUES(value-expression{1})
       |
       | Decrypts the bytes objects in VALUES using the private key in PRIVATE_KEY.
       |
       | Note that this function requires the VALUES parameter to either be a single bytes object or a list of bytes
       | objects.
       |
       | The PRIVATE_KEY parameter must be a RSA private key in PEM format (PKSv8, which starts with the header
       | "-----BEGIN RSA PRIVATE KEY-----"). The bytes data in VALUE is then decrypted to a string using the asymmetric
       | RSA 2048 bits algorithm - the data must have been encrypted with the corresponding public key. If the data
       | is encoded as a string, it must be cast (for example using ``datetime-parse``) or decoded using an appropriate
       | function such as ``json-parse`` or ``json-transit-parse``.
       |
     - | ``["json-transit-parse",``
       |    ``["decrypt-pki", "-----BEGIN RSA PRIVATE KEY-----..-----END RSA PRIVATE KEY-----",``
       |       ``["encrypt-pki", "-----BEGIN PUBLIC KEY-----..-----END PUBLIC KEY-----",``
       |           ``["json-transit", ["list", ["list", "a", "b", "c"]]]]]``

       | Returns ``["a", "b", "c"]``
       |
       | ``["json-transit-parse",``
       |    ``["decrypt-pki", "$SECRET(private-key-name)",``
       |       ``["encrypt-pki", "-----BEGIN PUBLIC KEY-----..-----END PUBLIC KEY-----",``
       |           ``["json-transit", ["list", ["list", "a", "b", "c"]]]]]``

       | Returns ``["a", "b", "c"]``
       |

.. _decrypt_pgp_dtl_function:

``decrypt-pgp``
---------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   PRIVATE_KEY(string{1})
       |   PASSPHRASE(string{1})
       |   VALUES(value-expression{1})
       |
       | Decrypts the strings in VALUES in OpenPGP format using the PGP private key in PRIVATE_KEY and the password in
       | PASSPHRASE.
       |
       | Note that this function requires the VALUES parameter to either be a string or a list of strings in OpenPGP
       | message format (these are ASCII strings starting with the header "----BEGIN PGP MESSAGE..", see RFC4880,
       | https://tools.ietf.org/html/rfc4880).
       |
       | The PRIVATE_KEY parameter must be a PGP private key which starts with the header
       | "-----BEGIN PGP PRIVATE KEY-----") and the password in PASSPHRASE must match this key so it can be unlocked.
       |
     - | ``["decrypt-pgp", "-----BEGIN PGP PRIVATE KEY..", "valid-password",``
       |     ``["encrypt-pgp", "-----BEGIN PGP PUBLIC KEY..", ["list", "data", "data2"]]]``
       |
       | Returns a list: ``["data", "data2"]``
       |
       | ``["decrypt-pgp", "-----BEGIN PGP PRIVATE KEY..", "valid-password",``
       |    ``["encrypt-pgp", "-----BEGIN PGP PUBLIC KEY..", "secret message"]]``
       |
       | Returns a string: ``"secret message"``
       |
       | ``["decrypt-pgp", "$SECRET(private-key-name)", "$SECRET(password-name)",``
       |    ``["encrypt-pgp", "-----BEGIN PGP PUBLIC KEY..", "secret message"]]``
       |
       | Returns a string: ``"secret message"``
