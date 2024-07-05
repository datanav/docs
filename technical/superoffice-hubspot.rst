===============================
SuperOffice to Hubspot Dataflow
===============================

Generated: 2024-07-05 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Hubspot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Person to Hubspot Contact
-------------------------------------
Every SuperOffice Person will be synchronized with a Hubspot Contact.

If a matching Hubspot Contact already exists, the SuperOffice Person will be merged with the existing one.
If no matching Hubspot Contact is found, a new Hubspot Contact will be created.

A SuperOffice Person will merge with a Hubspot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Hubspot Contact Property
   * - Emails.Value
     - properties.email

Once a link between a SuperOffice Person and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Hubspot Contact Property
     - Hubspot Data Type
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


SuperOffice User to Hubspot Contact
-----------------------------------
Before any synchronization can take place, a link between a SuperOffice User and a Hubspot Contact must be established.

A SuperOffice User will merge with a Hubspot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Hubspot Contact Property
   * - personEmail
     - properties.email

Once a link between a SuperOffice User and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Hubspot Contact Property
     - Hubspot Data Type
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


SuperOffice Product to Hubspot Product
--------------------------------------
Every SuperOffice Product will be synchronized with a Hubspot Product.

Once a link between a SuperOffice Product and a Hubspot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a Hubspot Product:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Hubspot Product Property
     - Hubspot Data Type
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


SuperOffice Quotealternative to Hubspot Quote
---------------------------------------------
Every SuperOffice Quotealternative will be synchronized with a Hubspot Quote.

Once a link between a SuperOffice Quotealternative and a Hubspot Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a Hubspot Quote:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - Hubspot Quote Property
     - Hubspot Data Type
   * - Name
     - properties.hs_title
     - "string"


SuperOffice Quoteline to Hubspot Lineitem
-----------------------------------------
Every SuperOffice Quoteline will be synchronized with a Hubspot Lineitem.

Once a link between a SuperOffice Quoteline and a Hubspot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a Hubspot Lineitem:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - Hubspot Lineitem Property
     - Hubspot Data Type
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


SuperOffice Sale to Hubspot Deal
--------------------------------
Every SuperOffice Sale will be synchronized with a Hubspot Deal.

Once a link between a SuperOffice Sale and a Hubspot Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale and a Hubspot Deal:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     - Hubspot Deal Property
     - Hubspot Data Type
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


SuperOffice User to Hubspot User
--------------------------------
Every SuperOffice User will be synchronized with a Hubspot User.

Once a link between a SuperOffice User and a Hubspot User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a Hubspot User:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Hubspot User Property
     - Hubspot Data Type
   * - personEmail
     - email
     - "string"

