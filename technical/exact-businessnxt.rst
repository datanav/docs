==========================================
ExactOnline to Visma Business Nxt Dataflow
==========================================

Generated: 2024-09-11 08:35:29

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ExactOnline to Visma Business Nxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


Exact Addresses to Visma Country
--------------------------------
Every Exact Addresses will be synchronized with a Visma Country.

Once a link between a Exact Addresses and a Visma Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Addresses and a Visma Country:

.. list-table::
   :header-rows: 1

   * - Exact Addresses Property
     - Visma Country Property
     - Visma Data Type
   * - CountryName
     - name
     - "string"


Exact Currencies to Visma Currency
----------------------------------
Every Exact Currencies will be synchronized with a Visma Currency.

Once a link between a Exact Currencies and a Visma Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Currencies and a Visma Currency:

.. list-table::
   :header-rows: 1

   * - Exact Currencies Property
     - Visma Currency Property
     - Visma Data Type
   * - Description
     - name
     - "string"


Exact Items to Visma Product
----------------------------
Every Exact Items will be synchronized with a Visma Product.

Once a link between a Exact Items and a Visma Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Items and a Visma Product:

.. list-table::
   :header-rows: 1

   * - Exact Items Property
     - Visma Product Property
     - Visma Data Type


Exact Salesorderlines to Visma Orderline
----------------------------------------
Every Exact Salesorderlines will be synchronized with a Visma Orderline.

Once a link between a Exact Salesorderlines and a Visma Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorderlines and a Visma Orderline:

.. list-table::
   :header-rows: 1

   * - Exact Salesorderlines Property
     - Visma Orderline Property
     - Visma Data Type


Exact Salesorders to Visma Order
--------------------------------
Every Exact Salesorders will be synchronized with a Visma Order.

Once a link between a Exact Salesorders and a Visma Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorders and a Visma Order:

.. list-table::
   :header-rows: 1

   * - Exact Salesorders Property
     - Visma Order Property
     - Visma Data Type
   * - Discount
     - totalDiscountAmountInCurrency
     - "string"

