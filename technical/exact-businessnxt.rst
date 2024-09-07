=============================
Exact to Businessnxt Dataflow
=============================

Generated: 2024-09-07 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact to Businessnxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Accounts to Businessnxt Address
-------------------------------------
Every Exact Accounts will be synchronized with a Businessnxt Address.

Once a link between a Exact Accounts and a Businessnxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Accounts and a Businessnxt Address:

.. list-table::
   :header-rows: 1

   * - Exact Accounts Property
     - Businessnxt Address Property
     - Businessnxt Data Type
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


Exact Currencies to Businessnxt Country
---------------------------------------
Every Exact Currencies will be synchronized with a Businessnxt Country.

Once a link between a Exact Currencies and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Currencies and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Exact Currencies Property
     - Businessnxt Country Property
     - Businessnxt Data Type
   * - Description
     - name
     - "string"


Exact Departments to Businessnxt Address
----------------------------------------
Every Exact Departments will be synchronized with a Businessnxt Address.

Once a link between a Exact Departments and a Businessnxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Departments and a Businessnxt Address:

.. list-table::
   :header-rows: 1

   * - Exact Departments Property
     - Businessnxt Address Property
     - Businessnxt Data Type


Exact Divisions to Businessnxt Address
--------------------------------------
Every Exact Divisions will be synchronized with a Businessnxt Address.

Once a link between a Exact Divisions and a Businessnxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Divisions and a Businessnxt Address:

.. list-table::
   :header-rows: 1

   * - Exact Divisions Property
     - Businessnxt Address Property
     - Businessnxt Data Type


Exact Quotations to Businessnxt Order
-------------------------------------
Every Exact Quotations will be synchronized with a Businessnxt Order.

Once a link between a Exact Quotations and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Quotations and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Exact Quotations Property
     - Businessnxt Order Property
     - Businessnxt Data Type


Exact Salesinvoices to Businessnxt Order
----------------------------------------
Every Exact Salesinvoices will be synchronized with a Businessnxt Order.

Once a link between a Exact Salesinvoices and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesinvoices and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Exact Salesinvoices Property
     - Businessnxt Order Property
     - Businessnxt Data Type


Exact Salesorderlines to Businessnxt Order
------------------------------------------
Every Exact Salesorderlines will be synchronized with a Businessnxt Order.

Once a link between a Exact Salesorderlines and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorderlines and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Exact Salesorderlines Property
     - Businessnxt Order Property
     - Businessnxt Data Type


Exact Units to Businessnxt Country
----------------------------------
Every Exact Units will be synchronized with a Businessnxt Country.

Once a link between a Exact Units and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Units and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Exact Units Property
     - Businessnxt Country Property
     - Businessnxt Data Type
   * - Description
     - name
     - "string"


Exact Vatcodes to Businessnxt Country
-------------------------------------
Every Exact Vatcodes will be synchronized with a Businessnxt Country.

Once a link between a Exact Vatcodes and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Vatcodes and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Exact Vatcodes Property
     - Businessnxt Country Property
     - Businessnxt Data Type


Exact Addresses to Businessnxt Country
--------------------------------------
Every Exact Addresses will be synchronized with a Businessnxt Country.

Once a link between a Exact Addresses and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Addresses and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Exact Addresses Property
     - Businessnxt Country Property
     - Businessnxt Data Type
   * - CountryName
     - name
     - "string"


Exact Currencies to Businessnxt Currency
----------------------------------------
Every Exact Currencies will be synchronized with a Businessnxt Currency.

Once a link between a Exact Currencies and a Businessnxt Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Currencies and a Businessnxt Currency:

.. list-table::
   :header-rows: 1

   * - Exact Currencies Property
     - Businessnxt Currency Property
     - Businessnxt Data Type
   * - Description
     - name
     - "string"


Exact Items to Businessnxt Product
----------------------------------
Every Exact Items will be synchronized with a Businessnxt Product.

Once a link between a Exact Items and a Businessnxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Items and a Businessnxt Product:

.. list-table::
   :header-rows: 1

   * - Exact Items Property
     - Businessnxt Product Property
     - Businessnxt Data Type


Exact Salesorderlines to Businessnxt Orderline
----------------------------------------------
Every Exact Salesorderlines will be synchronized with a Businessnxt Orderline.

Once a link between a Exact Salesorderlines and a Businessnxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorderlines and a Businessnxt Orderline:

.. list-table::
   :header-rows: 1

   * - Exact Salesorderlines Property
     - Businessnxt Orderline Property
     - Businessnxt Data Type


Exact Salesorders to Businessnxt Order
--------------------------------------
Every Exact Salesorders will be synchronized with a Businessnxt Order.

Once a link between a Exact Salesorders and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorders and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Exact Salesorders Property
     - Businessnxt Order Property
     - Businessnxt Data Type
   * - Discount
     - totalDiscountAmountInCurrency
     - "string"

