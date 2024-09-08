===========================
Invoiced to Webcrm Dataflow
===========================

Generated: 2024-09-08 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to Webcrm. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Customers company to Webcrm Organisations
--------------------------------------------------
Every Invoiced Customers company will be synchronized with a Webcrm Organisations.

Once a link between a Invoiced Customers company and a Webcrm Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers company and a Webcrm Organisations:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers company Property
     - Webcrm Organisations Property
     - Webcrm Data Type
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


Invoiced Contacts to Webcrm Persons
-----------------------------------
Every Invoiced Contacts will be synchronized with a Webcrm Persons.

Once a link between a Invoiced Contacts and a Webcrm Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Contacts and a Webcrm Persons:

.. list-table::
   :header-rows: 1

   * - Invoiced Contacts Property
     - Webcrm Persons Property
     - Webcrm Data Type


Invoiced Items to Webcrm Products
---------------------------------
Every Invoiced Items will be synchronized with a Webcrm Products.

Once a link between a Invoiced Items and a Webcrm Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Items and a Webcrm Products:

.. list-table::
   :header-rows: 1

   * - Invoiced Items Property
     - Webcrm Products Property
     - Webcrm Data Type
   * - unit_cost
     - ProductCostPrice
     - "string"


Invoiced Lineitem to Webcrm Quotationline
-----------------------------------------
Every Invoiced Lineitem will be synchronized with a Webcrm Quotationline.

Once a link between a Invoiced Lineitem and a Webcrm Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Lineitem and a Webcrm Quotationline:

.. list-table::
   :header-rows: 1

   * - Invoiced Lineitem Property
     - Webcrm Quotationline Property
     - Webcrm Data Type

