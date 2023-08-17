===============================
SuperOffice to HubSpot Dataflow
===============================

Generated: 2023-08-17 08:59:08

Introduction.
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
   * - Phones.Value
     - properties.phone
     - "string"
   * - Urls.Value
     - properties.website
     - "string"


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
   * - ERPProductKey
     - properties.hs_sku
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


SuperOffice Quoteline to HubSpot Lineitemdealassociation
--------------------------------------------------------
Every SuperOffice Quoteline will be synchronized with a HubSpot Lineitemdealassociation.

Once a link between a SuperOffice Quoteline and a HubSpot Lineitemdealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a HubSpot Lineitemdealassociation:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - HubSpot Lineitemdealassociation Property
     - HubSpot Data Type
   * - QuoteAlternativeId
     - toObjectId (Dependant on having wd:Q566889 in sesam_simpleAssociationTypesDependant on having wd:Q566889 in sesam_simpleAssociationTypes)
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


SuperOffice Ticket to HubSpot Ticket
------------------------------------
Every SuperOffice Ticket will be synchronized with a HubSpot Ticket.

Once a link between a SuperOffice Ticket and a HubSpot Ticket is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Ticket and a HubSpot Ticket:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ticket Property
     - HubSpot Ticket Property
     - HubSpot Data Type
   * - OwnedBy.AssociateId
     - properties.hubspot_owner_id
     - "string"
   * - Title
     - properties.subject
     - "string"

