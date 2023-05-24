====================================
Wave Financial to Tripletex Dataflow
====================================

Generated: 2023-05-24 13:06:33

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to Tripletex Customer
-----------------------------------
Every Wave Customer will be synchronized with a Tripletex Customer.

Once a link between a Wave Customer and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - name
     - name
     - "string"
   * - phone
     - phoneNumber
     - "string"


Wave Invoice to Tripletex Customer
----------------------------------
Every Wave Invoice will be synchronized with a Tripletex Customer.

Once a link between a Wave Invoice and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Tripletex Customer Property
     - Tripletex Data Type

