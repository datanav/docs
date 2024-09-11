===================================
BusinessNxt to ExactOnline Dataflow
===================================

Generated: 2024-09-11 09:30:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessNxt to ExactOnline. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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

