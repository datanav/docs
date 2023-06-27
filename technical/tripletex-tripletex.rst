===============================
Tripletex to Tripletex Dataflow
===============================

Generated: 2023-06-27 05:12:07

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Supplier to Tripletex Customer
----------------------------------------
Every Tripletex Supplier will be synchronized with a Tripletex Customer.

If a matching Tripletex Customer already exists, the Tripletex Supplier will be merged with the existing one.
If no matching Tripletex Customer is found, a new Tripletex Customer will be created.

A Tripletex Supplier will merge with a Tripletex Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - Tripletex Customer Property
   * - email
     - email
   * - email
     - invoiceEmail
   * - invoiceEmail
     - email
   * - email
     - overdueNoticeEmail
   * - overdueNoticeEmail
     - email
   * - invoiceEmail
     - invoiceEmail
   * - invoiceEmail
     - overdueNoticeEmail
   * - overdueNoticeEmail
     - invoiceEmail
   * - overdueNoticeEmail
     - overdueNoticeEmail

Once a link between a Tripletex Supplier and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - Tripletex Customer Property
     - Tripletex Data Type


Tripletex Customer to Tripletex Department
------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a Tripletex Department must be established.

A new Tripletex Department will be created from a Tripletex Customer if it is connected to a Tripletex Contact, Employee, or Department that is synchronized into Tripletex.

Once a link between a Tripletex Customer and a Tripletex Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Tripletex Department:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Tripletex Department Property
     - Tripletex Data Type


Tripletex Department to Tripletex Customer
------------------------------------------
Before any synchronization can take place, a link between a Tripletex Department and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a Tripletex Department if it is connected to a Tripletex Contact, or Employee that is synchronized into Tripletex.

Once a link between a Tripletex Department and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Tripletex Customer Property
     - Tripletex Data Type

