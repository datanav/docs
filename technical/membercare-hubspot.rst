==============================
MemberCare to HubSpot Dataflow
==============================

Generated: 2024-09-12 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from MemberCare to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

MemberCare Companies to HubSpot Company
---------------------------------------
Every MemberCare Companies will be synchronized with a HubSpot Company.

Once a link between a MemberCare Companies and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Companies and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - MemberCare Companies Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - companyName
     - properties.name
     - "string"
   * - url
     - properties.website
     - "string"


MemberCare Organizations to HubSpot Company
-------------------------------------------
Every MemberCare Organizations will be synchronized with a HubSpot Company.

Once a link between a MemberCare Organizations and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Organizations and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - MemberCare Organizations Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - name
     - properties.name
     - "string"


MemberCare Persons to HubSpot Contact
-------------------------------------
Every MemberCare Persons will be synchronized with a HubSpot Contact.

Once a link between a MemberCare Persons and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Persons and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - MemberCare Persons Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - addresses.country.id
     - properties.country
     - "string"
   * - addresses.id
     - id
     - "string"
   * - addresses.postalCode.city
     - properties.city
     - "string"
   * - addresses.postalCode.zipCode
     - properties.zip
     - "string"
   * - birthDate
     - properties.date_of_birth
     - "string"
   * - firstname
     - properties.firstname
     - "string"
   * - lastname
     - properties.lastname
     - "string"


MemberCare Invoices to HubSpot Lineitem
---------------------------------------
Every MemberCare Invoices will be synchronized with a HubSpot Lineitem.

Once a link between a MemberCare Invoices and a HubSpot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Invoices and a HubSpot Lineitem:

.. list-table::
   :header-rows: 1

   * - MemberCare Invoices Property
     - HubSpot Lineitem Property
     - HubSpot Data Type
   * - invoiceItems.description
     - properties.description
     - "string"
   * - invoiceItems.quantity
     - properties.quantity
     - N/A
   * - invoiceItems.unitPrice
     - properties.price
     - "string"

