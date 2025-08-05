:orphan:

.. _jinja_filters_section:


Jinja filters
=============
In addition to the `built-in filters <https://jinja.palletsprojects.com/en/stable/templates/#list-of-builtin-filters>`_,
we have also defined custom Jinja filters that can be used in pipe and system configurations. Some of these filters
produce the same output as the corresponding DTL function (see :ref:`table <dtl_filters>`), e.g. the ``bytes`` filter should give the same
results as the ``bytes`` DTL function. Note that underscores are used in place of dashes in filter names, as
opposed to DTL functions. System secrets and subscription-wide secrets can be used inside the filters
with ``secret('secret-name')``.



.. _custom_jinja_filters:

``decode_jwt``
^^^^^^^^^^^^^^

Decodes a JWT given a (public) key. Also supports supplying a JSON Web Key Set (JWKS) URL in place of a key. See the
table below for all supported arguments. Example usage: ``secret('jwt') | decode_jwt(key=secret('public_key'))``

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 5

   * - Argument
     - Type
     - Description
     - Default
     - Req

   * - ``key``
     - String
     - The public key used for decoding the JWT.
     -
     - Yes, if ``jwks_url`` is not used

   * - ``jwks_url``
     - String
     - An HTTPS endpoint containing JSON Web Keys (JWKS). Can be used in place of ``key``. The filter will
       decode the JWT using the key(s) provided in the endpoint.
     -
     - Yes, if ``key`` is not used

   * - ``algorithms``
     - List<String>
     - List of allowed algorithms.
     - ``['RS256']``
     - No

   * - ``verify``
     - Boolean
     - Whether the JWT signature should be verified.
     - ``true``
     - No

   * - ``require``
     - Str, List<String>
     - List of claims that must be present.
     -
     - No

   * - ``detached_payload``
     - Bytes
     - A payload to verify the signature against. Used for tokens that are not carrying a payload.
     -
     - No

   * - ``verify_aud``
     - Boolean
     - Check that the ``aud`` claim matches ``audience``. Defaults to the value of ``verify``.
     -
     - No

   * - ``verify_iss``
     - Boolean
     - Check that the ``iss`` claim matches ``issuer``. Defaults to the value of ``verify``.
     -
     - No

   * - ``verify_exp``
     - Boolean
     - Check that ``exp`` (expiration) claim value is in the future. Defaults to the value of ``verify``.
     -
     - No

   * - ``verify_iat``
     - Boolean
     - Check that ``iat`` (issued at) claim value is an integer. Defaults to the value of ``verify``.
     -
     - No

   * - ``verify_nbf``
     - Boolean
     - Check that ``nbf`` (not before) claim value is in the past. Defaults to the value of ``verify``.
     -
     - No

   * - ``strict_aud``
     - Boolean
     - Check that the aud claim is a single value (not a list), and matches ``audience`` exactly.
     - ``false``
     - No

   * - ``audience``
     - String, List<String>
     - The value to check against if ``verify_aud`` is true.
     -
     - No

   * - ``issuer``
     - String
     - The value to check against if ``verify_iss`` is true.
     -
     - No

   * - ``leeway``
     - Integer, Float
     - A time margin in seconds for the JWT expiration check.
     - ``0``
     - No

.. _dtl_filters:

DTL-equivalent filters
^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 60

   * - Filter
     - Description

   * - ``bytes``
     - See the :ref:`bytes <bytes_dtl_function>` DTL function.

   * - ``base64_encode``
     - See the :ref:`base64-encode <base64_encode_dtl_function>` DTL function.

   * - ``base64_decode``
     - See the :ref:`base64-decode <base64_decode_dtl_function>` DTL function.

   * - ``datetime``
     - See the :ref:`datetime <datetime_dtl_function>` DTL function.

   * - ``datetime_format``
     - See the :ref:`datetime-format <datetime_format_dtl_function>` DTL function.
