==============================
BusinessNxt to WebCRM Dataflow
==============================

Generated: 2024-09-11 08:37:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessNxt to WebCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Visma Address to Webcrm Organisations
-------------------------------------
Every Visma Address will be synchronized with a Webcrm Organisations.

Once a link between a Visma Address and a Webcrm Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Address and a Webcrm Organisations:

.. list-table::
   :header-rows: 1

   * - Visma Address Property
     - Webcrm Organisations Property
     - Webcrm Data Type
   * - name
     - OrganisationName
     - "string"
   * - phone
     - OrganisationTelephone
     - "string"


Visma Company to Webcrm Organisations
-------------------------------------
Every Visma Company will be synchronized with a Webcrm Organisations.

Once a link between a Visma Company and a Webcrm Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Company and a Webcrm Organisations:

.. list-table::
   :header-rows: 1

   * - Visma Company Property
     - Webcrm Organisations Property
     - Webcrm Data Type
   * - name
     - OrganisationName
     - "string"


BusinessNxt Orderline to WebCRM Quotationline
---------------------------------------------
Every BusinessNxt Orderline will be synchronized with a WebCRM Quotationline.

Once a link between a BusinessNxt Orderline and a WebCRM Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Orderline and a WebCRM Quotationline:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Orderline Property
     - WebCRM Quotationline Property
     - WebCRM Data Type


BusinessNxt Product to WebCRM Products
--------------------------------------
Every BusinessNxt Product will be synchronized with a WebCRM Products.

Once a link between a BusinessNxt Product and a WebCRM Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Product and a WebCRM Products:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Product Property
     - WebCRM Products Property
     - WebCRM Data Type
   * - priceQuantity
     - ProductPrice
     - "string"
   * - quantityPerUnit
     - ProductQuantity
     - "string"

