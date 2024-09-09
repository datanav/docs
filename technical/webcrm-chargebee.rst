============================
Webcrm to Chargebee Dataflow
============================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Webcrm to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Webcrm Opportunities to Chargebee Order
---------------------------------------
Every Webcrm Opportunities will be synchronized with a Chargebee Order.

Once a link between a Webcrm Opportunities and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Opportunities and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Webcrm Opportunities Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - OpportunityCurrencyName
     - currency_code
     - "string"


Webcrm Organisations to Chargebee Business_entity
-------------------------------------------------
Every Webcrm Organisations will be synchronized with a Chargebee Business_entity.

Once a link between a Webcrm Organisations and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Organisations and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - Webcrm Organisations Property
     - Chargebee Business_entity Property
     - Chargebee Data Type
   * - OrganisationName
     - name
     - "string"


Webcrm Persons to Chargebee Customer
------------------------------------
Every Webcrm Persons will be synchronized with a Chargebee Customer.

Once a link between a Webcrm Persons and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Persons and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Webcrm Persons Property
     - Chargebee Customer Property
     - Chargebee Data Type
   * - PersonFirstName
     - first_name
     - "string"
   * - PersonLastName
     - last_name
     - "string"


Webcrm Quotationline to Chargebee Order
---------------------------------------
Every Webcrm Quotationline will be synchronized with a Chargebee Order.

Once a link between a Webcrm Quotationline and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Quotationline and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Webcrm Quotationline Property
     - Chargebee Order Property
     - Chargebee Data Type


Webcrm Users to Chargebee Customer
----------------------------------
Every Webcrm Users will be synchronized with a Chargebee Customer.

Once a link between a Webcrm Users and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Users and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Webcrm Users Property
     - Chargebee Customer Property
     - Chargebee Data Type


Webcrm Products to Chargebee Item
---------------------------------
Every Webcrm Products will be synchronized with a Chargebee Item.

Once a link between a Webcrm Products and a Chargebee Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Products and a Chargebee Item:

.. list-table::
   :header-rows: 1

   * - Webcrm Products Property
     - Chargebee Item Property
     - Chargebee Data Type

