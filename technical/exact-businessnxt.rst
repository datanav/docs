===================================
ExactOnline to BusinessNxt Dataflow
===================================

Generated: 2024-09-11 08:49:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ExactOnline to BusinessNxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Accounts to Visma Address
-------------------------------
Every Exact Accounts will be synchronized with a Visma Address.

Once a link between a Exact Accounts and a Visma Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Accounts and a Visma Address:

.. list-table::
   :header-rows: 1

   * - Exact Accounts Property
     - Visma Address Property
     - Visma Data Type
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


Exact Currencies to Visma Country
---------------------------------
Every Exact Currencies will be synchronized with a Visma Country.

Once a link between a Exact Currencies and a Visma Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Currencies and a Visma Country:

.. list-table::
   :header-rows: 1

   * - Exact Currencies Property
     - Visma Country Property
     - Visma Data Type
   * - Description
     - name
     - "string"


Exact Departments to Visma Address
----------------------------------
Every Exact Departments will be synchronized with a Visma Address.

Once a link between a Exact Departments and a Visma Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Departments and a Visma Address:

.. list-table::
   :header-rows: 1

   * - Exact Departments Property
     - Visma Address Property
     - Visma Data Type


Exact Divisions to Visma Address
--------------------------------
Every Exact Divisions will be synchronized with a Visma Address.

Once a link between a Exact Divisions and a Visma Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Divisions and a Visma Address:

.. list-table::
   :header-rows: 1

   * - Exact Divisions Property
     - Visma Address Property
     - Visma Data Type


Exact Quotations to Visma Order
-------------------------------
Every Exact Quotations will be synchronized with a Visma Order.

Once a link between a Exact Quotations and a Visma Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Quotations and a Visma Order:

.. list-table::
   :header-rows: 1

   * - Exact Quotations Property
     - Visma Order Property
     - Visma Data Type


Exact Salesinvoices to Visma Order
----------------------------------
Every Exact Salesinvoices will be synchronized with a Visma Order.

Once a link between a Exact Salesinvoices and a Visma Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesinvoices and a Visma Order:

.. list-table::
   :header-rows: 1

   * - Exact Salesinvoices Property
     - Visma Order Property
     - Visma Data Type


Exact Salesorderlines to Visma Order
------------------------------------
Every Exact Salesorderlines will be synchronized with a Visma Order.

Once a link between a Exact Salesorderlines and a Visma Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorderlines and a Visma Order:

.. list-table::
   :header-rows: 1

   * - Exact Salesorderlines Property
     - Visma Order Property
     - Visma Data Type


Exact Units to Visma Country
----------------------------
Every Exact Units will be synchronized with a Visma Country.

Once a link between a Exact Units and a Visma Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Units and a Visma Country:

.. list-table::
   :header-rows: 1

   * - Exact Units Property
     - Visma Country Property
     - Visma Data Type
   * - Description
     - name
     - "string"


Exact Vatcodes to Visma Country
-------------------------------
Every Exact Vatcodes will be synchronized with a Visma Country.

Once a link between a Exact Vatcodes and a Visma Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Vatcodes and a Visma Country:

.. list-table::
   :header-rows: 1

   * - Exact Vatcodes Property
     - Visma Country Property
     - Visma Data Type


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

