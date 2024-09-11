=====================================
Business Nxt to Exact Online Dataflow
=====================================

Generated: 2024-09-11 11:41:16

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Nxt to Exact Online. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

BusinessNxt Address to ExactOnline Accounts
-------------------------------------------
Every BusinessNxt Address will be synchronized with a ExactOnline Accounts.

Once a link between a BusinessNxt Address and a ExactOnline Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Address and a ExactOnline Accounts:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Address Property
     - ExactOnline Accounts Property
     - ExactOnline Data Type
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


BusinessNxt Company to ExactOnline Accounts
-------------------------------------------
Every BusinessNxt Company will be synchronized with a ExactOnline Accounts.

Once a link between a BusinessNxt Company and a ExactOnline Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Company and a ExactOnline Accounts:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Company Property
     - ExactOnline Accounts Property
     - ExactOnline Data Type
   * - companyNo
     - ID
     - "string"
   * - name
     - Name
     - "string"


BusinessNxt Country to ExactOnline Currencies
---------------------------------------------
Every BusinessNxt Country will be synchronized with a ExactOnline Currencies.

Once a link between a BusinessNxt Country and a ExactOnline Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Country and a ExactOnline Currencies:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Country Property
     - ExactOnline Currencies Property
     - ExactOnline Data Type
   * - name
     - Description
     - "string"


BusinessNxt Order to ExactOnline Quotations
-------------------------------------------
Every BusinessNxt Order will be synchronized with a ExactOnline Quotations.

Once a link between a BusinessNxt Order and a ExactOnline Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Order and a ExactOnline Quotations:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Order Property
     - ExactOnline Quotations Property
     - ExactOnline Data Type


BusinessNxt Orderline to ExactOnline Quotations
-----------------------------------------------
Every BusinessNxt Orderline will be synchronized with a ExactOnline Quotations.

Once a link between a BusinessNxt Orderline and a ExactOnline Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Orderline and a ExactOnline Quotations:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Orderline Property
     - ExactOnline Quotations Property
     - ExactOnline Data Type


BusinessNxt Productcategory to ExactOnline Currencies
-----------------------------------------------------
Every BusinessNxt Productcategory will be synchronized with a ExactOnline Currencies.

Once a link between a BusinessNxt Productcategory and a ExactOnline Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Productcategory and a ExactOnline Currencies:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Productcategory Property
     - ExactOnline Currencies Property
     - ExactOnline Data Type
   * - text
     - Description
     - "string"


BusinessNxt Vat to ExactOnline Currencies
-----------------------------------------
Every BusinessNxt Vat will be synchronized with a ExactOnline Currencies.

Once a link between a BusinessNxt Vat and a ExactOnline Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Vat and a ExactOnline Currencies:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Vat Property
     - ExactOnline Currencies Property
     - ExactOnline Data Type


Business Nxt Address to Exact Online Addresses
----------------------------------------------
Every Business Nxt Address will be synchronized with a Exact Online Addresses.

Once a link between a Business Nxt Address and a Exact Online Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Address and a Exact Online Addresses:

.. list-table::
   :header-rows: 1

   * - Business Nxt Address Property
     - Exact Online Addresses Property
     - Exact Online Data Type
   * - countryNo
     - Country
     - "string"
   * - postalArea
     - City
     - "string"


Business Nxt Company to Exact Online Addresses
----------------------------------------------
Every Business Nxt Company will be synchronized with a Exact Online Addresses.

Once a link between a Business Nxt Company and a Exact Online Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Company and a Exact Online Addresses:

.. list-table::
   :header-rows: 1

   * - Business Nxt Company Property
     - Exact Online Addresses Property
     - Exact Online Data Type


Business Nxt Currency to Exact Online Currencies
------------------------------------------------
Every Business Nxt Currency will be synchronized with a Exact Online Currencies.

Once a link between a Business Nxt Currency and a Exact Online Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Currency and a Exact Online Currencies:

.. list-table::
   :header-rows: 1

   * - Business Nxt Currency Property
     - Exact Online Currencies Property
     - Exact Online Data Type
   * - name
     - Description
     - "string"


Business Nxt Order to Exact Online Salesorders
----------------------------------------------
Every Business Nxt Order will be synchronized with a Exact Online Salesorders.

Once a link between a Business Nxt Order and a Exact Online Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Order and a Exact Online Salesorders:

.. list-table::
   :header-rows: 1

   * - Business Nxt Order Property
     - Exact Online Salesorders Property
     - Exact Online Data Type
   * - totalDiscountAmountInCurrency
     - Discount
     - "string"


Business Nxt Orderline to Exact Online Salesorderlines
------------------------------------------------------
Every Business Nxt Orderline will be synchronized with a Exact Online Salesorderlines.

Once a link between a Business Nxt Orderline and a Exact Online Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Orderline and a Exact Online Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Business Nxt Orderline Property
     - Exact Online Salesorderlines Property
     - Exact Online Data Type


Business Nxt Product to Exact Online Items
------------------------------------------
Every Business Nxt Product will be synchronized with a Exact Online Items.

Once a link between a Business Nxt Product and a Exact Online Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Product and a Exact Online Items:

.. list-table::
   :header-rows: 1

   * - Business Nxt Product Property
     - Exact Online Items Property
     - Exact Online Data Type

