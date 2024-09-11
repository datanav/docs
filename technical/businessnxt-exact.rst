===========================================
Visma Business Nxt to Exact Online Dataflow
===========================================

Generated: 2024-09-11 07:47:14

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Visma Business Nxt to Exact Online. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businessnxt Address to Exact Accounts
-------------------------------------
Every Businessnxt Address will be synchronized with a Exact Accounts.

Once a link between a Businessnxt Address and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Address and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - Businessnxt Address Property
     - Exact Accounts Property
     - Exact Data Type
   * - addressNo
     - ID
     - "string"
   * - countryNo
     - Country
     - "string"
   * - name
     - Name
     - "string"
   * - noOfEmployees
     - CompanySize
     - "string"
   * - postCode
     - Postcode
     - "string"
   * - postalArea
     - City
     - "string"


Businessnxt Company to Exact Accounts
-------------------------------------
Every Businessnxt Company will be synchronized with a Exact Accounts.

Once a link between a Businessnxt Company and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Company and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - Businessnxt Company Property
     - Exact Accounts Property
     - Exact Data Type
   * - companyNo
     - ID
     - "string"
   * - name
     - Name
     - "string"


Businessnxt Country to Exact Currencies
---------------------------------------
Every Businessnxt Country will be synchronized with a Exact Currencies.

Once a link between a Businessnxt Country and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Country and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - Businessnxt Country Property
     - Exact Currencies Property
     - Exact Data Type
   * - name
     - Description
     - "string"


Businessnxt Order to Exact Quotations
-------------------------------------
Every Businessnxt Order will be synchronized with a Exact Quotations.

Once a link between a Businessnxt Order and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Order and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - Businessnxt Order Property
     - Exact Quotations Property
     - Exact Data Type


Businessnxt Orderline to Exact Quotations
-----------------------------------------
Every Businessnxt Orderline will be synchronized with a Exact Quotations.

Once a link between a Businessnxt Orderline and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Orderline and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - Businessnxt Orderline Property
     - Exact Quotations Property
     - Exact Data Type


Businessnxt Productcategory to Exact Currencies
-----------------------------------------------
Every Businessnxt Productcategory will be synchronized with a Exact Currencies.

Once a link between a Businessnxt Productcategory and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Productcategory and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - Businessnxt Productcategory Property
     - Exact Currencies Property
     - Exact Data Type
   * - text
     - Description
     - "string"


Businessnxt Vat to Exact Currencies
-----------------------------------
Every Businessnxt Vat will be synchronized with a Exact Currencies.

Once a link between a Businessnxt Vat and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Vat and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - Businessnxt Vat Property
     - Exact Currencies Property
     - Exact Data Type


Visma Address to Exact Addresses
--------------------------------
Every Visma Address will be synchronized with a Exact Addresses.

Once a link between a Visma Address and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Address and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - Visma Address Property
     - Exact Addresses Property
     - Exact Data Type
   * - countryNo
     - Country
     - "string"
   * - postalArea
     - City
     - "string"


Visma Company to Exact Addresses
--------------------------------
Every Visma Company will be synchronized with a Exact Addresses.

Once a link between a Visma Company and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Company and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - Visma Company Property
     - Exact Addresses Property
     - Exact Data Type


Visma Currency to Exact Currencies
----------------------------------
Every Visma Currency will be synchronized with a Exact Currencies.

Once a link between a Visma Currency and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Currency and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - Visma Currency Property
     - Exact Currencies Property
     - Exact Data Type
   * - name
     - Description
     - "string"


Visma Order to Exact Salesorders
--------------------------------
Every Visma Order will be synchronized with a Exact Salesorders.

Once a link between a Visma Order and a Exact Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Order and a Exact Salesorders:

.. list-table::
   :header-rows: 1

   * - Visma Order Property
     - Exact Salesorders Property
     - Exact Data Type
   * - totalDiscountAmountInCurrency
     - Discount
     - "string"


Visma Orderline to Exact Salesorderlines
----------------------------------------
Every Visma Orderline will be synchronized with a Exact Salesorderlines.

Once a link between a Visma Orderline and a Exact Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Orderline and a Exact Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Visma Orderline Property
     - Exact Salesorderlines Property
     - Exact Data Type


Visma Product to Exact Items
----------------------------
Every Visma Product will be synchronized with a Exact Items.

Once a link between a Visma Product and a Exact Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Product and a Exact Items:

.. list-table::
   :header-rows: 1

   * - Visma Product Property
     - Exact Items Property
     - Exact Data Type

