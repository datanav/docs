.. _csv_endpoint_sink:


CSV endpoint sink
-----------------

This is a data sink that registers an HTTP publisher endpoint that one can get entities in
`CSV format <https://en.wikipedia.org/wiki/Comma-separated_values>`_ from.

A pipe that references the ``CSV endpoint`` sink will not pump any
entities. In practice this means that a pump is not configured for the
pipe; the only way for entities to flow through the pipe is by
retrieving them from the CSV endpoint using a client that supports the HTTP protocol.

It exposes the URLs:

.. list-table::
   :header-rows: 1
   :widths: 100

   * - URL

   * - ``http://localhost:9042/api/publishers/mypipe/csv``
   * - ``http://localhost:9042/api/publishers/mypipe/csv/some_filename.csv``

The exposed URL may support additional parameters such as ``since`` and ``limit`` - see
the `API reference <./api.html#get--publishers-pipe_id-csv>`__ for the full details.

Note that you can optionally specify the filename to use in the ``Content-Disposition`` header of the HTTP response as
the last path element of the URL.

Prototype
^^^^^^^^^

::

    {
        "type": "csv_endpoint",
        "columns": ["properties","to","use","as","columns"],
        "quoting": "all|minimal|non-numeric|none",
        "delimiter": ",",
        "doublequote": true,
        "include_header": true,
        "escapechar": null,
        "lineterminator": "\r\n",
        "quotechar": "\"",
        "encoding": "utf-8",
        "encode_error_strategy": "replacement-strategy-to-use",
        "skip-deleted-entities": true,
        "filename": "my_data.csv",
        "content_disposition": "attachment"
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``columns``
     - List<String>
     - A list of string keys to look up in the entity to construct the CSV columns. If ``include_header`` is set to
       ``true`` (which is the default), this list will also be included as the first line of the CSV file.
     -
     - Yes

   * - ``quoting``
     - Enum<String>
     - A string from the set of "all", "minimal", "non-numeric" and "none" that describes how the fields of the CSV
       file will be quoted. A value of "all" means all fields will be quoted, even if they don't contain the ``quotechar``
       or ``delimiter`` characters. A value of "non-numeric" means all non-numeric values will be quoted. The "minimal"
       setting (the default) means only fields with contents that need to be quoted will be quoted. Finally, the ``none``
       value means do not quote (note this can produce broken CSV files if there are values that have to be quoted).
     - ``"minimal"``
     -

   * - ``delimiter``
     - String
     - The character to use as field separator. It will also affect which fields will be quoted if the ``quoting`` setting
       is set to ``minimal"`` (which is the default). The default value is to use the comma (``","``) character.
     - ``","``
     -

   * - ``doublequote``
     - Boolean
     - Controls how instances of ``quotechar`` appearing inside a field should themselves be quoted. When set to
       ``true`` (the default), the character is doubled (repeated). When set to ``false``, the ``escapechar`` property
       setting is used as a prefix to the ``quotechar``. If ``doublequoting`` is set to ``true`` but ``escapechar`` is
       not set, the backward slash character (``\``) is used as prefix.
     - ``true``
     -

   * - ``include_header``
     - Boolean
     - Controls if the ``columns`` property should be included as the header of the CSV file produced.
     - ``true``
     -

   * - ``escapechar``
     - String
     - A one-character string used by the sink to escape ``delimiter`` characters in fields if ``quoting`` is set to
       ``none`` and the ``quotechar`` if ``doublequote`` is set to ``false``. The default is ``null`` which disables
       escaping (except if ``doublequote`` is set to ``true``, in which case the default is ``\``).
     - ``null``
     -

   * - ``lineterminator``
     - String
     - A character sequence to use as the EOL marker in the CSV output. The default is carriage return plus linefeed
       (``"\r\n"``).
     - ``"\r\n"``
     -

   * - ``quotechar``
     - String
     - A one-character string that controls how to quote field values. The default is the double quote character. See
       ``doublequote`` and ``escapechar`` for related settings.
     - ``"\""``
     -

   * - ``byte_order_mark``
     - Boolean
     - If ``true`` the sink will emit a UTF-8 byte order mark (BOM) to the start of the file/stream. I should only be
       used in conjunction with a UTF-8 encoding.
     - ``false``
     -

   * - ``encoding``
     - String
     - Which encoding to use when converting the output to string values. The default is ``utf-8``. See
       `section 7.2.3 on this page <https://docs.python.org/3/library/codecs.html#codec-base-classes>`_ for a list of
       valid values.
     - ``"utf-8"``
     -

   * - ``encode_error_strategy``
     - String enum
     - An enumeration of "ignore", "replace", "xmlcharrefreplace" and "backslashreplace" that tells the sink how to deal
       with illegal characters in the output data when the ``encoding`` property is different than ``utf-8``.
       The default "backslashreplace" replaces the offending character(s) with backslash escaped unicode values
       (i.e. the ``"ę"`` character would be replaced with ``"\u0119"`` if it's illegal for the chosen encoding). The
       "replace" strategy will use a special unicode "replacement character" for unicode encodings,
       see https://en.wikipedia.org/wiki/Specials_%28Unicode_block%29 for more details or simply the ``"?"`` character
       if a non-unicode encoding. The "xmlcharrefreplace" replacement strategy uses numerical xml character values on
       the form ``"&#NNN;"``. The "ignore" strategy is the simplest and just skips any illegal characters entirely.
     - "backslashreplace"
     -
      .. _csv_endpoint_sink_param_skip_deleted_entities:

   * - ``skip-deleted-entities``
     - Boolean
     - This can be set to ``false`` to make deleted entities appear in the CSV output. The default is that
       deleted entities does not appear. If you set this to ``true`` you will also most likely want to include
       the "_deleted" attribute in the ``columns`` list, so that rows that represents deleted entities can be
       recognized. (If you need to rename or reformat the "_deleted" attribute you can do that by adding a
       :ref:`DTL transform <dtl_transform>` to the pipe.)
     - ``true``
     -

   * - ``filename``
     - String
     - This property provides a hint to HTTP clients on what filename to use when downloading data (via the
       ``Content-Disposition`` header property). Note that this property is not entirely standardized yet, so to be
       compatible with most HTTP clients, the filename should be ASCII characters only. For the same reason, quotes or
       backward or forward slashes should be avoided. If this property is not set, the contents will be served inline.
     -
     -

   * - ``content_disposition``
     - String
     - This property provides a hint to HTTP clients how to render the file data. The valid values are ``attachment``
       and ``inline``. It is used in the ``Content-Disposition`` header and the behaviour is client specific.
     - ``"attachment"``
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The pipe configuration given below will expose the ``my-entities``
publisher endpoint and read the entities from the ``my-entities``
dataset, picking the ``_id``, ``foo`` and ``bar`` properties as columns in the CSV file:

::

    {
        "_id": "my-entities",
        "name": "My published csv endpoint",
        "type": "pipe",
        "sink": {
            "type": "csv_endpoint"
            "columns": ["_id", "foo", "bar", "zoo"],
            "filename": "my_data.csv"
        }
    }

The data will be available at ``http://localhost:9042/api/publishers/my-entities/csv`` (or alternatively
``http://localhost:9042/api/publishers/my-entities/csv/some_other_filename.csv``)

