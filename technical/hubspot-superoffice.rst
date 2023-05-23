===============================
HubSpot to SuperOffice Dataflow
===============================

Generated: 2023-05-23 00:06:41

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Account to SuperOffice Pricelist
----------------------------------------
Before any synchronization can take place, a link between a HubSpot Account and a SuperOffice Pricelist must be established.

A HubSpot Account will merge with a SuperOffice Pricelist if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Account Property
     - SuperOffice Pricelist Property
   * - companyCurrency
     - Currency

Once a link between a HubSpot Account and a SuperOffice Pricelist is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Account and a SuperOffice Pricelist:

.. list-table::
   :header-rows: 1

   * - HubSpot Account Property
     - SuperOffice Pricelist Property
     - SuperOffice Data Type


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
     - Address.Street.Address1
     - "string"
   * - properties.address2
     - Address.Street.Address2
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
     - Domains
     - "list"
   * - properties.website
     - Urls.Value
     - "string"
   * - properties.zip
     - Address.Street.Zipcode
     - "string"


HubSpot Contact to SuperOffice Person
-------------------------------------
Every HubSpot Contact will be synchronized with a SuperOffice Person.

Once a link between a HubSpot Contact and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - SuperOffice Person Property
     - SuperOffice Data Type
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
When a HubSpot Deal gets the has a 100% probability, it  will be synchronized with a SuperOffice Sale.

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
     - "datetime-format","%Y-%m-%dT%H:%M:%S","_."]
   * - properties.deal_currency_code
     - Currency.Id
     - "integer"
   * - properties.dealname
     - SaleText
     - "string"
   * - properties.dealstage
     - Status
     - "string"
   * - properties.description
     - SaleText
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
   * - properties.name
     - Name
     - "string"
   * - properties.price
     - UnitListPrice
     - "string"
   * - properties.quantity
     - Quantity
     - "integer"


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
     - "integer"
   * - properties.hs_title
     - Name
     - "string"


HubSpot Ticket to SuperOffice Ticket
------------------------------------
Every HubSpot Ticket will be synchronized with a SuperOffice Ticket.

Once a link between a HubSpot Ticket and a SuperOffice Ticket is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticket and a SuperOffice Ticket:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticket Property
     - SuperOffice Ticket Property
     - SuperOffice Data Type
   * - properties.hubspot_owner_id
     - OwnedBy.AssociateId
     - "integer"
   * - properties.subject
     - Title
     - "string"

