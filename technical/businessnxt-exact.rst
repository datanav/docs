====================================
BusinessNxt to Exact Online Dataflow
====================================

Generated: 2024-09-11 08:35:29

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessNxt to Exact Online. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Visma Address to Exact Accounts
-------------------------------
Every Visma Address will be synchronized with a Exact Accounts.

Once a link between a Visma Address and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Address and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - Visma Address Property
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


Visma Company to Exact Accounts
-------------------------------
Every Visma Company will be synchronized with a Exact Accounts.

Once a link between a Visma Company and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Company and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - Visma Company Property
     - Exact Accounts Property
     - Exact Data Type
   * - companyNo
     - ID
     - "string"
   * - name
     - Name
     - "string"


Visma Country to Exact Currencies
---------------------------------
Every Visma Country will be synchronized with a Exact Currencies.

Once a link between a Visma Country and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Country and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - Visma Country Property
     - Exact Currencies Property
     - Exact Data Type
   * - name
     - Description
     - "string"


Visma Order to Exact Quotations
-------------------------------
Every Visma Order will be synchronized with a Exact Quotations.

Once a link between a Visma Order and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Order and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - Visma Order Property
     - Exact Quotations Property
     - Exact Data Type


Visma Orderline to Exact Quotations
-----------------------------------
Every Visma Orderline will be synchronized with a Exact Quotations.

Once a link between a Visma Orderline and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Orderline and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - Visma Orderline Property
     - Exact Quotations Property
     - Exact Data Type


Visma Productcategory to Exact Currencies
-----------------------------------------
Every Visma Productcategory will be synchronized with a Exact Currencies.

Once a link between a Visma Productcategory and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Productcategory and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - Visma Productcategory Property
     - Exact Currencies Property
     - Exact Data Type
   * - text
     - Description
     - "string"


Visma Vat to Exact Currencies
-----------------------------
Every Visma Vat will be synchronized with a Exact Currencies.

Once a link between a Visma Vat and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Vat and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - Visma Vat Property
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

