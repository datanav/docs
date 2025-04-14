.. _pricing:

===============================
Subscription Fee, payment terms
===============================

1. Subscription fee
===================

.. _pricing-developer:

Developer environment
---------------------
A developer environment has a fixed price and serves a single developer, or a CI test environment.
These do not have support for backup, VPN, or SLA and can not host test, staging or production environments. The development environment is cloud-only and restricted.
We strongly encourage following `test-driven development practices <https://en.wikipedia.org/wiki/Test-driven_development>`_
by using the :doc:`Sesam Client <hub/sesam-client>`.

.. list-table::
   :widths: 70 30
   :header-rows: 1

   * - Compute
     - Pr environment
   * - Fixed price Developer - 1 Engine < 20 GB Data
     - $75.00
   * - Fixed price Developer Pro - 2 Engines < 20 GB Data
     - $320.00

.. _pricing-production:

Production and test environment
-------------------------------

.. list-table::
   :widths: 70 30
   :header-rows: 1

   * - Compute [#]_
     - Pr environment
   * - Single compute - 4 Engines < 350 GB Data
     - $1,300.00
   * - Multi compute - 16 Engines < 1 TB Data
     - $4,200.00

.. list-table::
   :widths: 70 30
   :header-rows: 1

   * - Data [#]_
     - Pr GB
   * - Storage
     - $22.00
   * - VPN
     - $3.00

.. list-table::
   :widths: 70 30
   :header-rows: 1

   * - Additional features
     - 
   * - Pipe notifications
     - $25.00
   * - Metrics and monitoring
     - Free
   * - Integrated search and property lineage
     - Free

.. list-table::
   :widths: 70 30
   :header-rows: 1

   * - SLA - Response time [#]_
     - Pr GB
   * - Standard - 8h
     - $22.00
   * - Enterprise - 1h
     - $42.00
   * - Premium 0,5h x 24/7 [#]_
     - 125.00

.. [#] Geo-replicated backup is included in cloud environments.
.. [#] 1-year fixed price option available. 50% data price reduction for the fixed data amount, with 100% price increase for data exceeding the fixed data amount. Number of computes is determined by the maximum of fixed data amount and actual data amount.
.. [#] SLA is billed for minimum 50GB data and a maximum of 300GB.
.. [#] Contact support for Premium SLA.




3. Invoicing
============

From the start of the Services, the Customer will be invoiced as agreed for the Service.
The invoice shall be specified in a manner that allows the Customer to
control the individual price items, including any incurred standardized
penalties. SESAM offers electronic invoicing in EHF.

4. Due date
===========

Invoices are due after 30 calendar days.

4. Price adjustment
===================

Subscription Fee may be adjusted upon at least 30 days notice.

If, after the signature of the Agreement, changes in public taxes,
charges or other duties or other changes in public administrative
practice affects the vendor's costs connected to the Service, the
subscription fee shall be adjusted correspondingly without prior notice.



5. Legacy prices
================

The following items are no longer available for new subscriptions:

.. list-table::
  :widths: 70 30
  :header-rows: 1

  * - Compute
    - Pr environment
  * - Large compute - 8 Engines < 750 GB Data
    - $2,000.00

.. list-table::
  :widths: 70 30
  :header-rows: 1

  * - Pipe monitoring
    - Pr pipe
  * - Enterprise - Notifications
    - $25.00

.. list-table::
  :widths: 70 30
  :header-rows: 1

  * - :doc:`GDPR Data Access Portal <hub/gdpr-platform>`
    - Pr GB
  * - Basic < 1 request per second
    - $50.00
  * - Standard < 5 requests per second
    - $100.00
  * - Enterprise < 10 requests per second
    - $200.00
