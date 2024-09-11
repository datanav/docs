=============================
WebCRM to MemberCare Dataflow
=============================

Generated: 2024-09-11 08:07:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WebCRM to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WebCRM Opportunities to Membercare Invoices
-------------------------------------------
Every WebCRM Opportunities will be synchronized with a Membercare Invoices.

Once a link between a WebCRM Opportunities and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Opportunities and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - WebCRM Opportunities Property
     - Membercare Invoices Property
     - Membercare Data Type


WebCRM Organisations to Membercare Companies
--------------------------------------------
Every WebCRM Organisations will be synchronized with a Membercare Companies.

Once a link between a WebCRM Organisations and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Organisations and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - WebCRM Organisations Property
     - Membercare Companies Property
     - Membercare Data Type
   * - OrganisationName
     - companyName
     - "string"


WebCRM Persons to Membercare Persons
------------------------------------
Every WebCRM Persons will be synchronized with a Membercare Persons.

Once a link between a WebCRM Persons and a Membercare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Persons and a Membercare Persons:

.. list-table::
   :header-rows: 1

   * - WebCRM Persons Property
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


WebCRM Products to Membercare Products
--------------------------------------
Every WebCRM Products will be synchronized with a Membercare Products.

Once a link between a WebCRM Products and a Membercare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Products and a Membercare Products:

.. list-table::
   :header-rows: 1

   * - WebCRM Products Property
     - Membercare Products Property
     - Membercare Data Type


WebCRM Quotationline to Membercare Invoices
-------------------------------------------
Every WebCRM Quotationline will be synchronized with a Membercare Invoices.

Once a link between a WebCRM Quotationline and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Quotationline and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - WebCRM Quotationline Property
     - Membercare Invoices Property
     - Membercare Data Type


WebCRM Users to Membercare Persons
----------------------------------
Every WebCRM Users will be synchronized with a Membercare Persons.

Once a link between a WebCRM Users and a Membercare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Users and a Membercare Persons:

.. list-table::
   :header-rows: 1

   * - WebCRM Users Property
     - Membercare Persons Property
     - Membercare Data Type


WebCRM Organisations to MemberCare Countries
--------------------------------------------
Every WebCRM Organisations will be synchronized with a MemberCare Countries.

Once a link between a WebCRM Organisations and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Organisations and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - WebCRM Organisations Property
     - MemberCare Countries Property
     - MemberCare Data Type
   * - OrganisationCountryData
     - iso2Letter
     - "string"
   * - OrganisationCountryData
     - name
     - "string"
   * - OrganisationCountryData.CodeISO
     - iso2Letter
     - "string"
   * - OrganisationCountryData.Name
     - name
     - "string"

