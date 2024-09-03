=============================
Exact to Businessnxt Dataflow
=============================

Generated: 2024-09-03 08:55:46

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact to Businessnxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Accounts to  Address
--------------------------
Every Exact Accounts will be synchronized with a  Address.

Once a link between a Exact Accounts and a  Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Accounts and a  Address:

.. list-table::
   :header-rows: 1

   * - Exact Accounts Property
     -  Address Property
     -  Data Type
   * - City
     - postalArea
     - "string"
   * - CompanySize
     - noOfEmployees
     - "string"
   * - Country
     - countryNo
     - "string"
   * - ID
     - addressNo
     - "string"
   * - Name
     - name
     - "string"
   * - Postcode
     - postCode
     - "string"


Exact Currencies to  Country
----------------------------
Every Exact Currencies will be synchronized with a  Country.

Once a link between a Exact Currencies and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Currencies and a  Country:

.. list-table::
   :header-rows: 1

   * - Exact Currencies Property
     -  Country Property
     -  Data Type
   * - Description
     - name
     - "string"


Exact Departments to  Address
-----------------------------
Every Exact Departments will be synchronized with a  Address.

Once a link between a Exact Departments and a  Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Departments and a  Address:

.. list-table::
   :header-rows: 1

   * - Exact Departments Property
     -  Address Property
     -  Data Type


Exact Divisions to  Address
---------------------------
Every Exact Divisions will be synchronized with a  Address.

Once a link between a Exact Divisions and a  Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Divisions and a  Address:

.. list-table::
   :header-rows: 1

   * - Exact Divisions Property
     -  Address Property
     -  Data Type


Exact Quotations to  Order
--------------------------
Every Exact Quotations will be synchronized with a  Order.

Once a link between a Exact Quotations and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Quotations and a  Order:

.. list-table::
   :header-rows: 1

   * - Exact Quotations Property
     -  Order Property
     -  Data Type


Exact Salesinvoices to  Order
-----------------------------
Every Exact Salesinvoices will be synchronized with a  Order.

Once a link between a Exact Salesinvoices and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesinvoices and a  Order:

.. list-table::
   :header-rows: 1

   * - Exact Salesinvoices Property
     -  Order Property
     -  Data Type


Exact Salesorderlines to  Order
-------------------------------
Every Exact Salesorderlines will be synchronized with a  Order.

Once a link between a Exact Salesorderlines and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorderlines and a  Order:

.. list-table::
   :header-rows: 1

   * - Exact Salesorderlines Property
     -  Order Property
     -  Data Type


Exact Units to  Country
-----------------------
Every Exact Units will be synchronized with a  Country.

Once a link between a Exact Units and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Units and a  Country:

.. list-table::
   :header-rows: 1

   * - Exact Units Property
     -  Country Property
     -  Data Type
   * - Description
     - name
     - "string"


Exact Vatcodes to  Country
--------------------------
Every Exact Vatcodes will be synchronized with a  Country.

Once a link between a Exact Vatcodes and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Vatcodes and a  Country:

.. list-table::
   :header-rows: 1

   * - Exact Vatcodes Property
     -  Country Property
     -  Data Type


Exact Addresses to  Country
---------------------------
Every Exact Addresses will be synchronized with a  Country.

Once a link between a Exact Addresses and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Addresses and a  Country:

.. list-table::
   :header-rows: 1

   * - Exact Addresses Property
     -  Country Property
     -  Data Type
   * - CountryName
     - name
     - "string"


Exact Currencies to  Currency
-----------------------------
Every Exact Currencies will be synchronized with a  Currency.

Once a link between a Exact Currencies and a  Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Currencies and a  Currency:

.. list-table::
   :header-rows: 1

   * - Exact Currencies Property
     -  Currency Property
     -  Data Type
   * - Description
     - name
     - "string"


Exact Items to  Product
-----------------------
Every Exact Items will be synchronized with a  Product.

Once a link between a Exact Items and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Items and a  Product:

.. list-table::
   :header-rows: 1

   * - Exact Items Property
     -  Product Property
     -  Data Type


Exact Salesorderlines to  Orderline
-----------------------------------
Every Exact Salesorderlines will be synchronized with a  Orderline.

Once a link between a Exact Salesorderlines and a  Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorderlines and a  Orderline:

.. list-table::
   :header-rows: 1

   * - Exact Salesorderlines Property
     -  Orderline Property
     -  Data Type


Exact Salesorders to  Order
---------------------------
Every Exact Salesorders will be synchronized with a  Order.

Once a link between a Exact Salesorders and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorders and a  Order:

.. list-table::
   :header-rows: 1

   * - Exact Salesorders Property
     -  Order Property
     -  Data Type
   * - Discount
     - totalDiscountAmountInCurrency
     - "string"

