================================
Powerofficego to Webcrm Dataflow
================================

Generated: 2024-09-07 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Webcrm. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customers to Webcrm Organisations
-----------------------------------------------
Every Powerofficego Customers will be synchronized with a Webcrm Organisations.

Once a link between a Powerofficego Customers and a Webcrm Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Webcrm Organisations:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Webcrm Organisations Property
     - Webcrm Data Type
   * - Name
     - OrganisationName
     - "string"
   * - PhoneNumber
     - OrganisationTelephone
     - "string"


Powerofficego Departments to Webcrm Organisations
-------------------------------------------------
Every Powerofficego Departments will be synchronized with a Webcrm Organisations.

Once a link between a Powerofficego Departments and a Webcrm Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a Webcrm Organisations:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - Webcrm Organisations Property
     - Webcrm Data Type
   * - Name
     - OrganisationName
     - "string"


Powerofficego Contactperson to Webcrm Persons
---------------------------------------------
Every Powerofficego Contactperson will be synchronized with a Webcrm Persons.

Once a link between a Powerofficego Contactperson and a Webcrm Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Webcrm Persons:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Webcrm Persons Property
     - Webcrm Data Type
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


Powerofficego Product to Webcrm Products
----------------------------------------
Every Powerofficego Product will be synchronized with a Webcrm Products.

Once a link between a Powerofficego Product and a Webcrm Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a Webcrm Products:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - Webcrm Products Property
     - Webcrm Data Type
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


Powerofficego Salesorderlines to Webcrm Quotationline
-----------------------------------------------------
Every Powerofficego Salesorderlines will be synchronized with a Webcrm Quotationline.

Once a link between a Powerofficego Salesorderlines and a Webcrm Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderlines and a Webcrm Quotationline:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderlines Property
     - Webcrm Quotationline Property
     - Webcrm Data Type
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


Powerofficego Suppliers person to Webcrm Persons
------------------------------------------------
Every Powerofficego Suppliers person will be synchronized with a Webcrm Persons.

Once a link between a Powerofficego Suppliers person and a Webcrm Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers person and a Webcrm Persons:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers person Property
     - Webcrm Persons Property
     - Webcrm Data Type
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

