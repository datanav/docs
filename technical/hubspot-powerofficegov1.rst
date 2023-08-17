===================================
HubSpot to PowerOfficeGov1 Dataflow
===================================

Generated: 2023-08-17 08:03:37

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to PowerOfficeGov1. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Contact to PowerOfficeGov1 Employee
-------------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a PowerOfficeGov1 Employee must be established.

A HubSpot Contact will merge with a PowerOfficeGov1 Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - PowerOfficeGov1 Employee Property
   * - properties.email
     - email

Once a link between a HubSpot Contact and a PowerOfficeGov1 Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a PowerOfficeGov1 Employee:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - PowerOfficeGov1 Employee Property
     - PowerOfficeGov1 Data Type
   * - id
     - Id
     - "string"
   * - id
     - id
     - "integer"
   * - properties.address
     - MailAddress.Address1
     - "string"
   * - properties.address
     - address.addressLine1
     - "string"
   * - properties.city
     - MailAddress.City
     - "string"
   * - properties.city
     - address.city
     - "string"
   * - properties.country
     - MailAddress.CountryCode
     - "string"
   * - properties.country
     - address.country.id
     - "integer"
   * - properties.date_of_birth
     - DateOfBirth
     - "string"
   * - properties.date_of_birth
     - dateOfBirth
     - "datetime-format","%Y-%m-%d","_."]
   * - properties.email
     - email
     - "string"
   * - properties.firstname
     - FirstName
     - "string"
   * - properties.firstname
     - firstName
     - "string"
   * - properties.lastname
     - LastName
     - "string"
   * - properties.lastname
     - lastName
     - "string"
   * - properties.mobilephone
     - phoneNumberMobile
     - "string"
   * - properties.phone
     - phoneNumberWork
     - "string"
   * - properties.work_email
     - EmailAddress
     - "string"
   * - properties.zip
     - MailAddress.ZipCode
     - "string"
   * - properties.zip
     - address.postalCode
     - "string"


HubSpot Contact to PowerOfficeGov1 Person
-----------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a PowerOfficeGov1 Person must be established.

A HubSpot Contact will merge with a PowerOfficeGov1 Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - PowerOfficeGov1 Person Property
   * - properties.email
     - Emails.Value

Once a link between a HubSpot Contact and a PowerOfficeGov1 Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a PowerOfficeGov1 Person:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - PowerOfficeGov1 Person Property
     - PowerOfficeGov1 Data Type
   * - id
     - PersonId
     - "integer"
   * - properties.address
     - Address.Street.Address1
     - "string"
   * - properties.city
     - Address.Street.City
     - "string"
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


HubSpot Company to PowerOfficeGov1 Customer
-------------------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a PowerOfficeGov1 Customer must be established.

A new PowerOfficeGov1 Customer will be created from a HubSpot Company if it is connected to a HubSpot Deal that is synchronized into PowerOfficeGov1.

Once a link between a HubSpot Company and a PowerOfficeGov1 Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a PowerOfficeGov1 Customer:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - PowerOfficeGov1 Customer Property
     - PowerOfficeGov1 Data Type
   * - id
     - id
     - "integer"
   * - properties.address
     - address.addressLine1
     - "string"
   * - properties.address
     - physicalAddress.addressLine1
     - "string"
   * - properties.address
     - streetAddresses.address1
     - "string"
   * - properties.address2
     - address.addressLine2
     - "string"
   * - properties.address2
     - physicalAddress.addressLine2
     - "string"
   * - properties.address2
     - streetAddresses.address2
     - "string"
   * - properties.city
     - address.city
     - "string"
   * - properties.city
     - physicalAddress.city
     - "string"
   * - properties.city
     - streetAddresses.city
     - "string"
   * - properties.country
     - address.country.code
     - "string"
   * - properties.country
     - mailAddress.countryCode
     - "string"
   * - properties.country
     - physicalAddress.country.id
     - "integer"
   * - properties.country
     - streetAddresses.countryCode
     - "string"
   * - properties.description
     - internalNotes
     - "string"
   * - properties.industry
     - mailAddress.countryCode
     - "string"
   * - properties.industry
     - streetAddresses.countryCode
     - "string"
   * - properties.name
     - legalName
     - "string"
   * - properties.name
     - name
     - "string"
   * - properties.phone
     - phone
     - "string"
   * - properties.phone
     - phoneNumber
     - "string"
   * - properties.type
     - mailAddress.countryCode
     - "string"
   * - properties.type
     - streetAddresses.countryCode
     - "string"
   * - properties.website
     - website
     - "string"
   * - properties.website
     - websiteUrl
     - "string"
   * - properties.zip
     - address.postalCode
     - "string"
   * - properties.zip
     - physicalAddress.postalCode
     - "string"
   * - properties.zip
     - streetAddresses.zipCode
     - "string"
   * - updatedAt
     - lastChanged
     - "string"


HubSpot Contact to PowerOfficeGov1 Contact
------------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a PowerOfficeGov1 Contact must be established.

A new PowerOfficeGov1 Contact will be created from a HubSpot Contact if it is connected to a HubSpot Deal that is synchronized into PowerOfficeGov1.

Once a link between a HubSpot Contact and a PowerOfficeGov1 Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a PowerOfficeGov1 Contact:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - PowerOfficeGov1 Contact Property
     - PowerOfficeGov1 Data Type
   * - properties.email
     - email
     - "string"
   * - properties.firstname
     - firstName
     - "string"
   * - properties.lastname
     - lastName
     - "string"
   * - properties.mobilephone
     - phoneNumberMobile
     - "if","matches","+*","_."],"join"," ","slice", 1,"split", " ","_."]]],"_."]
   * - properties.phone
     - phoneNumberWork
     - "string"


HubSpot Company to PowerOfficeGov1 Contact
------------------------------------------
Every HubSpot Company will be synchronized with a PowerOfficeGov1 Contact.

Once a link between a HubSpot Company and a PowerOfficeGov1 Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a PowerOfficeGov1 Contact:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - PowerOfficeGov1 Contact Property
     - PowerOfficeGov1 Data Type
   * - id
     - ContactId
     - "integer"
   * - properties.address
     - Address.Street.Address1
     - "string"
   * - properties.address2
     - Address.Street.Address2
     - "string"
   * - properties.city
     - Address.Street.City
     - "string"
   * - properties.name
     - Name
     - "string"
   * - properties.phone
     - Phones.Value
     - "string"
   * - properties.website
     - Domains
     - "list"
   * - properties.website
     - Urls.Value
     - "string"
   * - properties.zip
     - Address.Street.Zipcode
     - "string"


HubSpot Account to PowerOfficeGov1 Currency
-------------------------------------------
Every HubSpot Account will be synchronized with a PowerOfficeGov1 Currency.

If a matching PowerOfficeGov1 Currency already exists, the HubSpot Account will be merged with the existing one.
If no matching PowerOfficeGov1 Currency is found, a new PowerOfficeGov1 Currency will be created.

A HubSpot Account will merge with a PowerOfficeGov1 Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Account Property
     - PowerOfficeGov1 Currency Property
   * - companyCurrency
     - Code
   * - companyCurrency
     - code

Once a link between a HubSpot Account and a PowerOfficeGov1 Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Account and a PowerOfficeGov1 Currency:

.. list-table::
   :header-rows: 1

   * - HubSpot Account Property
     - PowerOfficeGov1 Currency Property
     - PowerOfficeGov1 Data Type


HubSpot Contact to PowerOfficeGov1 Location
-------------------------------------------
Every HubSpot Contact will be synchronized with a PowerOfficeGov1 Location.

Once a link between a HubSpot Contact and a PowerOfficeGov1 Location is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a PowerOfficeGov1 Location:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - PowerOfficeGov1 Location Property
     - PowerOfficeGov1 Data Type


HubSpot Deal to PowerOfficeGov1 Currency
----------------------------------------
Every HubSpot Deal will be synchronized with a PowerOfficeGov1 Currency.

If a matching PowerOfficeGov1 Currency already exists, the HubSpot Deal will be merged with the existing one.
If no matching PowerOfficeGov1 Currency is found, a new PowerOfficeGov1 Currency will be created.

A HubSpot Deal will merge with a PowerOfficeGov1 Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - PowerOfficeGov1 Currency Property
   * - properties.deal_currency_code
     - Code
   * - properties.deal_currency_code
     - code

Once a link between a HubSpot Deal and a PowerOfficeGov1 Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a PowerOfficeGov1 Currency:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - PowerOfficeGov1 Currency Property
     - PowerOfficeGov1 Data Type


HubSpot Deal to PowerOfficeGov1 Salesorder
------------------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a PowerOfficeGov1 Salesorder.

Once a link between a HubSpot Deal and a PowerOfficeGov1 Salesorder is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a PowerOfficeGov1 Salesorder:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - PowerOfficeGov1 Salesorder Property
     - PowerOfficeGov1 Data Type
   * - properties.closedate
     - DeliveryDate
     - "string"
   * - properties.closedate
     - OrderDate
     - "string"
   * - properties.deal_currency_code
     - Currency
     - "string"


HubSpot Lineitemdealassociation to PowerOfficeGov1 Salesorderline
-----------------------------------------------------------------
Every HubSpot Lineitemdealassociation will be synchronized with a PowerOfficeGov1 Salesorderline.

Once a link between a HubSpot Lineitemdealassociation and a PowerOfficeGov1 Salesorderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a PowerOfficeGov1 Salesorderline:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - PowerOfficeGov1 Salesorderline Property
     - PowerOfficeGov1 Data Type


HubSpot Product to PowerOfficeGov1 Product
------------------------------------------
Every HubSpot Product will be synchronized with a PowerOfficeGov1 Product.

Once a link between a HubSpot Product and a PowerOfficeGov1 Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a PowerOfficeGov1 Product:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - PowerOfficeGov1 Product Property
     - PowerOfficeGov1 Data Type
   * - properties.description
     - Description
     - "string"
   * - properties.description
     - description
     - "string"
   * - properties.hs_cost_of_goods_sold
     - UnitCost
     - "string"
   * - properties.hs_cost_of_goods_sold
     - costExcludingVatCurrency
     - "integer"
   * - properties.hs_cost_of_goods_sold
     - costPrice
     - "string"
   * - properties.name
     - Name
     - "string"
   * - properties.name
     - name
     - "string"
   * - properties.price
     - UnitListPrice
     - "decimal"
   * - properties.price
     - priceExcludingVatCurrency
     - "float"
   * - properties.price
     - salesPrice
     - "string"
   * - properties.price
     - unitPrice
     - "string"

