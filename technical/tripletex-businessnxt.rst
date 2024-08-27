======================
Tripletex to  Dataflow
======================

Generated: 2024-08-27 12:02:26

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer to  Address
------------------------------
Every Tripletex Customer will be synchronized with a  Address.

Once a link between a Tripletex Customer and a  Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a  Address:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     -  Address Property
     -  Data Type
   * - name
     - name
     - "string"
   * - phoneNumber
     - phone
     - "string"
   * - phoneNumberMobile
     - mobilePhone
     - "string"


Tripletex Customer to  Company
------------------------------
Every Tripletex Customer will be synchronized with a  Company.

Once a link between a Tripletex Customer and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a  Company:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     -  Company Property
     -  Data Type
   * - customerNumber
     - companyBusinessNo (Dependant on having wd:Q852835 in countryIsoCode)
     - "string"
   * - name
     - name
     - "string"
   * - organizationNumber
     - companyBusinessNo (Dependant on having NO in countryIsoCode)
     - "string"


Tripletex Department to  Address
--------------------------------
Every Tripletex Department will be synchronized with a  Address.

Once a link between a Tripletex Department and a  Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a  Address:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     -  Address Property
     -  Data Type
   * - name
     - name
     - "string"


Tripletex Department to  Company
--------------------------------
Every Tripletex Department will be synchronized with a  Company.

Once a link between a Tripletex Department and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a  Company:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     -  Company Property
     -  Data Type
   * - departmentNumber
     - companyBusinessNo (Dependant on having wd:Q2366457 in countryIsoCode)
     - "string"
   * - name
     - name
     - "string"


Tripletex Country to  Country
-----------------------------
Every Tripletex Country will be synchronized with a  Country.

Once a link between a Tripletex Country and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Country and a  Country:

.. list-table::
   :header-rows: 1

   * - Tripletex Country Property
     -  Country Property
     -  Data Type
   * - isoAlpha2Code
     - isoCode
     - "string"
   * - name
     - name
     - "string"


Tripletex Currency to  Currency
-------------------------------
Every Tripletex Currency will be synchronized with a  Currency.

Once a link between a Tripletex Currency and a  Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Currency and a  Currency:

.. list-table::
   :header-rows: 1

   * - Tripletex Currency Property
     -  Currency Property
     -  Data Type
   * - displayName
     - name
     - "string"


Tripletex Order to  Order
-------------------------
Every Tripletex Order will be synchronized with a  Order.

Once a link between a Tripletex Order and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a  Order:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     -  Order Property
     -  Data Type
   * - deliveryDate
     - dueDate
     - "string"
   * - orderDate
     - orderDate
     - "string"


Tripletex Product to  Product
-----------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a  Product.

Once a link between a Tripletex Product and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a  Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     -  Product Property
     -  Data Type
   * - description
     - description
     - "string"
   * - priceExcludingVatCurrency
     - priceQuantity
     - "string"
   * - stockOfGoods
     - quantityPerUnit
     - "string"


Tripletex Productgroup to  Productcategory
------------------------------------------
Every Tripletex Productgroup will be synchronized with a  Productcategory.

Once a link between a Tripletex Productgroup and a  Productcategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productgroup and a  Productcategory:

.. list-table::
   :header-rows: 1

   * - Tripletex Productgroup Property
     -  Productcategory Property
     -  Data Type
   * - name
     - text
     - "string"

