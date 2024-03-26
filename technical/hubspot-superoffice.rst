===============================
HubSpot to Superoffice Dataflow
===============================

Generated: 2024-03-26 14:14:24

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Superoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Contact to  Person
--------------------------
Every HubSpot Contact will be synchronized with a  Person.

If a matching  Person already exists, the HubSpot Contact will be merged with the existing one.
If no matching  Person is found, a new  Person will be created.

A HubSpot Contact will merge with a  Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     -  Person Property
   * - properties.email
     - Emails.Value

Once a link between a HubSpot Contact and a  Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a  Person:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     -  Person Property
     -  Data Type
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
     - "datetime-format","%Y-%m-%dT%H:%M:%S","_."]
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


HubSpot Company to  Contact
---------------------------
Every HubSpot Company will be synchronized with a  Contact.

Once a link between a HubSpot Company and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a  Contact:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     -  Contact Property
     -  Data Type
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
     - "list"
   * - properties.website
     - Urls.Value
     - "string"
   * - properties.zip
     - Address.Postal.Zipcode
     - "string"
   * - properties.zip
     - Address.Street.Zipcode
     - "string"


HubSpot Company to  Person
--------------------------
Before any synchronization can take place, a link between a HubSpot Company and a  Person must be established.

A new  Person will be created from a HubSpot Company if it is connected to a HubSpot Deal that is synchronized into .

Once a link between a HubSpot Company and a  Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a  Person:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     -  Person Property
     -  Data Type


HubSpot Contact to  Contact
---------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a  Contact must be established.

A new  Contact will be created from a HubSpot Contact if it is connected to a HubSpot Deal that is synchronized into .

Once a link between a HubSpot Contact and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a  Contact:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     -  Contact Property
     -  Data Type


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


HubSpot Contactcompanyassociation to  Person
--------------------------------------------
Every HubSpot Contactcompanyassociation will be synchronized with a  Person.

Once a link between a HubSpot Contactcompanyassociation and a  Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociation and a  Person:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     -  Person Property
     -  Data Type
   * - sesam_simpleAssociationTypes
     - Contact.ContactId
     - "integer"
   * - toObjectId (Dependant on having wd:Q703534 in sesam_simpleAssociationTypesDependant on having wd:Q703534 in sesam_simpleAssociationTypesDependant on having wd:Q703534 in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having  in sesam_simpleAssociationTypesDependant on having wd:Q703534 in sesam_simpleAssociationTypesDependant on having wd:Q703534 in sesam_simpleAssociationTypesDependant on having wd:Q703534 in sesam_simpleAssociationTypesDependant on having wd:Q703534 in sesam_simpleAssociationTypesDependant on having wd:Q703534 in sesam_simpleAssociationTypes)
     - Contact.ContactId
     - "integer"


HubSpot User to  Person
-----------------------
Every HubSpot User will be synchronized with a  Person.

Once a link between a HubSpot User and a  Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a  Person:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     -  Person Property
     -  Data Type


HubSpot Deal to  Sale
---------------------
Every HubSpot Deal will be synchronized with a  Sale.

Once a link between a HubSpot Deal and a  Sale is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a  Sale:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     -  Sale Property
     -  Data Type
   * - properties.amount
     - Amount
     - "float"
   * - properties.closedate
     - Saledate
     - "datetime-format","%Y-%m-%dT%H:%M:%S","_."]
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


HubSpot Lineitem to  Quoteline
------------------------------
Every HubSpot Lineitem will be synchronized with a  Quoteline.

Once a link between a HubSpot Lineitem and a  Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a  Quoteline:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     -  Quoteline Property
     -  Data Type
   * - properties.description
     - Description
     - "string"
   * - properties.hs_discount_percentage
     - DiscountPercent
     - "integer"
   * - properties.hs_discount_percentage
     - ERPDiscountPercent
     - "decimal"
   * - properties.hs_product_id
     - ERPProductKey
     - "string"
   * - properties.name
     - Name
     - "string"
   * - properties.price
     - UnitListPrice
     - "if-null", "integer", "string"], "decimal"]
   * - properties.quantity
     - Quantity
     - "integer", "decimal"]


HubSpot Product to  Product
---------------------------
Every HubSpot Product will be synchronized with a  Product.

Once a link between a HubSpot Product and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a  Product:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     -  Product Property
     -  Data Type
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
     - "decimal"


HubSpot Quote to  Quotealternative
----------------------------------
Every HubSpot Quote will be synchronized with a  Quotealternative.

Once a link between a HubSpot Quote and a  Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a  Quotealternative:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     -  Quotealternative Property
     -  Data Type
   * - properties.hs_quote_amount
     - TotalPrice
     - "float"
   * - properties.hs_title
     - Name
     - "string"

