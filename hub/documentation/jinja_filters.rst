.. _jinja_filters_section:


Jinja filters
=============
In addition to the `built-in filters <https://jinja.palletsprojects.com/en/stable/templates/#list-of-builtin-filters>`_,
we have also defined custom Jinja filters that can be used in pipe and system configurations. Most of these filters
have a corresponding DTL function and should produce the same output, e.g. the ``bytes`` filter should give the same
results as the ``bytes`` DTL function. Note that underscores are used in place of dashes in filter names, as
opposed to DTL functions.

.. _custom_jinja_filters:

Custom Jinja filters
----------

.. list-table::
   :header-rows: 1
   :widths: 10, 60, 10, 40

   * - Filter
     - Description
     - Arguments
     - Example usage

   * - ``bytes``
     - See the :ref:`bytes <bytes_dtl_function>` DTL function.
     - None
     -

   * - ``base64_encode``
     - See the :ref:`base64-encode <base64_encode_dtl_function>` DTL function.
     - None
     -

   * - ``base64_decode``
     - See the :ref:`base64-decode <base64_decode_dtl_function>` DTL function.
     - None
     -

   * - ``datetime``
     - See the :ref:`datetime <datetime_dtl_function>` DTL function.
     -
     -

   * - ``datetime_filter``
     - See the :ref:`datetime-format <datetime_format_dtl_function>` DTL function.
     -
     -

   * - ``decode_jwt``
     - Decodes a JWT given a (public) key.
     - key
     - ``decode_jwt(secret('public_key'))``