==================================
Chargebee to Exact Online Dataflow
==================================

Generated: 2024-09-12 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Exact Online. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Address to Exact Online Addresses
-------------------------------------------
Every Chargebee Address will be synchronized with a Exact Online Addresses.

Once a link between a Chargebee Address and a Exact Online Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Address and a Exact Online Addresses:

.. list-table::
   :header-rows: 1

   * - Chargebee Address Property
     - Exact Online Addresses Property
     - Exact Online Data Type
   * - city
     - City
     - "string"
   * - country
     - Country
     - "string"
   * - country
     - CountryName
     - "string"


Chargebee Business_entity to Exact Online Accounts
--------------------------------------------------
Every Chargebee Business_entity will be synchronized with a Exact Online Accounts.

Once a link between a Chargebee Business_entity and a Exact Online Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Business_entity and a Exact Online Accounts:

.. list-table::
   :header-rows: 1

   * - Chargebee Business_entity Property
     - Exact Online Accounts Property
     - Exact Online Data Type
   * - name
     - Name
     - "string"


Chargebee Currency to Exact Online Currencies
---------------------------------------------
Every Chargebee Currency will be synchronized with a Exact Online Currencies.

Once a link between a Chargebee Currency and a Exact Online Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Currency and a Exact Online Currencies:

.. list-table::
   :header-rows: 1

   * - Chargebee Currency Property
     - Exact Online Currencies Property
     - Exact Online Data Type


Chargebee Customer to Exact Online Contacts
-------------------------------------------
Every Chargebee Customer will be synchronized with a Exact Online Contacts.

Once a link between a Chargebee Customer and a Exact Online Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Exact Online Contacts:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Exact Online Contacts Property
     - Exact Online Data Type
   * - billing_address.city
     - City
     - "string"
   * - billing_address.country
     - Country
     - "string"


Chargebee Item_family to Exact Online Currencies
------------------------------------------------
Every Chargebee Item_family will be synchronized with a Exact Online Currencies.

Once a link between a Chargebee Item_family and a Exact Online Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item_family and a Exact Online Currencies:

.. list-table::
   :header-rows: 1

   * - Chargebee Item_family Property
     - Exact Online Currencies Property
     - Exact Online Data Type


Chargebee Order to Exact Online Quotations
------------------------------------------
Every Chargebee Order will be synchronized with a Exact Online Quotations.

Once a link between a Chargebee Order and a Exact Online Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Order and a Exact Online Quotations:

.. list-table::
   :header-rows: 1

   * - Chargebee Order Property
     - Exact Online Quotations Property
     - Exact Online Data Type
   * - currency_code
     - Currency
     - "string"


Chargebee Item to Exact Online Items
------------------------------------
Every Chargebee Item will be synchronized with a Exact Online Items.

Once a link between a Chargebee Item and a Exact Online Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a Exact Online Items:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - Exact Online Items Property
     - Exact Online Data Type


Chargebee Order to Exact Online Salesorders
-------------------------------------------
Every Chargebee Order will be synchronized with a Exact Online Salesorders.

Once a link between a Chargebee Order and a Exact Online Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Order and a Exact Online Salesorders:

.. list-table::
   :header-rows: 1

   * - Chargebee Order Property
     - Exact Online Salesorders Property
     - Exact Online Data Type
   * - currency_code
     - Currency
     - "string"

