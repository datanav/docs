=================================
WebCRM to PowerOffice GO Dataflow
=================================

Generated: 2024-09-11 07:53:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WebCRM to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WebCRM Persons to PowerOffice Contactperson
-------------------------------------------
Every WebCRM Persons will be synchronized with a PowerOffice Contactperson.

Once a link between a WebCRM Persons and a PowerOffice Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Persons and a PowerOffice Contactperson:

.. list-table::
   :header-rows: 1

   * - WebCRM Persons Property
     - PowerOffice Contactperson Property
     - PowerOffice Data Type
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


WebCRM Products to PowerOffice Product
--------------------------------------
Every WebCRM Products will be synchronized with a PowerOffice Product.

Once a link between a WebCRM Products and a PowerOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Products and a PowerOffice Product:

.. list-table::
   :header-rows: 1

   * - WebCRM Products Property
     - PowerOffice Product Property
     - PowerOffice Data Type
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


WebCRM Quotationline to PowerOffice Salesorderlines
---------------------------------------------------
Every WebCRM Quotationline will be synchronized with a PowerOffice Salesorderlines.

Once a link between a WebCRM Quotationline and a PowerOffice Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Quotationline and a PowerOffice Salesorderlines:

.. list-table::
   :header-rows: 1

   * - WebCRM Quotationline Property
     - PowerOffice Salesorderlines Property
     - PowerOffice Data Type

