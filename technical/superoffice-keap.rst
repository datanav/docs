============================
SuperOffice to Keap Dataflow
============================

Generated: 2024-09-03 08:57:35

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to  Companies
---------------------------------
Every SuperOffice Contact will be synchronized with a  Companies.

Once a link between a SuperOffice Contact and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a  Companies:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     -  Companies Property
     -  Data Type
   * - Address.Postal.City
     - address.locality
     - "string"
   * - Address.Postal.Zipcode
     - address.zip_code
     - "string"
   * - Address.Street.City
     - address.locality
     - "string"
   * - Address.Street.Zipcode
     - address.zip_code
     - "string"
   * - ContactId
     - id
     - "string"
   * - Name
     - company_name
     - "string"


SuperOffice Person to  Contacts
-------------------------------
Every SuperOffice Person will be synchronized with a  Contacts.

Once a link between a SuperOffice Person and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a  Contacts:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     -  Contacts Property
     -  Data Type
   * - BirthDate
     - birthday
     - "string"


SuperOffice Product to Keap Product
-----------------------------------
Every SuperOffice Product will be synchronized with a Keap Product.

Once a link between a SuperOffice Product and a Keap Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a Keap Product:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Keap Product Property
     - Keap Data Type
   * - Description
     - product_desc
     - "string"
   * - Name
     - product_name
     - "string"
   * - UnitListPrice
     - product_price
     - "string"


SuperOffice Sale to Keap Opportunity
------------------------------------
Every SuperOffice Sale will be synchronized with a Keap Opportunity.

Once a link between a SuperOffice Sale and a Keap Opportunity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale and a Keap Opportunity:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     - Keap Opportunity Property
     - Keap Data Type
   * - Heading
     - opportunity_title
     - "string"

