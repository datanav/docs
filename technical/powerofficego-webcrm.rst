================================
PowerOfficeGO to WebCRM Dataflow
================================

Generated: 2024-09-11 08:49:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOfficeGO to WebCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice Customers to WebCRM Organisations
---------------------------------------------
Every PowerOffice Customers will be synchronized with a WebCRM Organisations.

Once a link between a PowerOffice Customers and a WebCRM Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Customers and a WebCRM Organisations:

.. list-table::
   :header-rows: 1

   * - PowerOffice Customers Property
     - WebCRM Organisations Property
     - WebCRM Data Type
   * - Name
     - OrganisationName
     - "string"
   * - PhoneNumber
     - OrganisationTelephone
     - "string"


PowerOffice Departments to WebCRM Organisations
-----------------------------------------------
Every PowerOffice Departments will be synchronized with a WebCRM Organisations.

Once a link between a PowerOffice Departments and a WebCRM Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Departments and a WebCRM Organisations:

.. list-table::
   :header-rows: 1

   * - PowerOffice Departments Property
     - WebCRM Organisations Property
     - WebCRM Data Type
   * - Name
     - OrganisationName
     - "string"


PowerOfficeGO Contactperson to WebCRM Persons
---------------------------------------------
Every PowerOfficeGO Contactperson will be synchronized with a WebCRM Persons.

Once a link between a PowerOfficeGO Contactperson and a WebCRM Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Contactperson and a WebCRM Persons:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Contactperson Property
     - WebCRM Persons Property
     - WebCRM Data Type
   * - dateOfBirth
     - document_number
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


PowerOfficeGO Product to WebCRM Products
----------------------------------------
Every PowerOfficeGO Product will be synchronized with a WebCRM Products.

Once a link between a PowerOfficeGO Product and a WebCRM Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Product and a WebCRM Products:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Product Property
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


PowerOfficeGO Salesorderlines to WebCRM Quotationline
-----------------------------------------------------
Every PowerOfficeGO Salesorderlines will be synchronized with a WebCRM Quotationline.

Once a link between a PowerOfficeGO Salesorderlines and a WebCRM Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Salesorderlines and a WebCRM Quotationline:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Salesorderlines Property
     - WebCRM Quotationline Property
     - WebCRM Data Type
   * - Allowance
     - QuotationLineDiscount
     - "string"
   * - ProductUnitCost
     - QuotationLineCostPrice
     - "string"
   * - ProductUnitPrice
     - QuotationLinePrice
     - "string"
   * - Quantity
     - QuotationLineQuantity
     - "string"
   * - VatRate
     - QuotationLineVatPercentage
     - "string"
   * - sesam_SalesOrderId
     - QuotationLineOpportunityId
     - "string"


PowerOfficeGO Suppliers person to WebCRM Persons
------------------------------------------------
Every PowerOfficeGO Suppliers person will be synchronized with a WebCRM Persons.

Once a link between a PowerOfficeGO Suppliers person and a WebCRM Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Suppliers person and a WebCRM Persons:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Suppliers person Property
     - WebCRM Persons Property
     - WebCRM Data Type
   * - DateOfBirth
     - document_number
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

