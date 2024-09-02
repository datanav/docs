============================
Businesscentral to  Dataflow
============================

Generated: 2024-09-02 08:11:38

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Companies to  Organisations
-------------------------------------------
Every Businesscentral Companies will be synchronized with a  Organisations.

Once a link between a Businesscentral Companies and a  Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Companies and a  Organisations:

.. list-table::
   :header-rows: 1

   * - Businesscentral Companies Property
     -  Organisations Property
     -  Data Type


Businesscentral Customers company to  Organisations
---------------------------------------------------
Every Businesscentral Customers company will be synchronized with a  Organisations.

Once a link between a Businesscentral Customers company and a  Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a  Organisations:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     -  Organisations Property
     -  Data Type
   * - displayName
     - OrganisationName
     - "string"
   * - phoneNumber
     - OrganisationTelephone
     - "string"


Businesscentral Contacts person to  Persons
-------------------------------------------
Every Businesscentral Contacts person will be synchronized with a  Persons.

Once a link between a Businesscentral Contacts person and a  Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a  Persons:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     -  Persons Property
     -  Data Type
   * - displayName
     - PersonName
     - "string"
   * - mobilePhoneNumber
     - PersonMobilePhone
     - "string"
   * - phoneNumber
     - PersonDirectPhone
     - "string"


Businesscentral Items to  Products
----------------------------------
Every Businesscentral Items will be synchronized with a  Products.

Once a link between a Businesscentral Items and a  Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a  Products:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     -  Products Property
     -  Data Type
   * - inventory
     - ProductQuantity
     - "string"
   * - unitCost
     - ProductCostPrice
     - "string"
   * - unitPrice
     - ProductPrice
     - "string"


Businesscentral Salesorderlines to  Quotationline
-------------------------------------------------
Every Businesscentral Salesorderlines will be synchronized with a  Quotationline.

Once a link between a Businesscentral Salesorderlines and a  Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorderlines and a  Quotationline:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorderlines Property
     -  Quotationline Property
     -  Data Type
   * - discountPercent
     - QuotationLineDiscount
     - "string"
   * - documentId
     - QuotationLineOpportunityId
     - "string"
   * - quantity
     - QuotationLineQuantity
     - "string"
   * - taxPercent
     - QuotationLineVatPercentage
     - "string"
   * - unitPrice
     - QuotationLinePrice
     - "string"

