=============================
Salesforce to WebCRM Dataflow
=============================

Generated: 2024-09-14 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to WebCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Division to WebCRM Organisations
-------------------------------------------
Every Salesforce Division will be synchronized with a WebCRM Organisations.

Once a link between a Salesforce Division and a WebCRM Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Division and a WebCRM Organisations:

.. list-table::
   :header-rows: 1

   * - Salesforce Division Property
     - WebCRM Organisations Property
     - WebCRM Data Type
   * - Name
     - OrganisationName
     - "string"


Salesforce Organization to WebCRM Organisations
-----------------------------------------------
Every Salesforce Organization will be synchronized with a WebCRM Organisations.

Once a link between a Salesforce Organization and a WebCRM Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a WebCRM Organisations:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - WebCRM Organisations Property
     - WebCRM Data Type
   * - Name
     - OrganisationName
     - "string"
   * - Name	
     - OrganisationName
     - "string"
   * - Phone
     - OrganisationTelephone
     - "string"
   * - Phone	
     - OrganisationTelephone
     - "string"


Salesforce Contact to WebCRM Persons
------------------------------------
Every Salesforce Contact will be synchronized with a WebCRM Persons.

Once a link between a Salesforce Contact and a WebCRM Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a WebCRM Persons:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - WebCRM Persons Property
     - WebCRM Data Type
   * - Birthdate
     - document_number
     - "string"
   * - FirstName
     - PersonFirstName
     - "string"
   * - LastName
     - PersonLastName
     - "string"
   * - MobilePhone
     - PersonMobilePhone
     - "string"
   * - Phone
     - PersonDirectPhone
     - "string"


Salesforce Invoiceline to WebCRM Quotationline
----------------------------------------------
Every Salesforce Invoiceline will be synchronized with a WebCRM Quotationline.

Once a link between a Salesforce Invoiceline and a WebCRM Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a WebCRM Quotationline:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - WebCRM Quotationline Property
     - WebCRM Data Type
   * - Description
     - QuotationLineCostPrice
     - "string"
   * - Description
     - QuotationLineDiscount
     - "string"
   * - Description
     - QuotationLinePrice
     - "string"
   * - Description
     - QuotationLineQuantity
     - "string"
   * - Description
     - QuotationLineVatPercentage
     - "string"


Salesforce Orderitem to WebCRM Quotationline
--------------------------------------------
Every Salesforce Orderitem will be synchronized with a WebCRM Quotationline.

Once a link between a Salesforce Orderitem and a WebCRM Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a WebCRM Quotationline:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - WebCRM Quotationline Property
     - WebCRM Data Type


Salesforce Product2 to WebCRM Products
--------------------------------------
Every Salesforce Product2 will be synchronized with a WebCRM Products.

Once a link between a Salesforce Product2 and a WebCRM Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a WebCRM Products:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - WebCRM Products Property
     - WebCRM Data Type


Salesforce Quotelineitem to WebCRM Quotationline
------------------------------------------------
Every Salesforce Quotelineitem will be synchronized with a WebCRM Quotationline.

Once a link between a Salesforce Quotelineitem and a WebCRM Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a WebCRM Quotationline:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - WebCRM Quotationline Property
     - WebCRM Data Type

