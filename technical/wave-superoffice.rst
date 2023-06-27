======================================
Wave Financial to SuperOffice Dataflow
======================================

Generated: 2023-06-27 11:46:54

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to SuperOffice Contact
------------------------------------
Every Wave Customer will be synchronized with a SuperOffice Contact.

Once a link between a Wave Customer and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - name
     - Name
     - "string"
   * - phone
     - Phones.Value
     - "string"
   * - website
     - Domains
     - "list"


Wave Vendor to SuperOffice Contact
----------------------------------
Every Wave Vendor will be synchronized with a SuperOffice Contact.

Once a link between a Wave Vendor and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - name
     - Name
     - "string"
   * - phone
     - Phones.Value
     - "string"
   * - website
     - Domains
     - "list"


Wave Product to SuperOffice Product
-----------------------------------
Every Wave Product will be synchronized with a SuperOffice Product.

Once a link between a Wave Product and a SuperOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a SuperOffice Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - SuperOffice Product Property
     - SuperOffice Data Type
   * - description
     - Description
     - "string"
   * - name
     - Name
     - "string"
   * - unitPrice
     - UnitListPrice
     - "decimal"

