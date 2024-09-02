========================
SuperOffice to  Dataflow
========================

Generated: 2024-09-02 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to  Address
-------------------------------
Every SuperOffice Contact will be synchronized with a  Address.

Once a link between a SuperOffice Contact and a  Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a  Address:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     -  Address Property
     -  Data Type
   * - Name
     - name
     - "string"
   * - Phones.Value
     - phone
     - "string"


SuperOffice Quotealternative to  Order
--------------------------------------
Every SuperOffice Quotealternative will be synchronized with a  Order.

Once a link between a SuperOffice Quotealternative and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a  Order:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     -  Order Property
     -  Data Type
   * - DiscountPercent
     - totalDiscountAmountInCurrency
     - "string"
   * - VAT
     - taxCode
     - "string"


SuperOffice Quoteline to  Order
-------------------------------
Every SuperOffice Quoteline will be synchronized with a  Order.

Once a link between a SuperOffice Quoteline and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a  Order:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     -  Order Property
     -  Data Type


SuperOffice Sale to  Order
--------------------------
Every SuperOffice Sale will be synchronized with a  Order.

Once a link between a SuperOffice Sale and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale and a  Order:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     -  Order Property
     -  Data Type
   * - Heading
     - name
     - "string"
   * - Saledate
     - dueDate
     - "string"
   * - Saledate
     - orderDate
     - "string"


SuperOffice Listcountryitems to  Country
----------------------------------------
Every SuperOffice Listcountryitems will be synchronized with a  Country.

Once a link between a SuperOffice Listcountryitems and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcountryitems and a  Country:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcountryitems Property
     -  Country Property
     -  Data Type
   * - Name
     - name
     - "string"
   * - TwoLetterISOCountry
     - isoCode
     - "string"


SuperOffice Listcurrencyitems to  Currency
------------------------------------------
Every SuperOffice Listcurrencyitems will be synchronized with a  Currency.

Once a link between a SuperOffice Listcurrencyitems and a  Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcurrencyitems and a  Currency:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcurrencyitems Property
     -  Currency Property
     -  Data Type
   * - Name
     - isoCode
     - "string"


SuperOffice Listproductcategoryitems to  Productcategory
--------------------------------------------------------
Every SuperOffice Listproductcategoryitems will be synchronized with a  Productcategory.

Once a link between a SuperOffice Listproductcategoryitems and a  Productcategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listproductcategoryitems and a  Productcategory:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listproductcategoryitems Property
     -  Productcategory Property
     -  Data Type
   * - Name
     - text
     - "string"
   * - Tooltip
     - description
     - "string"


SuperOffice Product to  Product
-------------------------------
Every SuperOffice Product will be synchronized with a  Product.

Once a link between a SuperOffice Product and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a  Product:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     -  Product Property
     -  Data Type
   * - Description
     - description
     - "string"
   * - UnitListPrice
     - priceQuantity
     - "string"
   * - Url
     - webPage
     - "string"


SuperOffice Quoteline to  Orderline
-----------------------------------
Every SuperOffice Quoteline will be synchronized with a  Orderline.

Once a link between a SuperOffice Quoteline and a  Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a  Orderline:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     -  Orderline Property
     -  Data Type
   * - QuoteAlternativeId
     - orderNo
     - "string"

