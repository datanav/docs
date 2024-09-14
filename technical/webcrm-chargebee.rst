============================
WebCRM to Chargebee Dataflow
============================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WebCRM to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WebCRM Opportunities to Chargebee Order
---------------------------------------
Every WebCRM Opportunities will be synchronized with a Chargebee Order.

Once a link between a WebCRM Opportunities and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Opportunities and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - WebCRM Opportunities Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - OpportunityCurrencyName
     - currency_code
     - "string"


WebCRM Organisations to Chargebee Business_entity
-------------------------------------------------
Every WebCRM Organisations will be synchronized with a Chargebee Business_entity.

Once a link between a WebCRM Organisations and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Organisations and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - WebCRM Organisations Property
     - Chargebee Business_entity Property
     - Chargebee Data Type
   * - OrganisationName
     - name
     - "string"


WebCRM Persons to Chargebee Customer
------------------------------------
Every WebCRM Persons will be synchronized with a Chargebee Customer.

Once a link between a WebCRM Persons and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Persons and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - WebCRM Persons Property
     - Chargebee Customer Property
     - Chargebee Data Type
   * - PersonFirstName
     - first_name
     - "string"
   * - PersonLastName
     - last_name
     - "string"


WebCRM Quotationline to Chargebee Order
---------------------------------------
Every WebCRM Quotationline will be synchronized with a Chargebee Order.

Once a link between a WebCRM Quotationline and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Quotationline and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - WebCRM Quotationline Property
     - Chargebee Order Property
     - Chargebee Data Type


WebCRM Users to Chargebee Customer
----------------------------------
Every WebCRM Users will be synchronized with a Chargebee Customer.

Once a link between a WebCRM Users and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Users and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - WebCRM Users Property
     - Chargebee Customer Property
     - Chargebee Data Type


WebCRM Products to Chargebee Item
---------------------------------
Every WebCRM Products will be synchronized with a Chargebee Item.

Once a link between a WebCRM Products and a Chargebee Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Products and a Chargebee Item:

.. list-table::
   :header-rows: 1

   * - WebCRM Products Property
     - Chargebee Item Property
     - Chargebee Data Type

