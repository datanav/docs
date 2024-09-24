=================================
PowerOffice GO to WebCRM Dataflow
=================================

Generated: 2024-09-24 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to WebCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice GO Customers to WebCRM Organisations
------------------------------------------------
Every PowerOffice GO Customers will be synchronized with a WebCRM Organisations.

Once a link between a PowerOffice GO Customers and a WebCRM Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a WebCRM Organisations:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - WebCRM Organisations Property
     - WebCRM Data Type
   * - Name
     - OrganisationName
     - "string"
   * - PhoneNumber
     - OrganisationTelephone
     - "string"


PowerOffice GO Departments to WebCRM Organisations
--------------------------------------------------
Every PowerOffice GO Departments will be synchronized with a WebCRM Organisations.

Once a link between a PowerOffice GO Departments and a WebCRM Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Departments and a WebCRM Organisations:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Departments Property
     - WebCRM Organisations Property
     - WebCRM Data Type
   * - Name
     - OrganisationName
     - "string"


PowerOffice GO Contactperson to WebCRM Persons
----------------------------------------------
Every PowerOffice GO Contactperson will be synchronized with a WebCRM Persons.

Once a link between a PowerOffice GO Contactperson and a WebCRM Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a WebCRM Persons:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - WebCRM Persons Property
     - WebCRM Data Type
   * - dateOfBirth
     - document_number
     - "string"
   * - emailAddress
     - PersonEmail
     - "string"
   * - firstName
     - PersonFirstName
     - "string"
   * - lastName
     - PersonLastName
     - "string"
   * - partyId
     - PersonOrganisationId
     - "string"
   * - phoneNumber
     - PersonDirectPhone
     - "string"


PowerOffice GO Product to WebCRM Products
-----------------------------------------
Every PowerOffice GO Product will be synchronized with a WebCRM Products.

Once a link between a PowerOffice GO Product and a WebCRM Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Product and a WebCRM Products:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Product Property
     - WebCRM Products Property
     - WebCRM Data Type
   * - availableStock
     - ProductQuantity
     - "string"
   * - costPrice
     - ProductCostPrice
     - "string"
   * - salesPrice
     - ProductPrice
     - "string"
   * - vatCode
     - ProductVatCode
     - "string"


PowerOffice GO Salesorderlines to WebCRM Quotationline
------------------------------------------------------
Every PowerOffice GO Salesorderlines will be synchronized with a WebCRM Quotationline.

Once a link between a PowerOffice GO Salesorderlines and a WebCRM Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Salesorderlines and a WebCRM Quotationline:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Salesorderlines Property
     - WebCRM Quotationline Property
     - WebCRM Data Type


PowerOffice GO Suppliers (human data) to WebCRM Persons
-------------------------------------------------------
Every PowerOffice GO Suppliers (human data) will be synchronized with a WebCRM Persons.

Once a link between a PowerOffice GO Suppliers (human data) and a WebCRM Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Suppliers (human data) and a WebCRM Persons:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Suppliers (human data) Property
     - WebCRM Persons Property
     - WebCRM Data Type
   * - DateOfBirth
     - document_number
     - "string"
   * - EmailAddress
     - PersonEmail
     - "string"
   * - FirstName
     - PersonFirstName
     - "string"
   * - LastName
     - PersonLastName
     - "string"
   * - PhoneNumber
     - PersonDirectPhone
     - "string"

