====================================
Business Central to HubSpot Dataflow
====================================

Generated: 2024-09-12 00:00:03

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


Business Central Contacts person to HubSpot Contact
---------------------------------------------------
Every Business Central Contacts person will be synchronized with a HubSpot Contact.

Once a link between a Business Central Contacts person and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contacts person and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts person Property
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


Business Central Customers company to HubSpot Company
-----------------------------------------------------
Every Business Central Customers company will be synchronized with a HubSpot Company.

Once a link between a Business Central Customers company and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers company and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Business Central Customers company Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - address.city
     - properties.city
     - "string"
   * - address.countryLetterCode
     - properties.country
     - "string"
   * - address.postalCode
     - properties.zip
     - "string"
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
   * - id (Dependant on having  in typeDependant on having NO in type)
     - sync_org_nr
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


Business Central Customers person to HubSpot Contact
----------------------------------------------------
Every Business Central Customers person will be synchronized with a HubSpot Contact.

Once a link between a Business Central Customers person and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers person and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Business Central Customers person Property
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
   * - email
     - properties.email
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
   * - displayName.string
     - properties.name
     - "string"
   * - displayName2
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
   * - amountExcludingTax
     - properties.price
     - "string"
   * - description
     - properties.description
     - "string"
   * - description
     - properties.name
     - "string"
   * - discountPercent
     - properties.hs_discount_percentage
     - "string"
   * - invoiceQuantity
     - properties.quantity
     - "integer"
   * - itemId
     - properties.hs_product_id
     - "string"
   * - quantity
     - properties.quantity
     - N/A
   * - unitPrice
     - properties.price
     - "string"

