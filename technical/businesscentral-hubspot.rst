============================
Businesscentral to  Dataflow
============================

Generated: 2024-01-07 00:00:01

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Companies to  Company
-------------------------------------
Every Businesscentral Companies will be synchronized with a  Company.

Once a link between a Businesscentral Companies and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Companies and a  Company:

.. list-table::
   :header-rows: 1

   * - Businesscentral Companies Property
     -  Company Property
     -  Data Type


Businesscentral Contacts person to  Contact
-------------------------------------------
Every Businesscentral Contacts person will be synchronized with a  Contact.

Once a link between a Businesscentral Contacts person and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a  Contact:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     -  Contact Property
     -  Data Type
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


Businesscentral Customers company to  Company
---------------------------------------------
Every Businesscentral Customers company will be synchronized with a  Company.

Once a link between a Businesscentral Customers company and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a  Company:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     -  Company Property
     -  Data Type
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
   * - phoneNumber
     - properties.phone
     - "string"
   * - postalCode
     - properties.zip
     - "string"


Businesscentral Items to  Product
---------------------------------
Every Businesscentral Items will be synchronized with a  Product.

Once a link between a Businesscentral Items and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a  Product:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     -  Product Property
     -  Data Type
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


Businesscentral Salesorderlines to  Lineitem
--------------------------------------------
Every Businesscentral Salesorderlines will be synchronized with a  Lineitem.

Once a link between a Businesscentral Salesorderlines and a  Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorderlines and a  Lineitem:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorderlines Property
     -  Lineitem Property
     -  Data Type
   * - amountExcludingTax
     - properties.price
     - "string"
   * - description
     - properties.description
     - "string"
   * - description
     - properties.name
     - "string"
   * - invoiceQuantity
     - properties.quantity
     - "integer"
   * - itemId
     - properties.hs_product_id
     - "string"
   * - quantity
     - properties.quantity
     - "integer"
   * - unitPrice
     - properties.price
     - "string"


Businesscentral Salesorderlines to  Lineitemdealassociation
-----------------------------------------------------------
Every Businesscentral Salesorderlines will be synchronized with a  Lineitemdealassociation.

Once a link between a Businesscentral Salesorderlines and a  Lineitemdealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorderlines and a  Lineitemdealassociation:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorderlines Property
     -  Lineitemdealassociation Property
     -  Data Type
   * - documentId
     - toObjectId (Dependant on having wd:Q566889 in sesam_simpleAssociationTypes)
     - "string"

