===============================
HubSpot to SuperOffice Dataflow
===============================

Generated: 2024-10-01 00:00:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Contact to SuperOffice Person
-------------------------------------
Every HubSpot Contact will be synchronized with a SuperOffice Person.

If a matching SuperOffice Person already exists, the HubSpot Contact will be merged with the existing one.
If no matching SuperOffice Person is found, a new SuperOffice Person will be created.

A HubSpot Contact will merge with a SuperOffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - SuperOffice Person Property
   * - properties.email
     - Emails.Value

Once a link between a HubSpot Contact and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - id
     - PersonId
     - "integer"
   * - properties.address
     - Address.Street.Address1
     - "string"
   * - properties.city
     - Address.Street.City
     - "string"
   * - properties.country
     - Country.CountryId
     - "integer"
   * - properties.date_of_birth
     - BirthDate
     - N/A
   * - properties.email
     - Emails.Value
     - "string"
   * - properties.firstname
     - Firstname
     - "string"
   * - properties.lastname
     - Lastname
     - "string"
   * - properties.mobilephone
     - MobilePhones.Value
     - "string"
   * - properties.phone
     - OfficePhones.Value
     - "string"
   * - properties.zip
     - Address.Street.Zipcode
     - "string"


HubSpot Company to SuperOffice Contact
--------------------------------------
Every HubSpot Company will be synchronized with a SuperOffice Contact.

Once a link between a HubSpot Company and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - id
     - ContactId
     - "integer"
   * - properties.address
     - Address.Postal.Address1
     - "string"
   * - properties.address
     - Address.Street.Address1
     - "string"
   * - properties.address2
     - Address.Postal.Address2
     - "string"
   * - properties.address2
     - Address.Street.Address2
     - "string"
   * - properties.city
     - Address.Postal.City
     - "string"
   * - properties.city
     - Address.Street.City
     - "string"
   * - properties.country
     - Country.CountryId
     - "integer"
   * - properties.name
     - Name
     - "string"
   * - properties.phone
     - Phones.Value
     - "string"
   * - properties.website
     - Urls.Value
     - "string"
   * - properties.zip
     - Address.Postal.Zipcode
     - "string"
   * - properties.zip
     - Address.Street.Zipcode
     - "string"


HubSpot Contactcompanyassociation to SuperOffice Person
-------------------------------------------------------
Every HubSpot Contactcompanyassociation will be synchronized with a SuperOffice Person.

Once a link between a HubSpot Contactcompanyassociation and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociation and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - toObjectId (Dependant on having wd:Q703534 in sesam_simpleAssociationTypes)
     - Contact.ContactId
     - "integer"


HubSpot User to SuperOffice Person
----------------------------------
Every HubSpot User will be synchronized with a SuperOffice Person.

Once a link between a HubSpot User and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - SuperOffice Person Property
     - SuperOffice Data Type


HubSpot Deal to SuperOffice Sale
--------------------------------
Every HubSpot Deal will be synchronized with a SuperOffice Sale.

Once a link between a HubSpot Deal and a SuperOffice Sale is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a SuperOffice Sale:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - SuperOffice Sale Property
     - SuperOffice Data Type
   * - properties.amount
     - Amount
     - "float"
   * - properties.closedate
     - Saledate
     - N/A
   * - properties.deal_currency_code
     - Currency.Id
     - "integer"
   * - properties.dealname
     - Heading
     - "string"


HubSpot Lineitem to SuperOffice Quoteline
-----------------------------------------
Every HubSpot Lineitem will be synchronized with a SuperOffice Quoteline.

Once a link between a HubSpot Lineitem and a SuperOffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a SuperOffice Quoteline:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - SuperOffice Quoteline Property
     - SuperOffice Data Type
   * - properties.description
     - Description
     - "string"
   * - properties.hs_discount_percentage
     - ERPDiscountPercent
     - "integer"
   * - properties.hs_product_id
     - ERPProductKey
     - "string"
   * - properties.name
     - Name
     - "string"
   * - properties.price
     - UnitListPrice
     - N/A
   * - properties.quantity
     - Quantity
     - N/A


HubSpot Lineitemdealassociationtype to SuperOffice Quoteline
------------------------------------------------------------
Every HubSpot Lineitemdealassociationtype will be synchronized with a SuperOffice Quoteline.

Once a link between a HubSpot Lineitemdealassociationtype and a SuperOffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociationtype and a SuperOffice Quoteline:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociationtype Property
     - SuperOffice Quoteline Property
     - SuperOffice Data Type
   * - label
     - VATInfo
     - "string"


HubSpot Lineitemquoteassociationtype to SuperOffice Quoteline
-------------------------------------------------------------
Every HubSpot Lineitemquoteassociationtype will be synchronized with a SuperOffice Quoteline.

Once a link between a HubSpot Lineitemquoteassociationtype and a SuperOffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociationtype and a SuperOffice Quoteline:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociationtype Property
     - SuperOffice Quoteline Property
     - SuperOffice Data Type
   * - label
     - VATInfo
     - "string"


HubSpot Product to SuperOffice Product
--------------------------------------
Every HubSpot Product will be synchronized with a SuperOffice Product.

Once a link between a HubSpot Product and a SuperOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a SuperOffice Product:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - SuperOffice Product Property
     - SuperOffice Data Type
   * - properties.description
     - Description
     - "string"
   * - properties.hs_cost_of_goods_sold
     - UnitCost
     - "string"
   * - properties.name
     - Name
     - "string"
   * - properties.price
     - UnitListPrice
     - N/A


HubSpot Quote to SuperOffice Quotealternative
---------------------------------------------
Every HubSpot Quote will be synchronized with a SuperOffice Quotealternative.

Once a link between a HubSpot Quote and a SuperOffice Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a SuperOffice Quotealternative:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - SuperOffice Quotealternative Property
     - SuperOffice Data Type
   * - properties.hs_quote_amount
     - TotalPrice
     - "float"

