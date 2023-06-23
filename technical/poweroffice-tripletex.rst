=================================
Poweroffice to Tripletex Dataflow
=================================

Generated: 2023-06-23 07:31:52

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Poweroffice to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Poweroffice Employee to Tripletex Employee
------------------------------------------
Before any synchronization can take place, a link between a Poweroffice Employee and a Tripletex Employee must be established.

A Poweroffice Employee will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Poweroffice Employee Property
     - Tripletex Employee Property
   * - SocialSecurityNumber
     - nationalIdentityNumber

Once a link between a Poweroffice Employee and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Employee and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - Poweroffice Employee Property
     - Tripletex Employee Property
     - Tripletex Data Type
   * - DateOfBirth
     - dateOfBirth
     - "datetime-format","%Y-%m-%d","_."]
   * - FirstName
     - firstName
     - "string"
   * - LastName
     - lastName
     - "string"


Poweroffice Customer to Tripletex Customer
------------------------------------------
Every Poweroffice Customer will be synchronized with a Tripletex Customer.

Once a link between a Poweroffice Customer and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Customer and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Poweroffice Customer Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - EmailAddress
     - email
     - "string"
   * - InvoiceEmailAddress
     - invoiceEmail
     - "string"
   * - LegalName
     - name
     - "string"
   * - PhoneNumber
     - phoneNumber
     - "string"
   * - id
     - id
     - "integer"
   * - mailAddress.address1
     - postalAddress.addressLine1
     - "string"
   * - mailAddress.address2
     - postalAddress.addressLine2
     - "string"
   * - mailAddress.city
     - postalAddress.city
     - "string"
   * - mailAddress.countryCode
     - postalAddress.country.id
     - "integer"
   * - mailAddress.zipCode
     - postalAddress.postalCode
     - "string"

