===================================
Businesscentral to Hubspot Dataflow
===================================

Generated: 2024-07-04 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to Hubspot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Companies to Hubspot Company
--------------------------------------------
Every Businesscentral Companies will be synchronized with a Hubspot Company.

Once a link between a Businesscentral Companies and a Hubspot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Companies and a Hubspot Company:

.. list-table::
   :header-rows: 1

   * - Businesscentral Companies Property
     - Hubspot Company Property
     - Hubspot Data Type


Businesscentral Contacts person to Hubspot Contact
--------------------------------------------------
Every Businesscentral Contacts person will be synchronized with a Hubspot Contact.

Once a link between a Businesscentral Contacts person and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     - Hubspot Contact Property
     - Hubspot Data Type
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


Businesscentral Customers company to Hubspot Company
----------------------------------------------------
Every Businesscentral Customers company will be synchronized with a Hubspot Company.

Once a link between a Businesscentral Customers company and a Hubspot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a Hubspot Company:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     - Hubspot Company Property
     - Hubspot Data Type
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


Businesscentral Customers person to Hubspot Contact
---------------------------------------------------
Every Businesscentral Customers person will be synchronized with a Hubspot Contact.

Once a link between a Businesscentral Customers person and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers person and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers person Property
     - Hubspot Contact Property
     - Hubspot Data Type
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


Businesscentral Employees to Hubspot Contact
--------------------------------------------
Every Businesscentral Employees will be synchronized with a Hubspot Contact.

Once a link between a Businesscentral Employees and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Employees and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - Businesscentral Employees Property
     - Hubspot Contact Property
     - Hubspot Data Type
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


Businesscentral Items to Hubspot Product
----------------------------------------
Every Businesscentral Items will be synchronized with a Hubspot Product.

Once a link between a Businesscentral Items and a Hubspot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a Hubspot Product:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     - Hubspot Product Property
     - Hubspot Data Type
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


Businesscentral Salesorderlines to Hubspot Lineitem
---------------------------------------------------
Every Businesscentral Salesorderlines will be synchronized with a Hubspot Lineitem.

Once a link between a Businesscentral Salesorderlines and a Hubspot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorderlines and a Hubspot Lineitem:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorderlines Property
     - Hubspot Lineitem Property
     - Hubspot Data Type
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

