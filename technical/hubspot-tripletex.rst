=============================
HubSpot to Tripletex Dataflow
=============================

Generated: 2023-05-23 06:26:42

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to Tripletex Customer
-----------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a SuperOffice Contact if it is connected to a SuperOffice Hubspot-deal, Hubspot-quote, Tripletex-order, Sale, User, Tripletex-contact, Person, Tripletex-employee, Poweroffice-customer, Poweroffice-salesorder, Poweroffice-contactperson, or Quotealternative that is synchronized into Tripletex.

A SuperOffice Contact will merge with a Tripletex Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Tripletex Customer Property
   * - Emails.Value
     - email
   * - Emails.Value
     - invoiceEmail
   * - Emails.Value
     - overdueNoticeEmail

Once a link between a SuperOffice Contact and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - Address.Postal.Address1
     - postalAddress.addressLine1
     - "string"
   * - Address.Postal.Address2
     - postalAddress.addressLine2
     - "string"
   * - Address.Postal.City
     - postalAddress.city
     - "string"
   * - Address.Postal.Zipcode
     - postalAddress.postalCode
     - "string"
   * - Address.Street.Address1
     - physicalAddress.addressLine1
     - "string"
   * - Address.Street.Address2
     - physicalAddress.addressLine2
     - "string"
   * - Address.Street.City
     - physicalAddress.city
     - "string"
   * - Address.Street.Zipcode
     - physicalAddress.postalCode
     - "string"
   * - Associate.AssociateId
     - accountManager.id
     - "integer"
   * - ContactId
     - id
     - "integer"
   * - Country.CountryId
     - physicalAddress.country.id
     - "integer"
   * - Country.CountryId
     - postalAddress.country.id
     - "integer"
   * - Emails.Value
     - email
     - "string"
   * - Name
     - name
     - "string"
   * - OrgNr (Dependant on having NOR in Country.ThreeLetterISOCountryDependant on having NOR in Country.ThreeLetterISOCountry)
     - organizationNumber
     - "string"
   * - Phones.Value
     - phoneNumber
     - "string"


SuperOffice Person to Tripletex Contact
---------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a Tripletex Contact must be established.

A new Tripletex Contact will be created from a SuperOffice Person if it is connected to a SuperOffice Hubspot-deal, Tripletex-order, Sale, Poweroffice-salesorder, or Quotealternative that is synchronized into Tripletex.

A SuperOffice Person will merge with a Tripletex Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Tripletex Contact Property
   * - Emails.Value
     - email

Once a link between a SuperOffice Person and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Tripletex Contact Property
     - Tripletex Data Type
   * - Contact.ContactId
     - customer.id
     - "integer"
   * - Emails.Value
     - email
     - "string"
   * - Firstname
     - firstName
     - "string"
   * - Lastname
     - lastName
     - "string"
   * - MobilePhones.Value
     - phoneNumberMobile
     - "string"
   * - OfficePhones.Value
     - phoneNumberWork
     - "string"


HubSpot Company to Tripletex Customer
-------------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a HubSpot Company if it is connected to a HubSpot Deal, Tripletex-order, Superoffice-sale, Poweroffice-salesorder, or Superoffice-quotealternative that is synchronized into Tripletex.

Once a link between a HubSpot Company and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - id
     - id
     - "integer"
   * - properties.address
     - physicalAddress.addressLine1
     - "string"
   * - properties.address2
     - physicalAddress.addressLine2
     - "string"
   * - properties.city
     - physicalAddress.city
     - "string"
   * - properties.country
     - physicalAddress.country.id
     - "integer"
   * - properties.name
     - name
     - "string"
   * - properties.phone
     - phoneNumber
     - "string"
   * - properties.zip
     - physicalAddress.postalCode
     - "string"


HubSpot Contact to Tripletex Department
---------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a Tripletex Department must be established.

A new Tripletex Department will be created from a HubSpot Contact if it is connected to a HubSpot User, Superoffice-user, Tripletex-contact, Freshteam-employee, Superoffice-person, Tripletex-employee, Poweroffice-employee, or Tripletex-department that is synchronized into Tripletex.

Once a link between a HubSpot Contact and a Tripletex Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Tripletex Department:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Tripletex Department Property
     - Tripletex Data Type
   * - Name
     - name
     - "string"


HubSpot Quotealternative to Tripletex Order
-------------------------------------------
Before any synchronization can take place, a link between a HubSpot Quotealternative and a Tripletex Order must be established.

A new Tripletex Order will be created from a HubSpot Quotealternative if it is connected to a HubSpot Lineitem, Tripletex-orderline, Superoffice-quoteline, or Poweroffice-salesorderline that is synchronized into Tripletex.

Once a link between a HubSpot Quotealternative and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotealternative and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotealternative Property
     - Tripletex Order Property
     - Tripletex Data Type
   * - Name
     - invoiceComment
     - "string"
   * - sesam_Accepted
     - isClosed
     - "string"


HubSpot Customer to Tripletex Department
----------------------------------------
Before any synchronization can take place, a link between a HubSpot Customer and a Tripletex Department must be established.

A new Tripletex Department will be created from a HubSpot Customer if it is connected to a HubSpot User, Superoffice-user, Tripletex-contact, Freshteam-employee, Superoffice-person, Tripletex-employee, Poweroffice-employee, or Tripletex-department that is synchronized into Tripletex.

Once a link between a HubSpot Customer and a Tripletex Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Customer and a Tripletex Department:

.. list-table::
   :header-rows: 1

   * - HubSpot Customer Property
     - Tripletex Department Property
     - Tripletex Data Type
   * - name
     - name
     - "string"


HubSpot Department to Tripletex Customer
----------------------------------------
Before any synchronization can take place, a link between a HubSpot Department and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a HubSpot Department if it is connected to a HubSpot Quote, Superoffice-user, Tripletex-contact, Superoffice-person, Tripletex-employee, Poweroffice-customer, or Poweroffice-contactperson that is synchronized into Tripletex.

Once a link between a HubSpot Department and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Department and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - HubSpot Department Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - name
     - name
     - "string"


HubSpot Deal to Tripletex Order
-------------------------------
When a HubSpot Deal gets the has a 100% probability, it  will be synchronized with a Tripletex Order.

Once a link between a HubSpot Deal and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Tripletex Order Property
     - Tripletex Data Type
   * - properties.closedate
     - deliveryDate
     - "datetime-format","%Y-%m-%d","_."]
   * - properties.closedate
     - orderDate
     - "datetime-format","%Y-%m-%d","_."]
   * - properties.deal_currency_code
     - currency.id
     - "integer"
   * - properties.dealstage
     - isClosed
     - "string"


HubSpot Lineitem to Tripletex Orderline
---------------------------------------
Every HubSpot Lineitem will be synchronized with a Tripletex Orderline.

Once a link between a HubSpot Lineitem and a Tripletex Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a Tripletex Orderline:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - Tripletex Orderline Property
     - Tripletex Data Type
   * - properties.hs_product_id
     - unitCostCurrency
     - "string"
   * - properties.name
     - description
     - "string"
   * - properties.price
     - unitPriceExcludingVatCurrency
     - "float"
   * - properties.quantity
     - count
     - "float"


HubSpot Product to Tripletex Product
------------------------------------
Every HubSpot Product will be synchronized with a Tripletex Product.

Once a link between a HubSpot Product and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - Tripletex Product Property
     - Tripletex Data Type
   * - properties.description
     - description
     - "string"
   * - properties.hs_cost_of_goods_sold
     - costExcludingVatCurrency
     - "integer"
   * - properties.hs_sku
     - number
     - "string"
   * - properties.name
     - name
     - "string"
   * - properties.price
     - priceExcludingVatCurrency
     - "float"


HubSpot User to Tripletex Employee
----------------------------------
Every HubSpot User will be synchronized with a Tripletex Employee.

Once a link between a HubSpot User and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - Tripletex Employee Property
     - Tripletex Data Type


SuperOffice Product to Tripletex Product
----------------------------------------
Every SuperOffice Product will be synchronized with a Tripletex Product.

If a matching Tripletex Product already exists, the SuperOffice Product will be merged with the existing one.
If no matching Tripletex Product is found, a new Tripletex Product will be created.

A SuperOffice Product will merge with a Tripletex Product if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Tripletex Product Property
   * - ERPProductKey
     - number

Once a link between a SuperOffice Product and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Tripletex Product Property
     - Tripletex Data Type
   * - Description
     - description
     - "string"
   * - ERPPriceListKey
     - currency.id
     - "integer"
   * - ERPProductKey
     - number
     - "string"
   * - Name
     - name
     - "string"
   * - PriceUnit
     - productUnit.id
     - "integer"
   * - Supplier
     - supplier.id
     - "integer"
   * - UnitCost
     - costExcludingVatCurrency
     - "integer"
   * - UnitListPrice
     - priceExcludingVatCurrency
     - "float"
   * - VAT
     - vatType
     - "integer"
   * - VAT
     - vatType.id
     - "integer"

