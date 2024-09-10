==============================
Membercare to Hubspot Dataflow
==============================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Membercare to Hubspot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Membercare Companies to Hubspot Company
---------------------------------------
Every Membercare Companies will be synchronized with a Hubspot Company.

Once a link between a Membercare Companies and a Hubspot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Companies and a Hubspot Company:

.. list-table::
   :header-rows: 1

   * - Membercare Companies Property
     - Hubspot Company Property
     - Hubspot Data Type
   * - companyName
     - properties.name
     - "string"
   * - url
     - properties.website
     - "string"


Membercare Organizations to Hubspot Company
-------------------------------------------
Every Membercare Organizations will be synchronized with a Hubspot Company.

Once a link between a Membercare Organizations and a Hubspot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Organizations and a Hubspot Company:

.. list-table::
   :header-rows: 1

   * - Membercare Organizations Property
     - Hubspot Company Property
     - Hubspot Data Type
   * - name
     - properties.name
     - "string"


Membercare Persons to Hubspot Contact
-------------------------------------
Every Membercare Persons will be synchronized with a Hubspot Contact.

Once a link between a Membercare Persons and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Persons and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - Membercare Persons Property
     - Hubspot Contact Property
     - Hubspot Data Type
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


Membercare Invoices to Hubspot Lineitem
---------------------------------------
Every Membercare Invoices will be synchronized with a Hubspot Lineitem.

Once a link between a Membercare Invoices and a Hubspot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Invoices and a Hubspot Lineitem:

.. list-table::
   :header-rows: 1

   * - Membercare Invoices Property
     - Hubspot Lineitem Property
     - Hubspot Data Type
   * - invoiceItems.description
     - properties.description
     - "string"
   * - invoiceItems.quantity
     - properties.quantity
     - N/A
   * - invoiceItems.unitPrice
     - properties.price
     - "string"

