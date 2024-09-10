=============================
Businessnxt to Exact Dataflow
=============================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businessnxt to Exact. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


Businessnxt Address to Exact Addresses
--------------------------------------
Every Businessnxt Address will be synchronized with a Exact Addresses.

Once a link between a Businessnxt Address and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Address and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - Businessnxt Address Property
     - Exact Addresses Property
     - Exact Data Type
   * - countryNo
     - Country
     - "string"
   * - postalArea
     - City
     - "string"


Businessnxt Company to Exact Addresses
--------------------------------------
Every Businessnxt Company will be synchronized with a Exact Addresses.

Once a link between a Businessnxt Company and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Company and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - Businessnxt Company Property
     - Exact Addresses Property
     - Exact Data Type


Businessnxt Currency to Exact Currencies
----------------------------------------
Every Businessnxt Currency will be synchronized with a Exact Currencies.

Once a link between a Businessnxt Currency and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Currency and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - Businessnxt Currency Property
     - Exact Currencies Property
     - Exact Data Type
   * - name
     - Description
     - "string"


Businessnxt Order to Exact Salesorders
--------------------------------------
Every Businessnxt Order will be synchronized with a Exact Salesorders.

Once a link between a Businessnxt Order and a Exact Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Order and a Exact Salesorders:

.. list-table::
   :header-rows: 1

   * - Businessnxt Order Property
     - Exact Salesorders Property
     - Exact Data Type
   * - totalDiscountAmountInCurrency
     - Discount
     - "string"


Businessnxt Orderline to Exact Salesorderlines
----------------------------------------------
Every Businessnxt Orderline will be synchronized with a Exact Salesorderlines.

Once a link between a Businessnxt Orderline and a Exact Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Orderline and a Exact Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Businessnxt Orderline Property
     - Exact Salesorderlines Property
     - Exact Data Type


Businessnxt Product to Exact Items
----------------------------------
Every Businessnxt Product will be synchronized with a Exact Items.

Once a link between a Businessnxt Product and a Exact Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Product and a Exact Items:

.. list-table::
   :header-rows: 1

   * - Businessnxt Product Property
     - Exact Items Property
     - Exact Data Type

