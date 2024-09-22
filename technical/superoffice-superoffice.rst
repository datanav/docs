===================================
SuperOffice to SuperOffice Dataflow
===================================

Generated: 2024-09-22 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to SuperOffice Contact
------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a SuperOffice Contact must be established.

A SuperOffice Contact will merge with a SuperOffice Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - SuperOffice Contact Property
   * - ContactId
     - ContactId
   * - Emails.Value
     - Emails.Value

Once a link between a SuperOffice Contact and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - Address.Postal.Address1
     - Address.Street.Address1
     - "string"
   * - Address.Postal.Address2
     - Address.Street.Address2
     - "string"
   * - Address.Postal.Address3
     - Address.Street.Address3
     - "string"
   * - Address.Postal.City
     - Address.Street.City
     - "string"
   * - Address.Postal.Zipcode
     - Address.Street.Zipcode
     - "string"
   * - Address.Street.Address1
     - Address.Postal.Address1
     - "string"
   * - Address.Street.Address2
     - Address.Postal.Address2
     - "string"
   * - Address.Street.Address3
     - Address.Postal.Address3
     - "string"
   * - Address.Street.City
     - Address.Postal.City
     - "string"
   * - Address.Street.Zipcode
     - Address.Postal.Zipcode
     - "string"
   * - ContactId
     - ContactId
     - "integer"
   * - Country.CountryId
     - Country.CountryId
     - N/A
   * - Country.ThreeLetterISOCountry
     - OrgNr (Dependant on having wd:Q906278 in Country.TwoLetterISOCountry)
     - "string"


SuperOffice Ownercontactlink to SuperOffice Contact
---------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Ownercontactlink and a SuperOffice Contact must be established.

A SuperOffice Ownercontactlink will merge with a SuperOffice Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ownercontactlink Property
     - SuperOffice Contact Property
   * - contact_id
     - ContactId

Once a link between a SuperOffice Ownercontactlink and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Ownercontactlink and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ownercontactlink Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - name
     - Name
     - "string"


SuperOffice Person to SuperOffice Person
----------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a SuperOffice Person must be established.

A SuperOffice Person will merge with a SuperOffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - SuperOffice Person Property
   * - Emails.Value
     - Emails.Value

Once a link between a SuperOffice Person and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - SuperOffice Person Property
     - SuperOffice Data Type


SuperOffice Product to SuperOffice Product
------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Product and a SuperOffice Product must be established.

A SuperOffice Product will merge with a SuperOffice Product if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - SuperOffice Product Property
   * - ProductId
     - ProductId
   * - ERPProductKey
     - ERPProductKey

Once a link between a SuperOffice Product and a SuperOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a SuperOffice Product:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - SuperOffice Product Property
     - SuperOffice Data Type


SuperOffice Quote to SuperOffice Sale
-------------------------------------
Before any synchronization can take place, a link between a SuperOffice Quote and a SuperOffice Sale must be established.

A SuperOffice Quote will merge with a SuperOffice Sale if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quote Property
     - SuperOffice Sale Property
   * - SaleId
     - SaleId

Once a link between a SuperOffice Quote and a SuperOffice Sale is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quote and a SuperOffice Sale:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quote Property
     - SuperOffice Sale Property
     - SuperOffice Data Type
   * - AcceptedQuoteAlternativeId
     - Status
     - "string"


SuperOffice Sale to SuperOffice Sale
------------------------------------
Before any synchronization can take place, a link between a SuperOffice Sale and a SuperOffice Sale must be established.

A SuperOffice Sale will merge with a SuperOffice Sale if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     - SuperOffice Sale Property
   * - SaleId
     - SaleId

Once a link between a SuperOffice Sale and a SuperOffice Sale is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale and a SuperOffice Sale:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     - SuperOffice Sale Property
     - SuperOffice Data Type
   * - Contact.ContactId
     - Person.PersonId
     - "integer"
   * - Person.PersonId
     - Contact.ContactId
     - "integer"


SuperOffice User to SuperOffice Person
--------------------------------------
Before any synchronization can take place, a link between a SuperOffice User and a SuperOffice Person must be established.

A SuperOffice User will merge with a SuperOffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - SuperOffice Person Property
   * - personEmail
     - Emails.Value

Once a link between a SuperOffice User and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - contactId
     - Contact.ContactId
     - "integer"
   * - firstName
     - Firstname
     - "string"
   * - lastName
     - Lastname
     - "string"
   * - personEmail
     - Emails.Value
     - "string"

