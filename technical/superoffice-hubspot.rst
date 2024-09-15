===============================
SuperOffice to HubSpot Dataflow
===============================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Person to HubSpot Contact
-------------------------------------
Every SuperOffice Person will be synchronized with a HubSpot Contact.

If a matching HubSpot Contact already exists, the SuperOffice Person will be merged with the existing one.
If no matching HubSpot Contact is found, a new HubSpot Contact will be created.

A SuperOffice Person will merge with a HubSpot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - HubSpot Contact Property
   * - Emails.Value
     - properties.email

Once a link between a SuperOffice Person and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - Address.Street.Address1
     - properties.address
     - "string"
   * - Address.Street.City
     - properties.city
     - "string"
   * - Address.Street.Zipcode
     - properties.zip
     - "string"
   * - BirthDate
     - properties.date_of_birth
     - "string"
   * - Country.CountryId
     - properties.country
     - "string"
   * - Emails.Value
     - properties.email
     - "string"
   * - Firstname
     - properties.firstname
     - "string"
   * - Lastname
     - properties.lastname
     - "string"
   * - MobilePhones.Value
     - properties.mobilephone
     - "string"
   * - OfficePhones.Value
     - properties.phone
     - "string"
   * - PersonId
     - id
     - "string"


SuperOffice User to HubSpot Contact
-----------------------------------
Before any synchronization can take place, a link between a SuperOffice User and a HubSpot Contact must be established.

A SuperOffice User will merge with a HubSpot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - HubSpot Contact Property
   * - personEmail
     - properties.email

Once a link between a SuperOffice User and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - contactCategory
     - properties.country
     - "string"
   * - contactCategory
     - properties.state
     - "string"
   * - firstName
     - properties.firstname
     - "string"
   * - lastName
     - properties.lastname
     - "string"
   * - personEmail
     - properties.email
     - "string"


SuperOffice Contact to HubSpot Company
--------------------------------------
Every SuperOffice Contact will be synchronized with a HubSpot Company.

Once a link between a SuperOffice Contact and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - Address.Postal.Address1
     - properties.address
     - "string"
   * - Address.Postal.Address2
     - properties.address2
     - "string"
   * - Address.Postal.City
     - properties.city
     - "string"
   * - Address.Postal.Zipcode
     - properties.zip
     - "string"
   * - Address.Street.Address1
     - properties.address
     - "string"
   * - Address.Street.Address2
     - properties.address2
     - "string"
   * - Address.Street.City
     - properties.city
     - "string"
   * - Address.Street.Zipcode
     - properties.zip
     - "string"
   * - ContactId
     - id
     - "string"
   * - Country.CountryId
     - properties.country
     - "string"
   * - Domains
     - properties.website
     - "string"
   * - Name
     - properties.name
     - "string"
   * - OrgNr (Dependant on having NO in Country.TwoLetterISOCountry)
     - properties.sesam_org_number_no
     - "string"
   * - OrgNr (Dependant on having SE in Country.TwoLetterISOCountry)
     - properties.sesam_org_number_se
     - "string"
   * - OrgNr (Dependant on having  in Country.ThreeLetterISOCountryDependant on having NO in Country.ThreeLetterISOCountryDependant on having  in Country.TwoLetterISOCountryDependant on having NO in Country.TwoLetterISOCountry)
     - sync_org_nr
     - "string"
   * - Phones.Value
     - properties.phone
     - "string"
   * - Urls.Value
     - properties.website
     - "string"


SuperOffice Contact to HubSpot Contact
--------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a HubSpot Contact must be established.

A new HubSpot Contact will be created from a SuperOffice Contact if it is connected to a SuperOffice Quote, or Quotealternative that is synchronized into HubSpot.

Once a link between a SuperOffice Contact and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - HubSpot Contact Property
     - HubSpot Data Type


SuperOffice Person to HubSpot Company
-------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a HubSpot Company must be established.

A new HubSpot Company will be created from a SuperOffice Person if it is connected to a SuperOffice Quote, or Quotealternative that is synchronized into HubSpot.

Once a link between a SuperOffice Person and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - HubSpot Company Property
     - HubSpot Data Type


SuperOffice Product to HubSpot Product
--------------------------------------
Every SuperOffice Product will be synchronized with a HubSpot Product.

Once a link between a SuperOffice Product and a HubSpot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a HubSpot Product:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - HubSpot Product Property
     - HubSpot Data Type
   * - Description
     - properties.description
     - "string"
   * - ERPProductKey
     - properties.hs_sku
     - "string"
   * - Name
     - properties.name
     - "string"
   * - UnitCost
     - properties.hs_cost_of_goods_sold
     - "string"
   * - UnitListPrice
     - properties.price
     - "string"


SuperOffice Quotealternative to HubSpot Quote
---------------------------------------------
Every SuperOffice Quotealternative will be synchronized with a HubSpot Quote.

Once a link between a SuperOffice Quotealternative and a HubSpot Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a HubSpot Quote:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - HubSpot Quote Property
     - HubSpot Data Type
   * - Name
     - properties.hs_title
     - "string"


SuperOffice Quoteline to HubSpot Lineitem
-----------------------------------------
Every SuperOffice Quoteline will be synchronized with a HubSpot Lineitem.

Once a link between a SuperOffice Quoteline and a HubSpot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a HubSpot Lineitem:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - HubSpot Lineitem Property
     - HubSpot Data Type
   * - Description
     - properties.description
     - "string"
   * - DiscountPercent
     - properties.hs_discount_percentage
     - "string"
   * - ERPDiscountPercent
     - properties.hs_discount_percentage
     - "string"
   * - ERPProductKey
     - properties.hs_product_id
     - "string"
   * - Name
     - properties.name
     - "string"
   * - Quantity
     - properties.quantity
     - N/A
   * - UnitListPrice
     - properties.price
     - "string"


SuperOffice Sale to HubSpot Deal
--------------------------------
Every SuperOffice Sale will be synchronized with a HubSpot Deal.

Once a link between a SuperOffice Sale and a HubSpot Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale and a HubSpot Deal:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     - HubSpot Deal Property
     - HubSpot Data Type
   * - Amount
     - properties.amount
     - "string"
   * - Currency.Id
     - properties.deal_currency_code
     - "string"
   * - Heading
     - properties.dealname
     - "string"
   * - SaleText
     - properties.dealname
     - "string"
   * - SaleText
     - properties.description
     - "string"
   * - Saledate
     - properties.closedate
     - "string"


SuperOffice User to HubSpot User
--------------------------------
Every SuperOffice User will be synchronized with a HubSpot User.

Once a link between a SuperOffice User and a HubSpot User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a HubSpot User:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - HubSpot User Property
     - HubSpot Data Type
   * - personEmail
     - email
     - "string"

