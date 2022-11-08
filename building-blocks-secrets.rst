.. _concepts-secrets:

Secrets
=======

:ref:`Secrets <secrets_manager>` are like environment variables except that they are write-only. Once written to the API you cannot read them back out, but you can reference them in your configuration. They should be used for sensitive values like passwords and other credentials.

A secret can only be used in certain locations of the configuration. If you have a secret called ``mysecret`` then you can reference it in configuration like this: ``"$SECRET(mysecret)"``.

It is recommended that secrets are local. They can also be global but it is not recommended.
