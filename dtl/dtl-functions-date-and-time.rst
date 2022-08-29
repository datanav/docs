Date and time
=============

A general note on timezone conversion functions: Sesam relies on tabulated historical data for daylight
saving information for the various timezones. This data gets corrected or supplemented from time to time which means
that the result of an explicit or implicit timezone conversion operation can change over time.

.. _now_dtl_function:

``now``
-------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   NONE(value-expression{0})
       |
       | Returns the current time as a datetime value.
       |
     - | ``["now"]``
       |
       | Returns the current time as a datetime value, e.g.
         "~t2016-05-13T14:32:00.431Z".

       .. WARNING::

          This function is non-deterministic and will return a
          different value every time it is evaluated. Be aware that if
          the pipe is rewound or reset then it will produce a
          different output. Dependency tracking will also have a
          similar effect as to produce a different value when entities
          are reprocessed.

          *Use this function with care and make sure
          that you are aware of the consequences of reprocessing
          entities.*

.. _datetime_dtl_function:

``datetime``
------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   FUNCTION(default-value-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | Translates all non-null input values to datetime values. If no default value
         expression is given, values that don't parse as datetime values will
         be silently ignored. If not, the evaluated value from the default
         expression will be used as a replacement value.
       |
     - | ``["datetime", "2015-07-28T09:46:00.12345Z"]``
       |
       | Returns one datetime value: "~t2015-07-28T09:46:00.12345Z".
       |
       | ``["datetime", 1438076760123450000]``
       |
       | Returns one datetime value: "~t2015-07-28T09:46:00.12345Z". Note that
         integer values are treated as nanoseconds since "1970-01-01T00:00:00Z".
         Negative integer values are interpreted as nanoseconds before that.
       |
       | ``["datetime", ["list", ["now"], ["now"], "hello"]]``
       |
       | Returns a list of two datetime values which both are the current time.
         The "hello" string is ignored.
       |
       | ``["datetime", ["now"], "hello"]``
       |
       | Returns the current time as a datetime value, e.g.
         "~t2016-05-13T14:32:00.431Z". Note that this was created by the
         function argument.

.. _datetime_parse_dtl_function:

``datetime-parse``
------------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   TIMEZONE_NAME(string{0|1})
       |   FORMATSTRING(string{1})
       |   VALUES(value-expression{1})
       |
       | Translates all non-null input values to datetime values. The values must be strings
         matching the format string given. Any values that don't parse as datetime values will
         be silently ignored.
       |
       | The timezone name defaults to "UTC". The datetime string will be interpreted
         as being in this timezone. Click :ref:`here<supported_timezones>` to
         see the list of supported timezones.
       |
       |
       | The supported formatting tokens are:
       |
       |   %d - day of the month (01 to 31)
       |   %e - day of the month (1 to 31)
       |   %H - hour, using a 24-hour clock (00 to 23)
       |   %I - hour, using a 12-hour clock (01 to 12)
       |   %m - month (01 to 12)
       |   %M - minute
       |   %p - either am or pm according to the given time value
       |   %S - second
       |   %f - microsecond as a decimal number, zero-padded on the left
       |   %y - year without a century (range 00 to 99)
       |   %Y - year including the century
       |   %z - UTC offset in the form +HHMM, -HHMM, +HH:MM or -HH:MM. If present, this token must be the last token in the format string.
       |   %% - a literal % character
       |

       .. NOTE::

          When using ``%y``, then the two digits are converted
          according to the POSIX and ISO C standards; 00-68 are mapped
          to the years 2000-2068 and 69-99 are mapped to the years 1969-1999.
     - | ``["datetime-parse",``
       |   ``"%Y-%m-%dT%H:%M:%S.%fZ",``
       |   ``"2015-07-28T09:46:00.12345Z"]``
       |
       | Returns one datetime value: "~t2015-07-28T09:46:00.12345Z".
       |
       | ``["datetime-parse",``
       |   ``"%Y-%m-%dT%H:%M:%S%z",``
       |   ``"2015-07-28T09:46:00+0200"]``
       |
       | Returns one datetime value: "~t2015-07-28T07:46:00Z".
       |
       | ``["datetime-parse", "%d.%m.%Y", "28.07.2015"]``
       |
       | Returns one datetime value: "~t2015-07-28T00:00:00Z".
       |
       | ``["datetime-parse",``
       |   ``"%d.%m.%Y", ["list", "28.07.2015", "01.01.1970"]``
       |
       | Returns two datetime values: ["~t2015-07-28T00:00:00Z", "~t1970-01-01T00:00:00Z"]
       |
       | ``["datetime-parse", "Europe/Oslo"``
       |   ``"%Y-%m-%dT%H:%M:%S",``
       |   ``"2018-08-18T12:39:01"]``
       |
       | Returns one datetime value: "~t2018-08-08T10:39:01Z".

.. _datetime_format_dtl_function:

``datetime-format``
-------------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   TIMEZONE_NAME(string{0|1})
       |   FORMATSTRING(string{1})
       |   VALUES(value-expression{1})
       |
       | Translates all non-null input datetime values to strings. The strings will be formattet according to the format string.
         Any values that aren't datetime values will be silently ignored. Note that precision loss is possible since
         ``datetime`` objects internally have nanoseconds precision while the formatted strings will only support
         microseconds (using the seconds fraction token ``%f``).
       |
       | The timezone name defaults to "UTC". The datetime value will be translated to this timezone before it
         is formatted. Click :ref:`here<supported_timezones>` to see the list of supported timezones.

       .. NOTE::

          When using ``%y``, then the years are converted
          according to the POSIX and ISO C standards; the years 2000-2068 are mapped to 00-68
          and the years 1969-1999 are mapped to 69-99. For years outside of that range the
          last two digits are used.
     - | ``["datetime-format", "%Y-%m-%dT%H:%M:%SZ",``
       |   ``["datetime-parse", "%Y-%m-%d", "2015-07-28"]]``
       |
       | Returns one string: "2015-07-28T00:00:00Z".
       |
       | ``["datetime-format",``
       |   ``"%Y-%m-%d %H:%M:%S",``
       |   ``["datetime-parse",``
       |     ``"%Y-%m-%dT%H:%M:%S",``
       |     ``"2018-08-18T12:39:01"]]``
       |
       | Returns one string: "2018-08-18 12:39:01".
       |
       | ``["datetime-format", "Europe/Oslo",``
       |   ``"%Y-%m-%d %H:%M:%S",``
       |   ``["datetime-parse",``
       |     ``"%Y-%m-%dT%H:%M:%S",``
       |     ``"2018-08-18T12:39:01"]]``
       |
       | Returns one string: "2018-08-18 14:39:01".
       |
       | ``["datetime-format", "Europe/Oslo",``
       |   ``"%Y-%m-%d %H:%M:%S",``
       |   ``["datetime-parse", "Europe/Oslo",``
       |     ``"%Y-%m-%dT%H:%M:%S",``
       |     ``"2018-08-18T12:39:01"]]``
       |
       | Returns one string: "2018-08-18 12:39:01".
       |
       | See ``datetime-parse`` for the supported tokens in the format string.

.. _datetime_plus_dtl_function:

``datetime-plus``
-----------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   DATEPART(string{1})
       |   VALUE(integer{1})
       |   VALUES(value-expression{1})
       |
       | Adds a fixed ``VALUE`` number (positive or negative) of ``DATEPART`` values to the the input values,
       | producing new datetime objects. ``DATEPART`` can be one of the following values:
       |
       |   ``year``
       |   ``month``
       |   ``week``
       |   ``day``
       |   ``hour``
       |   ``minute``
       |   ``second``
       |   ``millisecond``
       |   ``microsecond``
       |   ``nanosecond``
       |

     - | ``["datetime-plus", "day", 1, ["datetime-parse",``
       |   ``"%Y-%m-%d", "2015-07-28"]]``
       |
       | Returns one datetime value: ``"~t2015-07-29T00:00:00Z"``.
       |
       | ``["datetime-plus", "hour", -1, ["datetime-parse",``
       |   ``"%Y-%m-%d", "2016-03-01"]]``
       |
       | Returns one datetime value: ``"~t2016-02-29T23:00:00Z"``.
       |
       | ``["datetime-plus", "year", 1,``
       |     ``["list",``
       |         ``["datetime-parse",``
       |           ``"%Y-%m-%d", "1971-01-01"],``
       |         ``["datetime-parse",``
       |           ``"%Y-%m-%d", "1950-06-01"]]``
       |
       | Returns two datetime values: ``["~t1972-01-01T00:00:00Z",``
       |                               ``"~t1951-06-01T00:00:00Z"]``.

.. _datetime_diff_dtl_function:

``datetime-diff``
-----------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   DATEPART(string{1})
       |   STARTDATE(value-expression{1})
       |   ENDDATE(value-expression{1})
       |
       | Computes the positive or negative number of ``DATEPART`` values between the end and start date input values
       | ``DATEPART`` can be one of the following values:
       |
       |   ``year``
       |   ``month``
       |   ``week``
       |   ``day``
       |   ``hour``
       |   ``minute``
       |   ``second``
       |   ``millisecond``
       |   ``microsecond``
       |   ``nanosecond``
       |
       | Note that the return values are rounded downwards to the nearest (absolute) integer value, i.e. +-11 months is
       | 0 years and +-8 days is +-1 week.

       |
     - | ``["datetime-diff", "day",``
       |   ``["datetime-parse", "%Y-%m-%d", "2015-07-28"],``
       |   ``["datetime-parse", "%Y-%m-%d", "2015-07-29"]]``
       |
       | Returns one integer value: -1
       |
       | ``["datetime-diff", "day",``
       |   ``["datetime-parse", "%Y-%m-%d", "2015-07-29"],``
       |   ``["datetime-parse", "%Y-%m-%d", "2015-07-28"]]``
       |
       | Returns one integer value: 1
       |
       | ``["datetime-diff", "year",``
       |   ``["datetime-parse", "%Y-%m-%d", "2015-03-02"],``
       |   ``["datetime-parse", "%Y-%m-%d", "2016-07-29"]]``
       |
       | Returns: -1
       |
       | ``["datetime-diff", "month",``
       |   ``["datetime-parse", "%Y-%m-%d", "2015-03-02"],``
       |   ``["datetime-parse", "%Y-%m-%d", "2016-07-29"]]``
       |
       | Returns: -16

.. _datetime_shift_dtl_function:

``datetime-shift``
------------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   FROM_TIMEZONE(string{1})
       |   TO_TIMEZONE(string{1})
       |   VALUES(value-expression{1})
       |
       | Shifts all the input datetime values from one timezone to another timezone. Any values that aren't datetime
         values will be silently ignored. Click :ref:`here<supported_timezones>` to see the list of supported timezones.
       | Internally, SESAM stores datetimes as UTC, and timezone converting is usually done automatically by the datasources.
         Sometimes, though, there is need to explicitly convert a timezone in a non-UTC timezone into some other timezone; An
         example is if you are reading from a CSV-file where one of the columns is a date-string with no explicit timezone information,
         but where you know that the dates are in some non-UTC timezone. In this case you could use the datetime-shift function
         to convert the dates from the CSV-file into correct UTC datetimes. |
     - | ``["datetime-shift", "Europe/Oslo", "UTC",``
       |     ``["datetime-parse",``
       |         ``"%Y/%m/%d %H:%M", "2015/07/28 09:46"]]``
       |
       | Returns one datetime value: ``"~t2015-07-28T07:46:00Z"``.
       | ``["datetime-shift", "UTC", "Europe/Oslo",``
       |     ``["datetime-parse",``
       |         ``"%Y/%m/%d %H:%M", "2015/07/28 09:46"]]``
       |
       | Returns one datetime value: ``"~t2015-07-28T11:46:00Z"``.
       |
       | ``["datetime-shift", "Europe/Oslo", "UTC",``
       |     ``["list",``
       |         ``["datetime-parse",``
       |           ``"%Y/%m/%d %H:%M", "2015/07/28 09:46"],``
       |         ``["datetime-parse",``
       |           ``"%Y/%m/%d %H:%M", "2015/07/28 04:46"]]``
       |
       | Returns two datetime values: ``["~t2015-07-28T07:46:00Z",``
       |                               ``"~t2015-07-28T02:46:00Z"]``.

.. _is_datetime_dtl_function:

``is-datetime``
---------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns true if value is a datetime value or
         if it is a list, that the first element in the list is a datetime value.
       |
     - | ``["is-datetime", ["now"]]``
       |
       | Returns true.
       |
       | ``["is-datetime",``
       |   ``["datetime", "2015-07-28T09:46:00.12345Z"]]``
       |
       | Returns true.
       |
       | ``["is-datetime", "2015-07-28T09:46:00.12345Z"]``
       |
       | Returns false.
       |
       | ``["is-datetime", ["list", "1", 2]]``
       |
       | Returns false.
