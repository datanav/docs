=======================
Keap to Webcrm Dataflow
=======================

Generated: 2024-09-08 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Keap to Webcrm. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Keap Companies to Webcrm Organisations
--------------------------------------
Every Keap Companies will be synchronized with a Webcrm Organisations.

Once a link between a Keap Companies and a Webcrm Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Companies and a Webcrm Organisations:

.. list-table::
   :header-rows: 1

   * - Keap Companies Property
     - Webcrm Organisations Property
     - Webcrm Data Type
   * - company_name
     - OrganisationName
     - "string"


Keap Opportunity to Webcrm Opportunities
----------------------------------------
Every Keap Opportunity will be synchronized with a Webcrm Opportunities.

Once a link between a Keap Opportunity and a Webcrm Opportunities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Opportunity and a Webcrm Opportunities:

.. list-table::
   :header-rows: 1

   * - Keap Opportunity Property
     - Webcrm Opportunities Property
     - Webcrm Data Type


Keap Product to Webcrm Products
-------------------------------
Every Keap Product will be synchronized with a Webcrm Products.

Once a link between a Keap Product and a Webcrm Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Product and a Webcrm Products:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     - Webcrm Products Property
     - Webcrm Data Type
   * - product_price
     - ProductPrice
     - "string"


Keap Users to Webcrm Users
--------------------------
Every Keap Users will be synchronized with a Webcrm Users.

Once a link between a Keap Users and a Webcrm Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Users and a Webcrm Users:

.. list-table::
   :header-rows: 1

   * - Keap Users Property
     - Webcrm Users Property
     - Webcrm Data Type
   * - email_address
     - UserEmail
     - "string"
   * - job_title
     - UserTitle
     - "string"

