===============================
HubSpot to SuperOffice Dataflow
===============================

Generated: 2023-06-23 07:30:52

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Contact to SuperOffice Person
-------------------------------------
Every HubSpot Contact will be synchronized with a SuperOffice Person.

If a matching SuperOffice Person already exists, the HubSpot Contact will be merged with the existing one.
If no matching SuperOffice Person is found, a new SuperOffice Person will be created.

A HubSpot Contact will merge with a SuperOffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - SuperOffice Person Property
   * - properties.email
     - Emails.Value

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
   * - properties.name
     - Name
     - "string"
   * - properties.phone
     - Phones.Value
     - "string"
   * - properties.website
     - Domains
     - "list"
   * - properties.zip
     - Address.Street.Zipcode
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

