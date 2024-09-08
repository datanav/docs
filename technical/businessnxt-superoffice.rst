===================================
Businessnxt to Superoffice Dataflow
===================================

Generated: 2024-09-08 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businessnxt to Superoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businessnxt Address to Superoffice Contact
------------------------------------------
Every Businessnxt Address will be synchronized with a Superoffice Contact.

Once a link between a Businessnxt Address and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Address and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - Businessnxt Address Property
     - Superoffice Contact Property
     - Superoffice Data Type
   * - name
     - Name
     - "string"
   * - phone
     - Phones.Value
     - "string"


Businessnxt Company to Superoffice Contact
------------------------------------------
Every Businessnxt Company will be synchronized with a Superoffice Contact.

Once a link between a Businessnxt Company and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Company and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - Businessnxt Company Property
     - Superoffice Contact Property
     - Superoffice Data Type
   * - companyBusinessNo
     - OrgNr (Dependant on having  in Country.TwoLetterISOCountry)
     - "string"
   * - name
     - Name
     - "string"


Businessnxt Orderline to Superoffice Quoteline
----------------------------------------------
Every Businessnxt Orderline will be synchronized with a Superoffice Quoteline.

Once a link between a Businessnxt Orderline and a Superoffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Orderline and a Superoffice Quoteline:

.. list-table::
   :header-rows: 1

   * - Businessnxt Orderline Property
     - Superoffice Quoteline Property
     - Superoffice Data Type
   * - orderNo
     - QuoteAlternativeId
     - "integer"


Businessnxt Product to Superoffice Product
------------------------------------------
Every Businessnxt Product will be synchronized with a Superoffice Product.

Once a link between a Businessnxt Product and a Superoffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Product and a Superoffice Product:

.. list-table::
   :header-rows: 1

   * - Businessnxt Product Property
     - Superoffice Product Property
     - Superoffice Data Type
   * - description
     - Description
     - "string"
   * - priceQuantity
     - UnitListPrice
     - N/A
   * - webPage
     - Url
     - "string"

