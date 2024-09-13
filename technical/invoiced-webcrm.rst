===========================
Invoiced to WebCRM Dataflow
===========================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to WebCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Customers company to WebCRM Organisations
--------------------------------------------------
Every Invoiced Customers company will be synchronized with a WebCRM Organisations.

Once a link between a Invoiced Customers company and a WebCRM Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers company and a WebCRM Organisations:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers company Property
     - WebCRM Organisations Property
     - WebCRM Data Type
   * - address1
     - OrganisationAddress
     - "string"
   * - address1
     - OrganisationDeliveryAddress
     - "string"
   * - city
     - OrganisationCity
     - "string"
   * - city
     - OrganisationDeliveryCity
     - "string"
   * - id
     - OrganisationId
     - "string"
   * - name
     - OrganisationName
     - "string"
   * - postal_code
     - OrganisationDeliveryPostCode
     - "string"
   * - postal_code
     - OrganisationPostCode
     - "string"


Invoiced Contacts to WebCRM Persons
-----------------------------------
Every Invoiced Contacts will be synchronized with a WebCRM Persons.

Once a link between a Invoiced Contacts and a WebCRM Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Contacts and a WebCRM Persons:

.. list-table::
   :header-rows: 1

   * - Invoiced Contacts Property
     - WebCRM Persons Property
     - WebCRM Data Type
   * - name
     - PersonName
     - "string"
   * - phone
     - PersonMobilePhone
     - "string"
   * - title
     - PersonTitle
     - "string"


Invoiced Items to WebCRM Products
---------------------------------
Every Invoiced Items will be synchronized with a WebCRM Products.

Once a link between a Invoiced Items and a WebCRM Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Items and a WebCRM Products:

.. list-table::
   :header-rows: 1

   * - Invoiced Items Property
     - WebCRM Products Property
     - WebCRM Data Type
   * - unit_cost
     - ProductCostPrice
     - "string"


Invoiced Lineitem to WebCRM Quotationline
-----------------------------------------
Every Invoiced Lineitem will be synchronized with a WebCRM Quotationline.

Once a link between a Invoiced Lineitem and a WebCRM Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Lineitem and a WebCRM Quotationline:

.. list-table::
   :header-rows: 1

   * - Invoiced Lineitem Property
     - WebCRM Quotationline Property
     - WebCRM Data Type

