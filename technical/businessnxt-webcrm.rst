==============================
Businessnxt to Webcrm Dataflow
==============================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businessnxt to Webcrm. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businessnxt Address to Webcrm Organisations
-------------------------------------------
Every Businessnxt Address will be synchronized with a Webcrm Organisations.

Once a link between a Businessnxt Address and a Webcrm Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Address and a Webcrm Organisations:

.. list-table::
   :header-rows: 1

   * - Businessnxt Address Property
     - Webcrm Organisations Property
     - Webcrm Data Type
   * - name
     - OrganisationName
     - "string"
   * - phone
     - OrganisationTelephone
     - "string"


Businessnxt Company to Webcrm Organisations
-------------------------------------------
Every Businessnxt Company will be synchronized with a Webcrm Organisations.

Once a link between a Businessnxt Company and a Webcrm Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Company and a Webcrm Organisations:

.. list-table::
   :header-rows: 1

   * - Businessnxt Company Property
     - Webcrm Organisations Property
     - Webcrm Data Type
   * - name
     - OrganisationName
     - "string"


Businessnxt Orderline to Webcrm Quotationline
---------------------------------------------
Every Businessnxt Orderline will be synchronized with a Webcrm Quotationline.

Once a link between a Businessnxt Orderline and a Webcrm Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Orderline and a Webcrm Quotationline:

.. list-table::
   :header-rows: 1

   * - Businessnxt Orderline Property
     - Webcrm Quotationline Property
     - Webcrm Data Type


Businessnxt Product to Webcrm Products
--------------------------------------
Every Businessnxt Product will be synchronized with a Webcrm Products.

Once a link between a Businessnxt Product and a Webcrm Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Product and a Webcrm Products:

.. list-table::
   :header-rows: 1

   * - Businessnxt Product Property
     - Webcrm Products Property
     - Webcrm Data Type
   * - priceQuantity
     - ProductPrice
     - "string"
   * - quantityPerUnit
     - ProductQuantity
     - "string"

