====================================
Business Central to HubSpot Dataflow
====================================

Generated: 2024-09-22 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Central Companies to HubSpot Company
---------------------------------------------
Every Business Central Companies will be synchronized with a HubSpot Company.

Once a link between a Business Central Companies and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Companies and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Business Central Companies Property
     - HubSpot Company Property
     - HubSpot Data Type


Business Central Contacts (human data) to HubSpot Contact
---------------------------------------------------------
Every Business Central Contacts (human data) will be synchronized with a HubSpot Contact.

Once a link between a Business Central Contacts (human data) and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contacts (human data) and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts (human data) Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - addressLine1
     - properties.address
     - "string"
   * - city
     - properties.city
     - "string"
   * - country
     - properties.country
     - "string"
   * - email
     - properties.email
     - "string"
   * - id
     - id
     - "string"
   * - mobilePhoneNumber
     - properties.mobilephone
     - "string"
   * - phoneNumber
     - properties.phone
     - "string"
   * - postalCode
     - properties.zip
     - "string"


Business Central Customers (organisation data) to HubSpot Company
-----------------------------------------------------------------
Every Business Central Customers (organisation data) will be synchronized with a HubSpot Company.

Once a link between a Business Central Customers (organisation data) and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (organisation data) and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Business Central Customers (organisation data) Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - addressLine1
     - properties.address
     - "string"
   * - addressLine2
     - properties.address2
     - "string"
   * - city
     - properties.city
     - "string"
   * - country
     - properties.country
     - "string"
   * - displayName
     - properties.name
     - "string"
   * - id
     - id
     - "string"
   * - phoneNumber
     - properties.phone
     - "string"
   * - postalCode
     - properties.zip
     - "string"
   * - website
     - properties.website
     - "string"


Business Central Customers (human data) to HubSpot Contact
----------------------------------------------------------
Every Business Central Customers (human data) will be synchronized with a HubSpot Contact.

Once a link between a Business Central Customers (human data) and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (human data) and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Business Central Customers (human data) Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - addressLine1
     - properties.address
     - "string"
   * - city
     - properties.city
     - "string"
   * - country
     - properties.country
     - "string"
   * - email
     - properties.email
     - "string"
   * - id
     - id
     - "string"
   * - phoneNumber
     - properties.phone
     - "string"
   * - postalCode
     - properties.zip
     - "string"


Business Central Employees to HubSpot Contact
---------------------------------------------
Every Business Central Employees will be synchronized with a HubSpot Contact.

Once a link between a Business Central Employees and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Employees and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Business Central Employees Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - birthDate
     - properties.date_of_birth
     - "string"
   * - givenName
     - properties.firstname
     - "string"
   * - mobilePhone
     - properties.mobilephone
     - "string"
   * - personalEmail
     - properties.email
     - "string"
   * - phoneNumber
     - properties.phone
     - "string"
   * - surname
     - properties.lastname
     - "string"


Business Central Items to HubSpot Product
-----------------------------------------
Every Business Central Items will be synchronized with a HubSpot Product.

Once a link between a Business Central Items and a HubSpot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Items and a HubSpot Product:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     - HubSpot Product Property
     - HubSpot Data Type
   * - displayName
     - properties.name
     - "string"
   * - unitCost
     - properties.hs_cost_of_goods_sold
     - "string"
   * - unitPrice
     - properties.price
     - "string"


Business Central Salesorderlines to HubSpot Lineitem
----------------------------------------------------
Every Business Central Salesorderlines will be synchronized with a HubSpot Lineitem.

Once a link between a Business Central Salesorderlines and a HubSpot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorderlines and a HubSpot Lineitem:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorderlines Property
     - HubSpot Lineitem Property
     - HubSpot Data Type


Business Central Salesorderlines to HubSpot Lineitemdealassociationtype
-----------------------------------------------------------------------
Every Business Central Salesorderlines will be synchronized with a HubSpot Lineitemdealassociationtype.

Once a link between a Business Central Salesorderlines and a HubSpot Lineitemdealassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorderlines and a HubSpot Lineitemdealassociationtype:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorderlines Property
     - HubSpot Lineitemdealassociationtype Property
     - HubSpot Data Type


Business Central Salesorderlines to HubSpot Lineitemquoteassociationtype
------------------------------------------------------------------------
Every Business Central Salesorderlines will be synchronized with a HubSpot Lineitemquoteassociationtype.

Once a link between a Business Central Salesorderlines and a HubSpot Lineitemquoteassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorderlines and a HubSpot Lineitemquoteassociationtype:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorderlines Property
     - HubSpot Lineitemquoteassociationtype Property
     - HubSpot Data Type


Business Central Salesorders to HubSpot Deal
--------------------------------------------
Every Business Central Salesorders will be synchronized with a HubSpot Deal.

Once a link between a Business Central Salesorders and a HubSpot Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorders and a HubSpot Deal:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
     - HubSpot Deal Property
     - HubSpot Data Type
   * - currencyId
     - properties.deal_currency_code
     - "string"
   * - orderDate
     - properties.closedate
     - "string"
   * - totalAmountExcludingTax
     - properties.amount
     - "string"

