=======================
Keap to WebCRM Dataflow
=======================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Keap to WebCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Keap Companies to WebCRM Organisations
--------------------------------------
Every Keap Companies will be synchronized with a WebCRM Organisations.

Once a link between a Keap Companies and a WebCRM Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Companies and a WebCRM Organisations:

.. list-table::
   :header-rows: 1

   * - Keap Companies Property
     - WebCRM Organisations Property
     - WebCRM Data Type
   * - company_name
     - OrganisationName
     - "string"


Keap Opportunity to WebCRM Opportunities
----------------------------------------
Every Keap Opportunity will be synchronized with a WebCRM Opportunities.

Once a link between a Keap Opportunity and a WebCRM Opportunities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Opportunity and a WebCRM Opportunities:

.. list-table::
   :header-rows: 1

   * - Keap Opportunity Property
     - WebCRM Opportunities Property
     - WebCRM Data Type


Keap Product to WebCRM Products
-------------------------------
Every Keap Product will be synchronized with a WebCRM Products.

Once a link between a Keap Product and a WebCRM Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Product and a WebCRM Products:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     - WebCRM Products Property
     - WebCRM Data Type
   * - product_price
     - ProductPrice
     - "string"


Keap Users to WebCRM Users
--------------------------
Every Keap Users will be synchronized with a WebCRM Users.

Once a link between a Keap Users and a WebCRM Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Users and a WebCRM Users:

.. list-table::
   :header-rows: 1

   * - Keap Users Property
     - WebCRM Users Property
     - WebCRM Data Type
   * - email_address
     - UserEmail
     - "string"
   * - job_title
     - UserTitle
     - "string"

