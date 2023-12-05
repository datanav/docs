============================
Businesscentral to  Dataflow
============================

Generated: 2023-12-05 00:00:00

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Companies to  Contact
-------------------------------------
Every Businesscentral Companies will be synchronized with a  Contact.

Once a link between a Businesscentral Companies and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Companies and a  Contact:

.. list-table::
   :header-rows: 1

   * - Businesscentral Companies Property
     -  Contact Property
     -  Data Type


Businesscentral Company to  Contact
-----------------------------------
Every Businesscentral Company will be synchronized with a  Contact.

Once a link between a Businesscentral Company and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Company and a  Contact:

.. list-table::
   :header-rows: 1

   * - Businesscentral Company Property
     -  Contact Property
     -  Data Type


Businesscentral Contact company to  Contact
-------------------------------------------
Every Businesscentral Contact company will be synchronized with a  Contact.

Once a link between a Businesscentral Contact company and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contact company and a  Contact:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contact company Property
     -  Contact Property
     -  Data Type
   * - addressLine1
     - Address.Postal.Address1
     - "string"
   * - addressLine1
     - Address.Street.Address1
     - "string"
   * - addressLine2
     - Address.Postal.Address2
     - "string"
   * - addressLine2
     - Address.Street.Address2
     - "string"
   * - city
     - Address.Postal.City
     - "string"
   * - city
     - Address.Street.City
     - "string"
   * - country
     - Country.CountryId
     - "integer"
   * - id
     - ContactId
     - "integer"
   * - phoneNumber
     - Phones.Value
     - "string"
   * - postalCode
     - Address.Postal.Zipcode
     - "string"
   * - postalCode
     - Address.Street.Zipcode
     - "string"


Businesscentral Contacts company to  Contact
--------------------------------------------
Every Businesscentral Contacts company will be synchronized with a  Contact.

Once a link between a Businesscentral Contacts company and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts company and a  Contact:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts company Property
     -  Contact Property
     -  Data Type
   * - phoneNumber
     - Phones.Value
     - "string"


Businesscentral Customers company to  Contact
---------------------------------------------
Every Businesscentral Customers company will be synchronized with a  Contact.

Once a link between a Businesscentral Customers company and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a  Contact:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     -  Contact Property
     -  Data Type
   * - displayName
     - Name
     - "string"
   * - phoneNumber
     - Phones.Value
     - "string"


Businesscentral Customers to  Contact
-------------------------------------
Every Businesscentral Customers will be synchronized with a  Contact.

Once a link between a Businesscentral Customers and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers and a  Contact:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers Property
     -  Contact Property
     -  Data Type


Businesscentral Itemcategories to  Listproductcategoryitems
-----------------------------------------------------------
Every Businesscentral Itemcategories will be synchronized with a  Listproductcategoryitems.

Once a link between a Businesscentral Itemcategories and a  Listproductcategoryitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Itemcategories and a  Listproductcategoryitems:

.. list-table::
   :header-rows: 1

   * - Businesscentral Itemcategories Property
     -  Listproductcategoryitems Property
     -  Data Type
   * - displayName
     - Name
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
     - Name
     - "string"
   * - displayName.string
     - Name
     - "string"
   * - itemCategoryId
     - ProductCategoryKey
     - "string"
   * - taxGroupCode
     - VAT
     - "integer", "decimal"]
   * - unitCost
     - UnitCost
     - "string"
   * - unitPrice
     - UnitListPrice
     - "decimal"

