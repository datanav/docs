===================================
BusinessNxt to ExactOnline Dataflow
===================================

Generated: 2024-09-11 08:38:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessNxt to ExactOnline. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


BusinessNxt Address to ExactOnline Addresses
--------------------------------------------
Every BusinessNxt Address will be synchronized with a ExactOnline Addresses.

Once a link between a BusinessNxt Address and a ExactOnline Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Address and a ExactOnline Addresses:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Address Property
     - ExactOnline Addresses Property
     - ExactOnline Data Type
   * - countryNo
     - Country
     - "string"
   * - postalArea
     - City
     - "string"


BusinessNxt Company to ExactOnline Addresses
--------------------------------------------
Every BusinessNxt Company will be synchronized with a ExactOnline Addresses.

Once a link between a BusinessNxt Company and a ExactOnline Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Company and a ExactOnline Addresses:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Company Property
     - ExactOnline Addresses Property
     - ExactOnline Data Type


BusinessNxt Currency to ExactOnline Currencies
----------------------------------------------
Every BusinessNxt Currency will be synchronized with a ExactOnline Currencies.

Once a link between a BusinessNxt Currency and a ExactOnline Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Currency and a ExactOnline Currencies:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Currency Property
     - ExactOnline Currencies Property
     - ExactOnline Data Type
   * - name
     - Description
     - "string"


BusinessNxt Order to ExactOnline Salesorders
--------------------------------------------
Every BusinessNxt Order will be synchronized with a ExactOnline Salesorders.

Once a link between a BusinessNxt Order and a ExactOnline Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Order and a ExactOnline Salesorders:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Order Property
     - ExactOnline Salesorders Property
     - ExactOnline Data Type
   * - totalDiscountAmountInCurrency
     - Discount
     - "string"


BusinessNxt Orderline to ExactOnline Salesorderlines
----------------------------------------------------
Every BusinessNxt Orderline will be synchronized with a ExactOnline Salesorderlines.

Once a link between a BusinessNxt Orderline and a ExactOnline Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Orderline and a ExactOnline Salesorderlines:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Orderline Property
     - ExactOnline Salesorderlines Property
     - ExactOnline Data Type


BusinessNxt Product to ExactOnline Items
----------------------------------------
Every BusinessNxt Product will be synchronized with a ExactOnline Items.

Once a link between a BusinessNxt Product and a ExactOnline Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Product and a ExactOnline Items:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Product Property
     - ExactOnline Items Property
     - ExactOnline Data Type

