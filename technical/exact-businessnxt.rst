===================================
ExactOnline to BusinessNxt Dataflow
===================================

Generated: 2024-09-11 08:38:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ExactOnline to BusinessNxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


ExactOnline Addresses to BusinessNxt Country
--------------------------------------------
Every ExactOnline Addresses will be synchronized with a BusinessNxt Country.

Once a link between a ExactOnline Addresses and a BusinessNxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Addresses and a BusinessNxt Country:

.. list-table::
   :header-rows: 1

   * - ExactOnline Addresses Property
     - BusinessNxt Country Property
     - BusinessNxt Data Type
   * - CountryName
     - name
     - "string"


ExactOnline Currencies to BusinessNxt Currency
----------------------------------------------
Every ExactOnline Currencies will be synchronized with a BusinessNxt Currency.

Once a link between a ExactOnline Currencies and a BusinessNxt Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Currencies and a BusinessNxt Currency:

.. list-table::
   :header-rows: 1

   * - ExactOnline Currencies Property
     - BusinessNxt Currency Property
     - BusinessNxt Data Type
   * - Description
     - name
     - "string"


ExactOnline Items to BusinessNxt Product
----------------------------------------
Every ExactOnline Items will be synchronized with a BusinessNxt Product.

Once a link between a ExactOnline Items and a BusinessNxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Items and a BusinessNxt Product:

.. list-table::
   :header-rows: 1

   * - ExactOnline Items Property
     - BusinessNxt Product Property
     - BusinessNxt Data Type


ExactOnline Salesorderlines to BusinessNxt Orderline
----------------------------------------------------
Every ExactOnline Salesorderlines will be synchronized with a BusinessNxt Orderline.

Once a link between a ExactOnline Salesorderlines and a BusinessNxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Salesorderlines and a BusinessNxt Orderline:

.. list-table::
   :header-rows: 1

   * - ExactOnline Salesorderlines Property
     - BusinessNxt Orderline Property
     - BusinessNxt Data Type


ExactOnline Salesorders to BusinessNxt Order
--------------------------------------------
Every ExactOnline Salesorders will be synchronized with a BusinessNxt Order.

Once a link between a ExactOnline Salesorders and a BusinessNxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Salesorders and a BusinessNxt Order:

.. list-table::
   :header-rows: 1

   * - ExactOnline Salesorders Property
     - BusinessNxt Order Property
     - BusinessNxt Data Type
   * - Discount
     - totalDiscountAmountInCurrency
     - "string"

