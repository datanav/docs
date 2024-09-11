====================================
Exact Online to BusinessNxt Dataflow
====================================

Generated: 2024-09-11 11:38:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact Online to BusinessNxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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

