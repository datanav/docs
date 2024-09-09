=============================
Salesforce to Webcrm Dataflow
=============================

Generated: 2024-09-09 13:32:29

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Webcrm. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Division to Webcrm Organisations
-------------------------------------------
Every Salesforce Division will be synchronized with a Webcrm Organisations.

Once a link between a Salesforce Division and a Webcrm Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Division and a Webcrm Organisations:

.. list-table::
   :header-rows: 1

   * - Salesforce Division Property
     - Webcrm Organisations Property
     - Webcrm Data Type
   * - Name
     - OrganisationName
     - "string"


Salesforce Organization to Webcrm Organisations
-----------------------------------------------
Every Salesforce Organization will be synchronized with a Webcrm Organisations.

Once a link between a Salesforce Organization and a Webcrm Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Webcrm Organisations:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Webcrm Organisations Property
     - Webcrm Data Type
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


Salesforce Contact to Webcrm Persons
------------------------------------
Every Salesforce Contact will be synchronized with a Webcrm Persons.

Once a link between a Salesforce Contact and a Webcrm Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a Webcrm Persons:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - Webcrm Persons Property
     - Webcrm Data Type
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


Salesforce Invoiceline to Webcrm Quotationline
----------------------------------------------
Every Salesforce Invoiceline will be synchronized with a Webcrm Quotationline.

Once a link between a Salesforce Invoiceline and a Webcrm Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a Webcrm Quotationline:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - Webcrm Quotationline Property
     - Webcrm Data Type
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


Salesforce Orderitem to Webcrm Quotationline
--------------------------------------------
Every Salesforce Orderitem will be synchronized with a Webcrm Quotationline.

Once a link between a Salesforce Orderitem and a Webcrm Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a Webcrm Quotationline:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - Webcrm Quotationline Property
     - Webcrm Data Type


Salesforce Product2 to Webcrm Products
--------------------------------------
Every Salesforce Product2 will be synchronized with a Webcrm Products.

Once a link between a Salesforce Product2 and a Webcrm Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Webcrm Products:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Webcrm Products Property
     - Webcrm Data Type


Salesforce Quotelineitem to Webcrm Quotationline
------------------------------------------------
Every Salesforce Quotelineitem will be synchronized with a Webcrm Quotationline.

Once a link between a Salesforce Quotelineitem and a Webcrm Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a Webcrm Quotationline:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - Webcrm Quotationline Property
     - Webcrm Data Type

