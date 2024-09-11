================================
WebCRM to PowerOfficeGO Dataflow
================================

Generated: 2024-09-11 08:38:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WebCRM to PowerOfficeGO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WebCRM Persons to PowerOfficeGO Contactperson
---------------------------------------------
Every WebCRM Persons will be synchronized with a PowerOfficeGO Contactperson.

Once a link between a WebCRM Persons and a PowerOfficeGO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Persons and a PowerOfficeGO Contactperson:

.. list-table::
   :header-rows: 1

   * - WebCRM Persons Property
     - PowerOfficeGO Contactperson Property
     - PowerOfficeGO Data Type
   * - PersonDirectPhone
     - phoneNumber
     - "string"
   * - PersonFirstName
     - firstName
     - "string"
   * - PersonLastName
     - lastName
     - "string"
   * - PersonOrganisationId
     - partyId
     - "integer"
   * - document_number
     - dateOfBirth
     - N/A


WebCRM Products to PowerOfficeGO Product
----------------------------------------
Every WebCRM Products will be synchronized with a PowerOfficeGO Product.

Once a link between a WebCRM Products and a PowerOfficeGO Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Products and a PowerOfficeGO Product:

.. list-table::
   :header-rows: 1

   * - WebCRM Products Property
     - PowerOfficeGO Product Property
     - PowerOfficeGO Data Type
   * - ProductCostPrice
     - costPrice
     - N/A
   * - ProductPrice
     - salesPrice
     - N/A
   * - ProductQuantity
     - availableStock
     - "integer"
   * - ProductVatCode
     - vatCode
     - "string"


WebCRM Quotationline to PowerOfficeGO Salesorderlines
-----------------------------------------------------
Every WebCRM Quotationline will be synchronized with a PowerOfficeGO Salesorderlines.

Once a link between a WebCRM Quotationline and a PowerOfficeGO Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Quotationline and a PowerOfficeGO Salesorderlines:

.. list-table::
   :header-rows: 1

   * - WebCRM Quotationline Property
     - PowerOfficeGO Salesorderlines Property
     - PowerOfficeGO Data Type

