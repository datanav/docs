===========================
Chargebee to Exact Dataflow
===========================

Generated: 2024-09-08 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Exact. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Address to Exact Addresses
------------------------------------
Every Chargebee Address will be synchronized with a Exact Addresses.

Once a link between a Chargebee Address and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Address and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - Chargebee Address Property
     - Exact Addresses Property
     - Exact Data Type
   * - city
     - City
     - "string"
   * - country
     - Country
     - "string"
   * - country
     - CountryName
     - "string"


Chargebee Business_entity to Exact Accounts
-------------------------------------------
Every Chargebee Business_entity will be synchronized with a Exact Accounts.

Once a link between a Chargebee Business_entity and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Business_entity and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - Chargebee Business_entity Property
     - Exact Accounts Property
     - Exact Data Type
   * - name
     - Name
     - "string"


Chargebee Currency to Exact Currencies
--------------------------------------
Every Chargebee Currency will be synchronized with a Exact Currencies.

Once a link between a Chargebee Currency and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Currency and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - Chargebee Currency Property
     - Exact Currencies Property
     - Exact Data Type


Chargebee Customer to Exact Contacts
------------------------------------
Every Chargebee Customer will be synchronized with a Exact Contacts.

Once a link between a Chargebee Customer and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Exact Contacts Property
     - Exact Data Type
   * - billing_address.city
     - City
     - "string"
   * - billing_address.country
     - Country
     - "string"


Chargebee Item_family to Exact Currencies
-----------------------------------------
Every Chargebee Item_family will be synchronized with a Exact Currencies.

Once a link between a Chargebee Item_family and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item_family and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - Chargebee Item_family Property
     - Exact Currencies Property
     - Exact Data Type


Chargebee Order to Exact Quotations
-----------------------------------
Every Chargebee Order will be synchronized with a Exact Quotations.

Once a link between a Chargebee Order and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Order and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - Chargebee Order Property
     - Exact Quotations Property
     - Exact Data Type
   * - currency_code
     - Currency
     - "string"


Chargebee Item to Exact Items
-----------------------------
Every Chargebee Item will be synchronized with a Exact Items.

Once a link between a Chargebee Item and a Exact Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a Exact Items:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - Exact Items Property
     - Exact Data Type


Chargebee Order to Exact Salesorders
------------------------------------
Every Chargebee Order will be synchronized with a Exact Salesorders.

Once a link between a Chargebee Order and a Exact Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Order and a Exact Salesorders:

.. list-table::
   :header-rows: 1

   * - Chargebee Order Property
     - Exact Salesorders Property
     - Exact Data Type
   * - currency_code
     - Currency
     - "string"

