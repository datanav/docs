================================
Webcrm to Powerofficego Dataflow
================================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Webcrm to Powerofficego. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Webcrm Persons to Powerofficego Contactperson
---------------------------------------------
Every Webcrm Persons will be synchronized with a Powerofficego Contactperson.

Once a link between a Webcrm Persons and a Powerofficego Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Persons and a Powerofficego Contactperson:

.. list-table::
   :header-rows: 1

   * - Webcrm Persons Property
     - Powerofficego Contactperson Property
     - Powerofficego Data Type
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


Webcrm Products to Powerofficego Product
----------------------------------------
Every Webcrm Products will be synchronized with a Powerofficego Product.

Once a link between a Webcrm Products and a Powerofficego Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Products and a Powerofficego Product:

.. list-table::
   :header-rows: 1

   * - Webcrm Products Property
     - Powerofficego Product Property
     - Powerofficego Data Type
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


Webcrm Quotationline to Powerofficego Salesorderlines
-----------------------------------------------------
Every Webcrm Quotationline will be synchronized with a Powerofficego Salesorderlines.

Once a link between a Webcrm Quotationline and a Powerofficego Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Quotationline and a Powerofficego Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Webcrm Quotationline Property
     - Powerofficego Salesorderlines Property
     - Powerofficego Data Type

