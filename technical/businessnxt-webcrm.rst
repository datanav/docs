===============================
Business Nxt to WebCRM Dataflow
===============================

Generated: 2024-09-12 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Nxt to WebCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Nxt Address to WebCRM Organisations
--------------------------------------------
Every Business Nxt Address will be synchronized with a WebCRM Organisations.

Once a link between a Business Nxt Address and a WebCRM Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Address and a WebCRM Organisations:

.. list-table::
   :header-rows: 1

   * - Business Nxt Address Property
     - WebCRM Organisations Property
     - WebCRM Data Type
   * - name
     - OrganisationName
     - "string"
   * - phone
     - OrganisationTelephone
     - "string"


Business Nxt Company to WebCRM Organisations
--------------------------------------------
Every Business Nxt Company will be synchronized with a WebCRM Organisations.

Once a link between a Business Nxt Company and a WebCRM Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Company and a WebCRM Organisations:

.. list-table::
   :header-rows: 1

   * - Business Nxt Company Property
     - WebCRM Organisations Property
     - WebCRM Data Type
   * - name
     - OrganisationName
     - "string"


Business Nxt Orderline to WebCRM Quotationline
----------------------------------------------
Every Business Nxt Orderline will be synchronized with a WebCRM Quotationline.

Once a link between a Business Nxt Orderline and a WebCRM Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Orderline and a WebCRM Quotationline:

.. list-table::
   :header-rows: 1

   * - Business Nxt Orderline Property
     - WebCRM Quotationline Property
     - WebCRM Data Type


Business Nxt Product to WebCRM Products
---------------------------------------
Every Business Nxt Product will be synchronized with a WebCRM Products.

Once a link between a Business Nxt Product and a WebCRM Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Product and a WebCRM Products:

.. list-table::
   :header-rows: 1

   * - Business Nxt Product Property
     - WebCRM Products Property
     - WebCRM Data Type
   * - priceQuantity
     - ProductPrice
     - "string"
   * - quantityPerUnit
     - ProductQuantity
     - "string"

