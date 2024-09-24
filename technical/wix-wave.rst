========================
Wix.com to Wave Dataflow
========================

Generated: 2024-09-24 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to Wave Customer
---------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a Wave Customer must be established.

A new Wave Customer will be created from a Wix.com Contacts if it is connected to a Wix.com Wix-orders that is synchronized into Wave.

A Wix.com Contacts will merge with a Wave Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Wave Customer Property
   * - primaryInfo.email
     - email

Once a link between a Wix.com Contacts and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Wave Customer Property
     - Wave Data Type
   * - info.name.first
     - firstName
     - "string"
   * - info.name.last
     - lastName
     - N/A
   * - primaryInfo.email
     - email
     - "string"
   * - primaryInfo.phone
     - phone
     - "string"


Wix.com Members to Wave Customer
--------------------------------
Before any synchronization can take place, a link between a Wix.com Members and a Wave Customer must be established.

A Wix.com Members will merge with a Wave Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - Wave Customer Property
   * - loginEmail
     - email

Once a link between a Wix.com Members and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - Wave Customer Property
     - Wave Data Type
   * - loginEmail
     - email
     - "string"


Wix.com Orders to Wave Invoice
------------------------------
Every Wix.com Orders will be synchronized with a Wave Invoice.

Once a link between a Wix.com Orders and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - Wave Invoice Property
     - Wave Data Type


Wix.com Products to Wave Product
--------------------------------
Every Wix.com Products will be synchronized with a Wave Product.

Once a link between a Wix.com Products and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a Wave Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - Wave Product Property
     - Wave Data Type
   * - name
     - name
     - "string"
   * - priceData.price
     - unitPrice
     - "string"

