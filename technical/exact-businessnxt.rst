=====================================
Exact Online to Business Nxt Dataflow
=====================================

Generated: 2024-09-11 11:41:16

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact Online to Business Nxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ExactOnline Accounts to BusinessNxt Address
-------------------------------------------
Every ExactOnline Accounts will be synchronized with a BusinessNxt Address.

Once a link between a ExactOnline Accounts and a BusinessNxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Accounts and a BusinessNxt Address:

.. list-table::
   :header-rows: 1

   * - ExactOnline Accounts Property
     - BusinessNxt Address Property
     - BusinessNxt Data Type
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


ExactOnline Currencies to BusinessNxt Country
---------------------------------------------
Every ExactOnline Currencies will be synchronized with a BusinessNxt Country.

Once a link between a ExactOnline Currencies and a BusinessNxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Currencies and a BusinessNxt Country:

.. list-table::
   :header-rows: 1

   * - ExactOnline Currencies Property
     - BusinessNxt Country Property
     - BusinessNxt Data Type
   * - Description
     - name
     - "string"


ExactOnline Departments to BusinessNxt Address
----------------------------------------------
Every ExactOnline Departments will be synchronized with a BusinessNxt Address.

Once a link between a ExactOnline Departments and a BusinessNxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Departments and a BusinessNxt Address:

.. list-table::
   :header-rows: 1

   * - ExactOnline Departments Property
     - BusinessNxt Address Property
     - BusinessNxt Data Type


ExactOnline Divisions to BusinessNxt Address
--------------------------------------------
Every ExactOnline Divisions will be synchronized with a BusinessNxt Address.

Once a link between a ExactOnline Divisions and a BusinessNxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Divisions and a BusinessNxt Address:

.. list-table::
   :header-rows: 1

   * - ExactOnline Divisions Property
     - BusinessNxt Address Property
     - BusinessNxt Data Type


ExactOnline Quotations to BusinessNxt Order
-------------------------------------------
Every ExactOnline Quotations will be synchronized with a BusinessNxt Order.

Once a link between a ExactOnline Quotations and a BusinessNxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Quotations and a BusinessNxt Order:

.. list-table::
   :header-rows: 1

   * - ExactOnline Quotations Property
     - BusinessNxt Order Property
     - BusinessNxt Data Type


ExactOnline Salesinvoices to BusinessNxt Order
----------------------------------------------
Every ExactOnline Salesinvoices will be synchronized with a BusinessNxt Order.

Once a link between a ExactOnline Salesinvoices and a BusinessNxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Salesinvoices and a BusinessNxt Order:

.. list-table::
   :header-rows: 1

   * - ExactOnline Salesinvoices Property
     - BusinessNxt Order Property
     - BusinessNxt Data Type


ExactOnline Salesorderlines to BusinessNxt Order
------------------------------------------------
Every ExactOnline Salesorderlines will be synchronized with a BusinessNxt Order.

Once a link between a ExactOnline Salesorderlines and a BusinessNxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Salesorderlines and a BusinessNxt Order:

.. list-table::
   :header-rows: 1

   * - ExactOnline Salesorderlines Property
     - BusinessNxt Order Property
     - BusinessNxt Data Type


ExactOnline Units to BusinessNxt Country
----------------------------------------
Every ExactOnline Units will be synchronized with a BusinessNxt Country.

Once a link between a ExactOnline Units and a BusinessNxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Units and a BusinessNxt Country:

.. list-table::
   :header-rows: 1

   * - ExactOnline Units Property
     - BusinessNxt Country Property
     - BusinessNxt Data Type
   * - Description
     - name
     - "string"


ExactOnline Vatcodes to BusinessNxt Country
-------------------------------------------
Every ExactOnline Vatcodes will be synchronized with a BusinessNxt Country.

Once a link between a ExactOnline Vatcodes and a BusinessNxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Vatcodes and a BusinessNxt Country:

.. list-table::
   :header-rows: 1

   * - ExactOnline Vatcodes Property
     - BusinessNxt Country Property
     - BusinessNxt Data Type


Exact Online Addresses to Business Nxt Country
----------------------------------------------
Every Exact Online Addresses will be synchronized with a Business Nxt Country.

Once a link between a Exact Online Addresses and a Business Nxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Addresses and a Business Nxt Country:

.. list-table::
   :header-rows: 1

   * - Exact Online Addresses Property
     - Business Nxt Country Property
     - Business Nxt Data Type
   * - CountryName
     - name
     - "string"


Exact Online Currencies to Business Nxt Currency
------------------------------------------------
Every Exact Online Currencies will be synchronized with a Business Nxt Currency.

Once a link between a Exact Online Currencies and a Business Nxt Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Currencies and a Business Nxt Currency:

.. list-table::
   :header-rows: 1

   * - Exact Online Currencies Property
     - Business Nxt Currency Property
     - Business Nxt Data Type
   * - Description
     - name
     - "string"


Exact Online Items to Business Nxt Product
------------------------------------------
Every Exact Online Items will be synchronized with a Business Nxt Product.

Once a link between a Exact Online Items and a Business Nxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Items and a Business Nxt Product:

.. list-table::
   :header-rows: 1

   * - Exact Online Items Property
     - Business Nxt Product Property
     - Business Nxt Data Type


Exact Online Salesorderlines to Business Nxt Orderline
------------------------------------------------------
Every Exact Online Salesorderlines will be synchronized with a Business Nxt Orderline.

Once a link between a Exact Online Salesorderlines and a Business Nxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Salesorderlines and a Business Nxt Orderline:

.. list-table::
   :header-rows: 1

   * - Exact Online Salesorderlines Property
     - Business Nxt Orderline Property
     - Business Nxt Data Type


Exact Online Salesorders to Business Nxt Order
----------------------------------------------
Every Exact Online Salesorders will be synchronized with a Business Nxt Order.

Once a link between a Exact Online Salesorders and a Business Nxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Salesorders and a Business Nxt Order:

.. list-table::
   :header-rows: 1

   * - Exact Online Salesorders Property
     - Business Nxt Order Property
     - Business Nxt Data Type
   * - Discount
     - totalDiscountAmountInCurrency
     - "string"

