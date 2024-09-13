============================
Keap to SuperOffice Dataflow
============================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Keap to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Keap Companies to SuperOffice Contact
-------------------------------------
Every Keap Companies will be synchronized with a SuperOffice Contact.

Once a link between a Keap Companies and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Companies and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Keap Companies Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - address.locality
     - Address.Postal.City
     - "string"
   * - address.locality
     - Address.Street.City
     - "string"
   * - address.zip_code
     - Address.Postal.Zipcode
     - "string"
   * - address.zip_code
     - Address.Street.Zipcode
     - "string"
   * - company_name
     - Name
     - "string"
   * - id
     - ContactId
     - "integer"


Keap Contacts to SuperOffice Person
-----------------------------------
Every Keap Contacts will be synchronized with a SuperOffice Person.

Once a link between a Keap Contacts and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Contacts and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Keap Contacts Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - birthday
     - BirthDate
     - N/A


Keap Opportunity to SuperOffice Sale
------------------------------------
Every Keap Opportunity will be synchronized with a SuperOffice Sale.

Once a link between a Keap Opportunity and a SuperOffice Sale is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Opportunity and a SuperOffice Sale:

.. list-table::
   :header-rows: 1

   * - Keap Opportunity Property
     - SuperOffice Sale Property
     - SuperOffice Data Type
   * - opportunity_title
     - Heading
     - "string"


Keap Product to SuperOffice Product
-----------------------------------
Every Keap Product will be synchronized with a SuperOffice Product.

Once a link between a Keap Product and a SuperOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Product and a SuperOffice Product:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     - SuperOffice Product Property
     - SuperOffice Data Type
   * - product_desc
     - Description
     - "string"
   * - product_name
     - Name
     - "string"
   * - product_price
     - UnitListPrice
     - N/A

