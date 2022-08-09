

.. _csv_source:

CSV source
----------

The CSV data source translates the rows of files in `CSV format <https://en.wikipedia.org/wiki/Comma-separated_values>`_
to entities.

The configuration options are:

Prototype
^^^^^^^^^

::

    {
       "type": "csv",
       "system": "a-valid-url-or-microservice-system-id",
       "url": "url-to-csv-file",
       "has_header": true,
       "field_names": ["mappings","from","columns","to","properties"],
       "auto_dialect": true,
       "dialect": "excel",
       "encoding": "utf-8",
       "decode_error_strategy": "strict-or-replace",
       "primary_key": ["list","of","column","names"],
       "whitelist": ["list","of","column","names","to","include"],
       "blacklist": ["list","of","column","names","to","exclude"],
       "preserve_empty_strings": false,
       "delimiter": ",",
       "escape_null_bytes": false
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

   * - ``url``
     - String
     - The URL of the ``CVS`` file to load.
     -
     - Yes

   * - ``system``
     - String
     - The ID of the :ref:`URL system <url_system>` or :ref:`microservice system <microservice_system>` component to use.
     -
     - Yes

   * - ``has_header``
     - Boolean
     - Flag that indicates to the source that the first row in the ``CSV`` file contains the names of the columns.
       If this property is set to ``false``, you will have to provide a list of column names in the ``field_names``
       property.
     - true
     -

   * - ``field_names``
     - List
     - If set, specifies the names of the columns. It takes precedence over the header in the CSV file if present.
     -
     -

   * - ``auto_dialect``
     - Boolean
     - Flag that hints to the source that it should try to guess the dialect of the ``CSV`` file on its own. Note
       that if ``dialect`` is explicitly set, ``auto_dialect`` is ignored.
     - true
     -

   * - ``dialect``
     - String
     - Encodes what type of CSV file the file is. This is basically presets of the other properties.
       The recognised values are ``"excel"``, ``"excel_tab"`` and ``"unix_dialect"``.
       Note that if ``dialect`` is explicitly set, ``auto_dialect`` is ignored. If both ``auto_dialect`` is ``false`` and
       no ``dialect`` has been explicitly set, the dialect chosen will be ``excel``.
     -
     -

   * - ``encoding``
     - String
     - The character set to used to encode the text in the CSV file
     - "UTF-8"
     -

   * - ``decode_error_strategy``
     - String
     - A enumeration of "strict" and "replace" that tells the character decoder how to deal with illegal characters
       in the input data. The default is "strict" which raises an error and stops processing. The "replace" option
       will log a warning and attempt to replace the offending character(s) with the unicode special character for
       "replacement character", see https://en.wikipedia.org/wiki/Specials_%28Unicode_block%29 for more details.
       Use the "replace" option with extreme care as it can lead to data loss if you're not absolutely sure of what
       you are doing. The preferred option should always be to try the fix the data at the source.
     - "strict"
     -

   * - ``primary_key``
     - List<String> or String
     - The name of the column(s) to use as ``_id`` in the generated entities. It can be either a list of strings
       (if the identity is a compound value) or a single column name (i.e. a string). The column name(s) are case
       sensitive and must match the contents of either ``field_names`` or the header of the CSV file.
     -
     - Yes

   * - ``whitelist``
     - List<String>
     - The names of the columns to include in the generated entities. If there is a ``blacklist`` also specified, the
       whitelist will be filtered against the contents of the blacklist.
     -
     -

   * - ``blacklist``
     - List<String>
     - The names of the columns to exclude from the generated entities. If there is a ``whitelist`` also specified, the
       blacklist operates on the values of the whitelist (and not the whole columnset).
     -
     -

   * - ``preserve_empty_strings``
     - Boolean
     - If set to ``true`` will include column values that are empty strings. By default these are omitted.
     - False
     -

   * - ``delimiter``
     - String
     - The character or string to use as the ``CSV`` field separator (delimiter)
     - ","
     -

   * - ``escape_null_bytes``
     - Boolean
     - If set to ``true``, null characters in the CSV will be escaped before the data is parsed. Null characters in a
       CSV file can fail the pipe if they are not escaped. By default, this is set to ``false`` due to performance
       reasons.
     - ``false``
     -

Continuation support
^^^^^^^^^^^^^^^^^^^^

See the section on :ref:`continuation support <continuation_support>` for more information.

.. list-table::
   :header-rows: 1
   :widths: 10, 80

   * - Property
     - Value

   * - ``supports_since``
     - ``false`` (Default)

   * - ``is_since_comparable``
     - ``true`` (Default)

   * - ``is_chronological``
     - ``false`` (Default)

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "source": {
            "type": "csv",
            "url": "http://blog.plsoucy.com/wp-content/uploads/2012/04/countries-20140629.csv",
            "primary_key": "Code",
            "encoding": "iso-8859-1"
        }
    }
