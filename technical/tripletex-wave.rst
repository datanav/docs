==========================
Tripletex to Wave Dataflow
==========================

Generated: 2023-06-23 11:19:51

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer to Wave Customer
-----------------------------------
Every Tripletex Customer will be synchronized with a Wave Customer.

Once a link between a Tripletex Customer and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Wave Customer Property
     - Wave Data Type


Tripletex Order to Wave Invoice
-------------------------------
Every Tripletex Order will be synchronized with a Wave Invoice.

Once a link between a Tripletex Order and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - Wave Invoice Property
     - Wave Data Type


Tripletex Product to Wave Product
---------------------------------
Before any synchronization can take place, a link between a Tripletex Product and a Wave Product must be established.

A new Wave Product will be created from a Tripletex Product if it is connected to a Tripletex Order that is synchronized into Wave.

Once a link between a Tripletex Product and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a Wave Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Wave Product Property
     - Wave Data Type


Tripletex Supplier to Wave Customer
-----------------------------------
Every Tripletex Supplier will be synchronized with a Wave Customer.

Once a link between a Tripletex Supplier and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - Wave Customer Property
     - Wave Data Type
   * - name
     - name
     - "string"
   * - phoneNumber
     - phone
     - "string"

