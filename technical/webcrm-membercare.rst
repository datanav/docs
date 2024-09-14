=============================
WebCRM to MemberCare Dataflow
=============================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WebCRM to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WebCRM Opportunities to MemberCare Invoices
-------------------------------------------
Every WebCRM Opportunities will be synchronized with a MemberCare Invoices.

Once a link between a WebCRM Opportunities and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Opportunities and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - WebCRM Opportunities Property
     - MemberCare Invoices Property
     - MemberCare Data Type


WebCRM Organisations to MemberCare Companies
--------------------------------------------
Every WebCRM Organisations will be synchronized with a MemberCare Companies.

Once a link between a WebCRM Organisations and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Organisations and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - WebCRM Organisations Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - OrganisationName
     - companyName
     - "string"


WebCRM Persons to MemberCare Persons
------------------------------------
Every WebCRM Persons will be synchronized with a MemberCare Persons.

Once a link between a WebCRM Persons and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Persons and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - WebCRM Persons Property
     - MemberCare Persons Property
     - MemberCare Data Type
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


WebCRM Products to MemberCare Products
--------------------------------------
Every WebCRM Products will be synchronized with a MemberCare Products.

Once a link between a WebCRM Products and a MemberCare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Products and a MemberCare Products:

.. list-table::
   :header-rows: 1

   * - WebCRM Products Property
     - MemberCare Products Property
     - MemberCare Data Type


WebCRM Quotationline to MemberCare Invoices
-------------------------------------------
Every WebCRM Quotationline will be synchronized with a MemberCare Invoices.

Once a link between a WebCRM Quotationline and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Quotationline and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - WebCRM Quotationline Property
     - MemberCare Invoices Property
     - MemberCare Data Type


WebCRM Users to MemberCare Persons
----------------------------------
Every WebCRM Users will be synchronized with a MemberCare Persons.

Once a link between a WebCRM Users and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Users and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - WebCRM Users Property
     - MemberCare Persons Property
     - MemberCare Data Type


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

