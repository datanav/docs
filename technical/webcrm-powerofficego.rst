=================================
WebCRM to PowerOffice GO Dataflow
=================================

Generated: 2024-09-14 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WebCRM to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WebCRM Persons to PowerOffice GO Contactperson
----------------------------------------------
Every WebCRM Persons will be synchronized with a PowerOffice GO Contactperson.

Once a link between a WebCRM Persons and a PowerOffice GO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Persons and a PowerOffice GO Contactperson:

.. list-table::
   :header-rows: 1

   * - WebCRM Persons Property
     - PowerOffice GO Contactperson Property
     - PowerOffice GO Data Type
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


WebCRM Products to PowerOffice GO Product
-----------------------------------------
Every WebCRM Products will be synchronized with a PowerOffice GO Product.

Once a link between a WebCRM Products and a PowerOffice GO Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Products and a PowerOffice GO Product:

.. list-table::
   :header-rows: 1

   * - WebCRM Products Property
     - PowerOffice GO Product Property
     - PowerOffice GO Data Type
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


WebCRM Quotationline to PowerOffice GO Salesorderlines
------------------------------------------------------
Every WebCRM Quotationline will be synchronized with a PowerOffice GO Salesorderlines.

Once a link between a WebCRM Quotationline and a PowerOffice GO Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Quotationline and a PowerOffice GO Salesorderlines:

.. list-table::
   :header-rows: 1

   * - WebCRM Quotationline Property
     - PowerOffice GO Salesorderlines Property
     - PowerOffice GO Data Type

