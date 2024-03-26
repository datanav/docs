========================
SuperOffice to  Dataflow
========================

Generated: 2024-03-26 00:00:02

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


SuperOffice User to  Contact
----------------------------
Before any synchronization can take place, a link between a SuperOffice User and a  Contact must be established.

A SuperOffice User will merge with a  Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     -  Contact Property
   * - personEmail
     - properties.email

Once a link between a SuperOffice User and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a  Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     -  Contact Property
     -  Data Type
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


SuperOffice Product to  Product
-------------------------------
Every SuperOffice Product will be synchronized with a  Product.

Once a link between a SuperOffice Product and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a  Product:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     -  Product Property
     -  Data Type
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


SuperOffice Quotealternative to  Quote
--------------------------------------
Every SuperOffice Quotealternative will be synchronized with a  Quote.

Once a link between a SuperOffice Quotealternative and a  Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a  Quote:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     -  Quote Property
     -  Data Type
   * - Name
     - properties.hs_title
     - "string"


SuperOffice Quoteline to  Lineitem
----------------------------------
Every SuperOffice Quoteline will be synchronized with a  Lineitem.

Once a link between a SuperOffice Quoteline and a  Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a  Lineitem:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     -  Lineitem Property
     -  Data Type
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
     - "string", "integer", "decimal"]]
   * - UnitListPrice
     - properties.price
     - "string"


SuperOffice Sale to  Deal
-------------------------
Every SuperOffice Sale will be synchronized with a  Deal.

Once a link between a SuperOffice Sale and a  Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale and a  Deal:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     -  Deal Property
     -  Data Type
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


SuperOffice User to  User
-------------------------
Every SuperOffice User will be synchronized with a  User.

Once a link between a SuperOffice User and a  User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a  User:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     -  User Property
     -  Data Type
   * - personEmail
     - email
     - "string"

