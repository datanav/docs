===================================
SuperOffice to Businessnxt Dataflow
===================================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Businessnxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to Businessnxt Address
------------------------------------------
Every SuperOffice Contact will be synchronized with a Businessnxt Address.

Once a link between a SuperOffice Contact and a Businessnxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Businessnxt Address:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Businessnxt Address Property
     - Businessnxt Data Type
   * - Name
     - name
     - "string"
   * - Phones.Value
     - phone
     - "string"


SuperOffice Quotealternative to Businessnxt Order
-------------------------------------------------
Every SuperOffice Quotealternative will be synchronized with a Businessnxt Order.

Once a link between a SuperOffice Quotealternative and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - Businessnxt Order Property
     - Businessnxt Data Type
   * - DiscountPercent
     - totalDiscountAmountInCurrency
     - "string"
   * - VAT
     - taxCode
     - "string"


SuperOffice Quoteline to Businessnxt Order
------------------------------------------
Every SuperOffice Quoteline will be synchronized with a Businessnxt Order.

Once a link between a SuperOffice Quoteline and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - Businessnxt Order Property
     - Businessnxt Data Type


SuperOffice Sale to Businessnxt Order
-------------------------------------
Every SuperOffice Sale will be synchronized with a Businessnxt Order.

Once a link between a SuperOffice Sale and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     - Businessnxt Order Property
     - Businessnxt Data Type
   * - Heading
     - name
     - "string"
   * - Saledate
     - dueDate
     - "string"
   * - Saledate
     - orderDate
     - "string"


SuperOffice Listcountryitems to Businessnxt Country
---------------------------------------------------
Every SuperOffice Listcountryitems will be synchronized with a Businessnxt Country.

Once a link between a SuperOffice Listcountryitems and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcountryitems and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcountryitems Property
     - Businessnxt Country Property
     - Businessnxt Data Type
   * - Name
     - name
     - "string"
   * - TwoLetterISOCountry
     - isoCode
     - "string"


SuperOffice Listcurrencyitems to Businessnxt Currency
-----------------------------------------------------
Every SuperOffice Listcurrencyitems will be synchronized with a Businessnxt Currency.

Once a link between a SuperOffice Listcurrencyitems and a Businessnxt Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcurrencyitems and a Businessnxt Currency:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcurrencyitems Property
     - Businessnxt Currency Property
     - Businessnxt Data Type
   * - Name
     - isoCode
     - "string"


SuperOffice Listproductcategoryitems to Businessnxt Productcategory
-------------------------------------------------------------------
Every SuperOffice Listproductcategoryitems will be synchronized with a Businessnxt Productcategory.

Once a link between a SuperOffice Listproductcategoryitems and a Businessnxt Productcategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listproductcategoryitems and a Businessnxt Productcategory:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listproductcategoryitems Property
     - Businessnxt Productcategory Property
     - Businessnxt Data Type
   * - Name
     - text
     - "string"
   * - Tooltip
     - description
     - "string"


SuperOffice Product to Businessnxt Product
------------------------------------------
Every SuperOffice Product will be synchronized with a Businessnxt Product.

Once a link between a SuperOffice Product and a Businessnxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a Businessnxt Product:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Businessnxt Product Property
     - Businessnxt Data Type
   * - Description
     - description
     - "string"
   * - UnitListPrice
     - priceQuantity
     - "string"
   * - Url
     - webPage
     - "string"


SuperOffice Quoteline to Businessnxt Orderline
----------------------------------------------
Every SuperOffice Quoteline will be synchronized with a Businessnxt Orderline.

Once a link between a SuperOffice Quoteline and a Businessnxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a Businessnxt Orderline:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - Businessnxt Orderline Property
     - Businessnxt Data Type
   * - QuoteAlternativeId
     - orderNo
     - "string"

