Cron expressions
================

Cron expressions encode a repeating interval of time. The format supported by the pump machinery of the Sesam node
is explained in more detail below. It follows mostly the explanation here: https://en.wikipedia.org/wiki/Cron

Syntax
------

A cron-expression is a string of 5 or 6 fields separated by space character. The string is parsed from left to right and
denotes in sequence:

.. list-table::
   :header-rows: 1
   :widths: 30, 20, 20, 20

   * - Field name
     - Mandatory?
     - Allowed values
     - Allowed special characters

   * - ``Minutes``
     - Yes
     - 0-59
     - \* , - /

   * - ``Hours``
     - Yes
     - 0-23
     - \* , - /

   * - ``Day of month``
     - Yes
     - 1-31
     - \* , - ? L W

   * - ``Month``
     - Yes
     - 1-12 or JAN-DEC
     - \* , - /

   * - ``Day of week``
     - Yes
     - 0-6 or SUN-SAT
     - \* , - ? L #/

   * - ``Year``
     - No
     - 1970–2099
     - \* , -

Examples
--------

.. list-table::
   :header-rows: 1
   :widths: 50, 50

   * - Expression
     - Meaning

   * - ``0 12 * * *``
     - Start at noon every day

   * - ``15 10 * * *``
     - Start at 10:15 every day

   * - ``15 10 * * * *``
     - Start at 10:15 every day

   * - ``15 10 * * * 2016``
     - Start at 10:15 every day during the year 2016

   * - ``* 14 * * *``
     - Start every minute starting at 14:00 and ending at 14:59, every day

   * - ``0/5 14 * * *``
     - Start every 5 minutes starting at 14:00 and ending at 14::55, every day

   * - ``0/5 14,18 * * *``
     - Start every 5 minutes starting at 14:00 and ending at 14:55, and also fire every 5 minutes starting at 18:00 and
       ending at 18:55, every day

   * - ``0-5 14 * * *``
     - Start every minute starting at 14:00 and ending at 14:05, every day

   * - ``10,44 14 * 3 WED``
     - Start at 14:10 and at 14:44 every wednesday in March

   * - ``15 10 * * MON-FRI``
     - Start at 10:15 every monday to friday

   * - ``15 10 15 * *``
     - Start at 10:15 on the 15th day of every month

   * - ``15 10 L * *``
     - Start at 10:15 on the last day of every month

   * - ``15 10 * * 6L``
     - Start at 10:15 on the last friday of every month

   * - ``15 10 * * 6L 2002-2005``
     - Start at 10:15 on every last friday of every month for the years 2002 to 2005

   * - ``15 10 * * 6#3``
     - Start at 10:15 on the third friday of every month

   * - ``0 12 1/5 * *``
     - Start at noon every 5 days every month, starting with the first day of the month

   * - ``11 11 11 11 *``
     - Start every 11th of november at 11:11
