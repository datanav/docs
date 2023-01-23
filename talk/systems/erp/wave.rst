.. _talk_wave:

Wave
====
Wave provides financial software and services for small businesses, with services include direct bank data imports, invoicing and expense tracking, customizable chart of accounts, and journal transactions.

https://waveapps.com

Supported types
---------------
The following types are currently supported.

.. list-table::
   :header-rows: 1

   * - Wave type
     - Maps to
     - Read
     - Write

   * - Customer
     - :ref:`Organisation <organisation>`
     - Yes
     - Yes

   * - Customer (embedded primary contact)
     - :ref:`Person <person>`
     - Yes
     - Yes

Known issues
------------

[IS-13377] We only support 200 entities for each entity type due to pagination issues.

[IS-13386] Only support users with a single business.

[IS-13388] Updates might get lost when updating customers