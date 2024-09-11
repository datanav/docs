====================================
SuperOffice to Business Nxt Dataflow
====================================

Generated: 2024-09-11 12:17:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Business Nxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to Business Nxt Address
-------------------------------------------
Every SuperOffice Contact will be synchronized with a Business Nxt Address.

Once a link between a SuperOffice Contact and a Business Nxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Business Nxt Address:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Business Nxt Address Property
     - Business Nxt Data Type
   * - Name
     - name
     - "string"
   * - Phones.Value
     - phone
     - "string"


SuperOffice Quotealternative to Business Nxt Order
--------------------------------------------------
Every SuperOffice Quotealternative will be synchronized with a Business Nxt Order.

Once a link between a SuperOffice Quotealternative and a Business Nxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a Business Nxt Order:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - Business Nxt Order Property
     - Business Nxt Data Type
   * - DiscountPercent
     - totalDiscountAmountInCurrency
     - "string"
   * - VAT
     - taxCode
     - "string"


SuperOffice Quoteline to Business Nxt Order
-------------------------------------------
Every SuperOffice Quoteline will be synchronized with a Business Nxt Order.

Once a link between a SuperOffice Quoteline and a Business Nxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a Business Nxt Order:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - Business Nxt Order Property
     - Business Nxt Data Type


SuperOffice Sale to Business Nxt Order
--------------------------------------
Every SuperOffice Sale will be synchronized with a Business Nxt Order.

Once a link between a SuperOffice Sale and a Business Nxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale and a Business Nxt Order:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     - Business Nxt Order Property
     - Business Nxt Data Type
   * - Heading
     - name
     - "string"
   * - Saledate
     - dueDate
     - "string"
   * - Saledate
     - orderDate
     - "string"


SuperOffice Listcountryitems to Business Nxt Country
----------------------------------------------------
Every SuperOffice Listcountryitems will be synchronized with a Business Nxt Country.

Once a link between a SuperOffice Listcountryitems and a Business Nxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcountryitems and a Business Nxt Country:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcountryitems Property
     - Business Nxt Country Property
     - Business Nxt Data Type
   * - Name
     - name
     - "string"
   * - TwoLetterISOCountry
     - isoCode
     - "string"


SuperOffice Listcurrencyitems to Business Nxt Currency
------------------------------------------------------
Every SuperOffice Listcurrencyitems will be synchronized with a Business Nxt Currency.

Once a link between a SuperOffice Listcurrencyitems and a Business Nxt Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcurrencyitems and a Business Nxt Currency:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcurrencyitems Property
     - Business Nxt Currency Property
     - Business Nxt Data Type
   * - Name
     - isoCode
     - "string"


SuperOffice Listproductcategoryitems to Business Nxt Productcategory
--------------------------------------------------------------------
Every SuperOffice Listproductcategoryitems will be synchronized with a Business Nxt Productcategory.

Once a link between a SuperOffice Listproductcategoryitems and a Business Nxt Productcategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listproductcategoryitems and a Business Nxt Productcategory:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listproductcategoryitems Property
     - Business Nxt Productcategory Property
     - Business Nxt Data Type
   * - Name
     - text
     - "string"
   * - Tooltip
     - description
     - "string"


SuperOffice Product to Business Nxt Product
-------------------------------------------
Every SuperOffice Product will be synchronized with a Business Nxt Product.

Once a link between a SuperOffice Product and a Business Nxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a Business Nxt Product:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Business Nxt Product Property
     - Business Nxt Data Type
   * - Description
     - description
     - "string"
   * - UnitListPrice
     - priceQuantity
     - "string"
   * - Url
     - webPage
     - "string"


SuperOffice Quoteline to Business Nxt Orderline
-----------------------------------------------
Every SuperOffice Quoteline will be synchronized with a Business Nxt Orderline.

Once a link between a SuperOffice Quoteline and a Business Nxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a Business Nxt Orderline:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - Business Nxt Orderline Property
     - Business Nxt Data Type
   * - QuoteAlternativeId
     - orderNo
     - "string"

