====================================
Business Nxt to SuperOffice Dataflow
====================================

Generated: 2024-09-14 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Nxt to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Nxt Address to SuperOffice Contact
-------------------------------------------
Every Business Nxt Address will be synchronized with a SuperOffice Contact.

Once a link between a Business Nxt Address and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Address and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Business Nxt Address Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - name
     - Name
     - "string"
   * - phone
     - Phones.Value
     - "string"


Business Nxt Company to SuperOffice Contact
-------------------------------------------
Every Business Nxt Company will be synchronized with a SuperOffice Contact.

Once a link between a Business Nxt Company and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Company and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Business Nxt Company Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - companyBusinessNo
     - OrgNr (Dependant on having  in Country.TwoLetterISOCountry)
     - "string"
   * - name
     - Name
     - "string"


Business Nxt Orderline to SuperOffice Quoteline
-----------------------------------------------
Every Business Nxt Orderline will be synchronized with a SuperOffice Quoteline.

Once a link between a Business Nxt Orderline and a SuperOffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Orderline and a SuperOffice Quoteline:

.. list-table::
   :header-rows: 1

   * - Business Nxt Orderline Property
     - SuperOffice Quoteline Property
     - SuperOffice Data Type
   * - orderNo
     - QuoteAlternativeId
     - "integer"


Business Nxt Product to SuperOffice Product
-------------------------------------------
Every Business Nxt Product will be synchronized with a SuperOffice Product.

Once a link between a Business Nxt Product and a SuperOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Product and a SuperOffice Product:

.. list-table::
   :header-rows: 1

   * - Business Nxt Product Property
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

