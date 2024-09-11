==============================
Salesforce to HubSpot Dataflow
==============================

Generated: 2024-09-11 07:56:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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
   * - Name	
     - properties.name
     - "string"
   * - Phone
     - properties.phone
     - "string"
   * - Phone	
     - properties.phone
     - "string"


Salesforce Seller to Hubspot Contact
------------------------------------
Every Salesforce Seller will be synchronized with a Hubspot Contact.

Once a link between a Salesforce Seller and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Seller and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - Salesforce Seller Property
     - Hubspot Contact Property
     - Hubspot Data Type


Salesforce User to Hubspot Contact
----------------------------------
Every Salesforce User will be synchronized with a Hubspot Contact.

Once a link between a Salesforce User and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - Hubspot Contact Property
     - Hubspot Data Type
   * - City
     - properties.city
     - "string"
   * - Country
     - properties.country
     - "string"
   * - Email
     - properties.email
     - "string"
   * - FirstName
     - properties.firstname
     - "string"
   * - ID
     - id
     - "string"
   * - LastName
     - properties.lastname
     - "string"
   * - MobilePhone
     - properties.mobilephone
     - "string"
   * - PostalCode
     - properties.zip
     - "string"
   * - Street
     - properties.address
     - "string"


Salesforce Invoiceline to HubSpot Lineitem
------------------------------------------
Every Salesforce Invoiceline will be synchronized with a HubSpot Lineitem.

Once a link between a Salesforce Invoiceline and a HubSpot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a HubSpot Lineitem:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - HubSpot Lineitem Property
     - HubSpot Data Type
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


Salesforce Orderitem to HubSpot Lineitem
----------------------------------------
Every Salesforce Orderitem will be synchronized with a HubSpot Lineitem.

Once a link between a Salesforce Orderitem and a HubSpot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a HubSpot Lineitem:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - HubSpot Lineitem Property
     - HubSpot Data Type
   * - Quantity
     - properties.quantity
     - N/A
   * - TotalPrice
     - properties.price
     - "string"


Salesforce Product2 to HubSpot Product
--------------------------------------
Every Salesforce Product2 will be synchronized with a HubSpot Product.

Once a link between a Salesforce Product2 and a HubSpot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a HubSpot Product:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - HubSpot Product Property
     - HubSpot Data Type
   * - Description
     - properties.description
     - "string"
   * - Description	
     - properties.description
     - "string"
   * - Name
     - properties.name
     - "string"
   * - Name	
     - properties.name
     - "string"


Salesforce Quote to HubSpot Quote
---------------------------------
Every Salesforce Quote will be synchronized with a HubSpot Quote.

Once a link between a Salesforce Quote and a HubSpot Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quote and a HubSpot Quote:

.. list-table::
   :header-rows: 1

   * - Salesforce Quote Property
     - HubSpot Quote Property
     - HubSpot Data Type
   * - Name
     - properties.hs_title
     - "string"


Salesforce Quotelineitem to HubSpot Lineitem
--------------------------------------------
Every Salesforce Quotelineitem will be synchronized with a HubSpot Lineitem.

Once a link between a Salesforce Quotelineitem and a HubSpot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a HubSpot Lineitem:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - HubSpot Lineitem Property
     - HubSpot Data Type
   * - Description
     - properties.description
     - "string"
   * - Discount
     - properties.hs_discount_percentage
     - "string"
   * - Quantity
     - properties.quantity
     - N/A
   * - TotalPriceWithTax
     - properties.price
     - "string"

