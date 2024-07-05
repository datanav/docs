===============================
HubSpot to Superoffice Dataflow
===============================

Generated: 2024-07-05 00:00:33

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Superoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Contact to Superoffice Person
-------------------------------------
Every HubSpot Contact will be synchronized with a Superoffice Person.

If a matching Superoffice Person already exists, the HubSpot Contact will be merged with the existing one.
If no matching Superoffice Person is found, a new Superoffice Person will be created.

A HubSpot Contact will merge with a Superoffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Superoffice Person Property
   * - properties.email
     - Emails.Value

Once a link between a HubSpot Contact and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Superoffice Person Property
     - Superoffice Data Type
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


HubSpot Company to Superoffice Contact
--------------------------------------
Every HubSpot Company will be synchronized with a Superoffice Contact.

Once a link between a HubSpot Company and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Superoffice Contact Property
     - Superoffice Data Type
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
   * - properties.sesam_org_number_no
     - OrgNr (Dependant on having NO in Country.TwoLetterISOCountry)
     - "string"
   * - properties.sesam_org_number_se
     - OrgNr (Dependant on having SE in Country.TwoLetterISOCountry)
     - "string"
   * - properties.website
     - Domains
     - N/A
   * - properties.website
     - Urls.Value
     - "string"
   * - properties.zip
     - Address.Postal.Zipcode
     - "string"
   * - properties.zip
     - Address.Street.Zipcode
     - "string"


HubSpot Company to Superoffice Person
-------------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a Superoffice Person must be established.

A new Superoffice Person will be created from a HubSpot Company if it is connected to a HubSpot Deal that is synchronized into Superoffice.

Once a link between a HubSpot Company and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Superoffice Person Property
     - Superoffice Data Type


HubSpot Contact to Superoffice Contact
--------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a Superoffice Contact must be established.

A new Superoffice Contact will be created from a HubSpot Contact if it is connected to a HubSpot Deal that is synchronized into Superoffice.

Once a link between a HubSpot Contact and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Superoffice Contact Property
     - Superoffice Data Type


HubSpot Pipelinedeal to SuperOffice Quotealternative
----------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Pipelinedeal and a SuperOffice Quotealternative must be established.

A new SuperOffice Quotealternative will be created from a HubSpot Pipelinedeal if it is connected to a HubSpot Deal, Quote, Lineitem, Quotedealassociation, Dealcompanyassociation, Dealcontactassociation, Lineitemdealassociation, Quotecompanyassociation, Quotecontactassociation, Lineitemquoteassociation, Ticketcompanyassociation, or Quotequotetemplateassociation that is synchronized into SuperOffice.

Once a link between a HubSpot Pipelinedeal and a SuperOffice Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Pipelinedeal and a SuperOffice Quotealternative:

.. list-table::
   :header-rows: 1

   * - HubSpot Pipelinedeal Property
     - SuperOffice Quotealternative Property
     - SuperOffice Data Type
   * - label
     - VATInfo
     - "string"
   * - stages.label
     - VATInfo
     - "string"


HubSpot Contactcompanyassociation to Superoffice Person
-------------------------------------------------------
Every HubSpot Contactcompanyassociation will be synchronized with a Superoffice Person.

Once a link between a HubSpot Contactcompanyassociation and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociation and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     - Superoffice Person Property
     - Superoffice Data Type
   * - sesam_simpleAssociationTypes
     - Contact.ContactId
     - "integer"
   * - toObjectId (Dependant on having wd:Q703534 in sesam_simpleAssociationTypesDependant on having wd:Q703534 in sesam_simpleAssociationTypesDependant on having wd:Q703534 in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having wd:Q703534 in sesam_simpleAssociationTypesDependant on having wd:Q703534 in sesam_simpleAssociationTypesDependant on having wd:Q703534 in sesam_simpleAssociationTypesDependant on having wd:Q703534 in sesam_simpleAssociationTypesDependant on having wd:Q703534 in sesam_simpleAssociationTypes)
     - Contact.ContactId
     - "integer"


HubSpot User to Superoffice Person
----------------------------------
Every HubSpot User will be synchronized with a Superoffice Person.

Once a link between a HubSpot User and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - Superoffice Person Property
     - Superoffice Data Type


HubSpot Deal to Superoffice Sale
--------------------------------
Every HubSpot Deal will be synchronized with a Superoffice Sale.

Once a link between a HubSpot Deal and a Superoffice Sale is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Superoffice Sale:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Superoffice Sale Property
     - Superoffice Data Type
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
   * - properties.dealname
     - SaleText
     - "string"
   * - properties.description
     - SaleText
     - "string"


HubSpot Lineitem to Superoffice Quoteline
-----------------------------------------
Every HubSpot Lineitem will be synchronized with a Superoffice Quoteline.

Once a link between a HubSpot Lineitem and a Superoffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a Superoffice Quoteline:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - Superoffice Quoteline Property
     - Superoffice Data Type
   * - properties.description
     - Description
     - "string"
   * - properties.hs_discount_percentage
     - DiscountPercent
     - "integer"
   * - properties.hs_discount_percentage
     - ERPDiscountPercent
     - N/A
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


HubSpot Product to Superoffice Product
--------------------------------------
Every HubSpot Product will be synchronized with a Superoffice Product.

Once a link between a HubSpot Product and a Superoffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a Superoffice Product:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - Superoffice Product Property
     - Superoffice Data Type
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


HubSpot Quote to Superoffice Quotealternative
---------------------------------------------
Every HubSpot Quote will be synchronized with a Superoffice Quotealternative.

Once a link between a HubSpot Quote and a Superoffice Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a Superoffice Quotealternative:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - Superoffice Quotealternative Property
     - Superoffice Data Type
   * - properties.hs_quote_amount
     - TotalPrice
     - "float"
   * - properties.hs_title
     - Name
     - "string"

