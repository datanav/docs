===================================
BusinessNxt to SuperOffice Dataflow
===================================

Generated: 2024-09-11 08:37:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessNxt to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Visma Address to Superoffice Contact
------------------------------------
Every Visma Address will be synchronized with a Superoffice Contact.

Once a link between a Visma Address and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Address and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - Visma Address Property
     - Superoffice Contact Property
     - Superoffice Data Type
   * - name
     - Name
     - "string"
   * - phone
     - Phones.Value
     - "string"


Visma Company to Superoffice Contact
------------------------------------
Every Visma Company will be synchronized with a Superoffice Contact.

Once a link between a Visma Company and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Company and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - Visma Company Property
     - Superoffice Contact Property
     - Superoffice Data Type
   * - companyBusinessNo
     - OrgNr (Dependant on having  in Country.TwoLetterISOCountry)
     - "string"
   * - name
     - Name
     - "string"


BusinessNxt Orderline to SuperOffice Quoteline
----------------------------------------------
Every BusinessNxt Orderline will be synchronized with a SuperOffice Quoteline.

Once a link between a BusinessNxt Orderline and a SuperOffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Orderline and a SuperOffice Quoteline:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Orderline Property
     - SuperOffice Quoteline Property
     - SuperOffice Data Type
   * - orderNo
     - QuoteAlternativeId
     - "integer"


BusinessNxt Product to SuperOffice Product
------------------------------------------
Every BusinessNxt Product will be synchronized with a SuperOffice Product.

Once a link between a BusinessNxt Product and a SuperOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Product and a SuperOffice Product:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Product Property
     - SuperOffice Product Property
     - SuperOffice Data Type
   * - description
     - Description
     - "string"
   * - priceQuantity
     - UnitListPrice
     - N/A
   * - webPage
     - Url
     - "string"

