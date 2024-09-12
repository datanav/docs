=======================
WebCRM to Keap Dataflow
=======================

Generated: 2024-09-12 13:14:11

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WebCRM to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WebCRM Organisations to Keap Companies
--------------------------------------
Every WebCRM Organisations will be synchronized with a Keap Companies.

Once a link between a WebCRM Organisations and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Organisations and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - WebCRM Organisations Property
     - Keap Companies Property
     - Keap Data Type
   * - OrganisationName
     - company_name
     - "string"


WebCRM Persons to Keap Contacts
-------------------------------
Every WebCRM Persons will be synchronized with a Keap Contacts.

Once a link between a WebCRM Persons and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Persons and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - WebCRM Persons Property
     - Keap Contacts Property
     - Keap Data Type
   * - PersonTitle
     - job_title
     - "string"
   * - document_number
     - birthday
     - "string"


WebCRM Users to Keap Contacts
-----------------------------
Every WebCRM Users will be synchronized with a Keap Contacts.

Once a link between a WebCRM Users and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Users and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - WebCRM Users Property
     - Keap Contacts Property
     - Keap Data Type
   * - UserTitle
     - job_title
     - "string"


WebCRM Opportunities to Keap Opportunity
----------------------------------------
Every WebCRM Opportunities will be synchronized with a Keap Opportunity.

Once a link between a WebCRM Opportunities and a Keap Opportunity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Opportunities and a Keap Opportunity:

.. list-table::
   :header-rows: 1

   * - WebCRM Opportunities Property
     - Keap Opportunity Property
     - Keap Data Type


WebCRM Products to Keap Product
-------------------------------
Every WebCRM Products will be synchronized with a Keap Product.

Once a link between a WebCRM Products and a Keap Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Products and a Keap Product:

.. list-table::
   :header-rows: 1

   * - WebCRM Products Property
     - Keap Product Property
     - Keap Data Type
   * - ProductPrice
     - product_price
     - "string"

