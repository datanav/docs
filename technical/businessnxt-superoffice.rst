===================================
BusinessNxt to SuperOffice Dataflow
===================================

Generated: 2024-09-11 09:30:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessNxt to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

BusinessNxt Address to SuperOffice Contact
------------------------------------------
Every BusinessNxt Address will be synchronized with a SuperOffice Contact.

Once a link between a BusinessNxt Address and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Address and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Address Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - name
     - Name
     - "string"
   * - phone
     - Phones.Value
     - "string"


BusinessNxt Company to SuperOffice Contact
------------------------------------------
Every BusinessNxt Company will be synchronized with a SuperOffice Contact.

Once a link between a BusinessNxt Company and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Company and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Company Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
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

