=============================
Webcrm to Membercare Dataflow
=============================

Generated: 2024-09-07 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Webcrm to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Webcrm Opportunities to Membercare Invoices
-------------------------------------------
Every Webcrm Opportunities will be synchronized with a Membercare Invoices.

Once a link between a Webcrm Opportunities and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Opportunities and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - Webcrm Opportunities Property
     - Membercare Invoices Property
     - Membercare Data Type


Webcrm Organisations to Membercare Companies
--------------------------------------------
Every Webcrm Organisations will be synchronized with a Membercare Companies.

Once a link between a Webcrm Organisations and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Organisations and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Webcrm Organisations Property
     - Membercare Companies Property
     - Membercare Data Type
   * - OrganisationName
     - companyName
     - "string"


Webcrm Persons to Membercare Persons
------------------------------------
Every Webcrm Persons will be synchronized with a Membercare Persons.

Once a link between a Webcrm Persons and a Membercare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Persons and a Membercare Persons:

.. list-table::
   :header-rows: 1

   * - Webcrm Persons Property
     - Membercare Persons Property
     - Membercare Data Type
   * - PersonFirstName
     - firstname
     - "string"
   * - PersonLastName
     - lastname
     - "string"
   * - PersonName
     - name
     - "string"
   * - document_number
     - birthDate
     - "string"


Webcrm Products to Membercare Products
--------------------------------------
Every Webcrm Products will be synchronized with a Membercare Products.

Once a link between a Webcrm Products and a Membercare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Products and a Membercare Products:

.. list-table::
   :header-rows: 1

   * - Webcrm Products Property
     - Membercare Products Property
     - Membercare Data Type


Webcrm Quotationline to Membercare Invoices
-------------------------------------------
Every Webcrm Quotationline will be synchronized with a Membercare Invoices.

Once a link between a Webcrm Quotationline and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Quotationline and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - Webcrm Quotationline Property
     - Membercare Invoices Property
     - Membercare Data Type


Webcrm Users to Membercare Persons
----------------------------------
Every Webcrm Users will be synchronized with a Membercare Persons.

Once a link between a Webcrm Users and a Membercare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Users and a Membercare Persons:

.. list-table::
   :header-rows: 1

   * - Webcrm Users Property
     - Membercare Persons Property
     - Membercare Data Type


Webcrm Organisations to Membercare Countries
--------------------------------------------
Every Webcrm Organisations will be synchronized with a Membercare Countries.

Once a link between a Webcrm Organisations and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Organisations and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - Webcrm Organisations Property
     - Membercare Countries Property
     - Membercare Data Type
   * - OrganisationCountryData
     - iso2Letter
     - "string"
   * - OrganisationCountryData
     - name
     - "string"

