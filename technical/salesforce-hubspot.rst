==============================
Salesforce to HubSpot Dataflow
==============================

Generated: 2024-09-24 00:00:26

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Contact to HubSpot Contact
-------------------------------------
Every Salesforce Contact will be synchronized with a HubSpot Contact.

Once a link between a Salesforce Contact and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - Birthdate
     - properties.date_of_birth
     - "string"
   * - Email
     - properties.email
     - "string"
   * - FirstName
     - properties.firstname
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


Salesforce Customer to HubSpot Contact
--------------------------------------
Every Salesforce Customer will be synchronized with a HubSpot Contact.

Once a link between a Salesforce Customer and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - HubSpot Contact Property
     - HubSpot Data Type


Salesforce Division to HubSpot Company
--------------------------------------
Every Salesforce Division will be synchronized with a HubSpot Company.

Once a link between a Salesforce Division and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Division and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Salesforce Division Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - Name
     - properties.name
     - "string"


Salesforce Organization to HubSpot Company
------------------------------------------
Every Salesforce Organization will be synchronized with a HubSpot Company.

Once a link between a Salesforce Organization and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - Name
     - properties.name
     - "string"
   * - Phone
     - properties.phone
     - "string"


Salesforce Seller to HubSpot Contact
------------------------------------
Every Salesforce Seller will be synchronized with a HubSpot Contact.

Once a link between a Salesforce Seller and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Seller and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Salesforce Seller Property
     - HubSpot Contact Property
     - HubSpot Data Type


Salesforce User to HubSpot Contact
----------------------------------
Every Salesforce User will be synchronized with a HubSpot Contact.

Once a link between a Salesforce User and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - HubSpot Contact Property
     - HubSpot Data Type
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


Salesforce Invoiceline to HubSpot Lineitemdealassociationtype
-------------------------------------------------------------
Every Salesforce Invoiceline will be synchronized with a HubSpot Lineitemdealassociationtype.

Once a link between a Salesforce Invoiceline and a HubSpot Lineitemdealassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a HubSpot Lineitemdealassociationtype:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - HubSpot Lineitemdealassociationtype Property
     - HubSpot Data Type


Salesforce Invoiceline to HubSpot Lineitemquoteassociationtype
--------------------------------------------------------------
Every Salesforce Invoiceline will be synchronized with a HubSpot Lineitemquoteassociationtype.

Once a link between a Salesforce Invoiceline and a HubSpot Lineitemquoteassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a HubSpot Lineitemquoteassociationtype:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - HubSpot Lineitemquoteassociationtype Property
     - HubSpot Data Type


Salesforce Order to HubSpot Deal
--------------------------------
Every Salesforce Order will be synchronized with a HubSpot Deal.

Once a link between a Salesforce Order and a HubSpot Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a HubSpot Deal:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - HubSpot Deal Property
     - HubSpot Data Type
   * - CurrencyIsoCode
     - properties.deal_currency_code
     - "string"
   * - Description
     - properties.description
     - "string"
   * - Name
     - properties.dealname
     - "string"
   * - OrderedDate
     - properties.closedate
     - "string"
   * - TotalAmount
     - properties.amount
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


Salesforce Orderitem to HubSpot Lineitemdealassociationtype
-----------------------------------------------------------
Every Salesforce Orderitem will be synchronized with a HubSpot Lineitemdealassociationtype.

Once a link between a Salesforce Orderitem and a HubSpot Lineitemdealassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a HubSpot Lineitemdealassociationtype:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - HubSpot Lineitemdealassociationtype Property
     - HubSpot Data Type


Salesforce Orderitem to HubSpot Lineitemquoteassociationtype
------------------------------------------------------------
Every Salesforce Orderitem will be synchronized with a HubSpot Lineitemquoteassociationtype.

Once a link between a Salesforce Orderitem and a HubSpot Lineitemquoteassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a HubSpot Lineitemquoteassociationtype:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - HubSpot Lineitemquoteassociationtype Property
     - HubSpot Data Type


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


Salesforce Quotelineitem to HubSpot Lineitemdealassociationtype
---------------------------------------------------------------
Every Salesforce Quotelineitem will be synchronized with a HubSpot Lineitemdealassociationtype.

Once a link between a Salesforce Quotelineitem and a HubSpot Lineitemdealassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a HubSpot Lineitemdealassociationtype:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - HubSpot Lineitemdealassociationtype Property
     - HubSpot Data Type


Salesforce Quotelineitem to HubSpot Lineitemquoteassociationtype
----------------------------------------------------------------
Every Salesforce Quotelineitem will be synchronized with a HubSpot Lineitemquoteassociationtype.

Once a link between a Salesforce Quotelineitem and a HubSpot Lineitemquoteassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a HubSpot Lineitemquoteassociationtype:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - HubSpot Lineitemquoteassociationtype Property
     - HubSpot Data Type

