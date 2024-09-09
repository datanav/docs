==============================
Salesforce to Hubspot Dataflow
==============================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Hubspot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Contact to Hubspot Contact
-------------------------------------
Every Salesforce Contact will be synchronized with a Hubspot Contact.

Once a link between a Salesforce Contact and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - Hubspot Contact Property
     - Hubspot Data Type
   * - Birthdate
     - properties.date_of_birth
     - "string"
   * - Email
     - properties.email
     - "string"
   * - FirstName
     - properties.firstname
     - "string"
   * - HomePhone
     - properties.phone
     - "string"
   * - LastName
     - properties.lastname
     - "string"
   * - MobilePhone
     - properties.mobilephone
     - "string"
   * - Phone
     - properties.phone
     - "string"


Salesforce Customer to Hubspot Contact
--------------------------------------
Every Salesforce Customer will be synchronized with a Hubspot Contact.

Once a link between a Salesforce Customer and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - Hubspot Contact Property
     - Hubspot Data Type


Salesforce Division to Hubspot Company
--------------------------------------
Every Salesforce Division will be synchronized with a Hubspot Company.

Once a link between a Salesforce Division and a Hubspot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Division and a Hubspot Company:

.. list-table::
   :header-rows: 1

   * - Salesforce Division Property
     - Hubspot Company Property
     - Hubspot Data Type
   * - Name
     - properties.name
     - "string"


Salesforce Organization to Hubspot Company
------------------------------------------
Every Salesforce Organization will be synchronized with a Hubspot Company.

Once a link between a Salesforce Organization and a Hubspot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Hubspot Company:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Hubspot Company Property
     - Hubspot Data Type
   * - Name	
     - properties.name
     - "string"
   * - Phone	
     - properties.phone
     - "string"


Salesforce Invoiceline to Hubspot Lineitem
------------------------------------------
Every Salesforce Invoiceline will be synchronized with a Hubspot Lineitem.

Once a link between a Salesforce Invoiceline and a Hubspot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a Hubspot Lineitem:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - Hubspot Lineitem Property
     - Hubspot Data Type
   * - Description
     - properties.description
     - "string"
   * - Name
     - properties.name
     - "string"
   * - Quantity
     - properties.quantity
     - N/A
   * - UnitPrice
     - properties.price
     - "string"


Salesforce Product2 to Hubspot Product
--------------------------------------
Every Salesforce Product2 will be synchronized with a Hubspot Product.

Once a link between a Salesforce Product2 and a Hubspot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Hubspot Product:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Hubspot Product Property
     - Hubspot Data Type
   * - Description	
     - properties.description
     - "string"
   * - Name	
     - properties.name
     - "string"

