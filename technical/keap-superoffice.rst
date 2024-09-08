============================
Keap to Superoffice Dataflow
============================

Generated: 2024-09-08 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Keap to Superoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Keap Companies to Superoffice Contact
-------------------------------------
Every Keap Companies will be synchronized with a Superoffice Contact.

Once a link between a Keap Companies and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Companies and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - Keap Companies Property
     - Superoffice Contact Property
     - Superoffice Data Type
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


Keap Contacts to Superoffice Person
-----------------------------------
Every Keap Contacts will be synchronized with a Superoffice Person.

Once a link between a Keap Contacts and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Contacts and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - Keap Contacts Property
     - Superoffice Person Property
     - Superoffice Data Type
   * - birthday
     - BirthDate
     - N/A


Keap Opportunity to Superoffice Sale
------------------------------------
Every Keap Opportunity will be synchronized with a Superoffice Sale.

Once a link between a Keap Opportunity and a Superoffice Sale is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Opportunity and a Superoffice Sale:

.. list-table::
   :header-rows: 1

   * - Keap Opportunity Property
     - Superoffice Sale Property
     - Superoffice Data Type
   * - opportunity_title
     - Heading
     - "string"


Keap Product to Superoffice Product
-----------------------------------
Every Keap Product will be synchronized with a Superoffice Product.

Once a link between a Keap Product and a Superoffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Product and a Superoffice Product:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     - Superoffice Product Property
     - Superoffice Data Type
   * - product_desc
     - Description
     - "string"
   * - product_name
     - Name
     - "string"
   * - product_price
     - UnitListPrice
     - N/A

