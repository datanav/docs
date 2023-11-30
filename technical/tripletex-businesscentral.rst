======================
Tripletex to  Dataflow
======================

Generated: 2023-11-30 13:24:08

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer to  Company
------------------------------
Every Tripletex Customer will be synchronized with a  Company.

Once a link between a Tripletex Customer and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a  Company:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     -  Company Property
     -  Data Type


Tripletex Department to  Company
--------------------------------
Every Tripletex Department will be synchronized with a  Company.

Once a link between a Tripletex Department and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a  Company:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     -  Company Property
     -  Data Type


Tripletex Order to  Salesorders
-------------------------------
Every Tripletex Order will be synchronized with a  Salesorders.

Once a link between a Tripletex Order and a  Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a  Salesorders:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     -  Salesorders Property
     -  Data Type
   * - contact.id
     - customerId
     - "string"
   * - customer.id
     - customerId
     - "string"

