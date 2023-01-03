.. _concepts-environment-variables:

Environment Variables
=====================

An :ref:`environment variable <environment_variables>` is a named value that you can reference in your configuration. Environment variables are used to parameterize your configuration so that you can easily enable/disable or change certain aspects of your configuration. If you have an environment variable called ``myvariable`` then you can reference it in configuration like this: ``"$ENV(myvariable)"``.

.. NOTE::

    Do not use environment variables for sensitive values; use :ref:`secrets <concepts-secrets>` instead. Environment variables are global only.
