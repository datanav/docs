=================================
Membercare to Salesforce Dataflow
=================================

Generated: 2024-09-05 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Membercare to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Membercare Organizations to Salesforce Organization
---------------------------------------------------
Every Membercare Organizations will be synchronized with a Salesforce Organization.

Once a link between a Membercare Organizations and a Salesforce Organization is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Organizations and a Salesforce Organization:

.. list-table::
   :header-rows: 1

   * - Membercare Organizations Property
     - Salesforce Organization Property
     - Salesforce Data Type
   * - addresses.country.id
     - Country
     - "string"
   * - addresses.postalCode.city
     - City
     - "string"
   * - addresses.postalCode.zipCode
     - PostalCode	
     - "string"
   * - company.addresses.addressDescription
     - Country
     - "string"
   * - company.addresses.municipality
     - PostalCode	
     - "string"
   * - company.addresses.start
     - City
     - "string"
   * - name
     - Name	
     - "string"


Membercare Products to Salesforce Product2
------------------------------------------
Every Membercare Products will be synchronized with a Salesforce Product2.

Once a link between a Membercare Products and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Products and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - Membercare Products Property
     - Salesforce Product2 Property
     - Salesforce Data Type
   * - name
     - Name	
     - "string"


Membercare Companies to Salesforce Organization
-----------------------------------------------
Every Membercare Companies will be synchronized with a Salesforce Organization.

Once a link between a Membercare Companies and a Salesforce Organization is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Companies and a Salesforce Organization:

.. list-table::
   :header-rows: 1

   * - Membercare Companies Property
     - Salesforce Organization Property
     - Salesforce Data Type
   * - addresses.country.id
     - Country
     - "string"
   * - addresses.postalCode.city
     - City
     - "string"
   * - addresses.postalCode.zipCode
     - PostalCode	
     - "string"
   * - companyName
     - Name	
     - "string"

