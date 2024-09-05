=================================
Salesforce to Membercare Dataflow
=================================

Generated: 2024-09-05 13:11:24

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Contact to Membercare Persons
----------------------------------------
Every Salesforce Contact will be synchronized with a Membercare Persons.

Once a link between a Salesforce Contact and a Membercare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a Membercare Persons:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - Membercare Persons Property
     - Membercare Data Type
   * - Birthdate
     - birthDate
     - "string"
   * - FirstName
     - firstname
     - "string"
   * - LastName
     - lastname
     - "string"
   * - Name
     - firstname
     - "string"
   * - Name
     - name
     - "string"


Salesforce Product2 to Membercare Products
------------------------------------------
Every Salesforce Product2 will be synchronized with a Membercare Products.

Once a link between a Salesforce Product2 and a Membercare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Membercare Products:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Membercare Products Property
     - Membercare Data Type
   * - Name	
     - name
     - "string"


Salesforce Contact to Membercare Countries
------------------------------------------
Every Salesforce Contact will be synchronized with a Membercare Countries.

Once a link between a Salesforce Contact and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - Membercare Countries Property
     - Membercare Data Type
   * - MailingCountry
     - name
     - "string"


Salesforce Currencytype to Membercare Companies
-----------------------------------------------
Every Salesforce Currencytype will be synchronized with a Membercare Companies.

Once a link between a Salesforce Currencytype and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Currencytype and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Salesforce Currencytype Property
     - Membercare Companies Property
     - Membercare Data Type


Salesforce Organization to Membercare Companies
-----------------------------------------------
Every Salesforce Organization will be synchronized with a Membercare Companies.

Once a link between a Salesforce Organization and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Membercare Companies Property
     - Membercare Data Type
   * - City
     - addresses.postalCode.city
     - "string"
   * - Country
     - addresses.country.id
     - "string"
   * - Name	
     - companyName
     - "string"
   * - Name	
     - name
     - "string"
   * - PostalCode	
     - addresses.postalCode.zipCode
     - "string"
   * - Street	
     - addresses.street
     - "string"

