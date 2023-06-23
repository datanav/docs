=================================
Tripletex to PowerOffice Dataflow
=================================

Generated: 2023-06-23 11:19:51

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to PowerOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Employee to PowerOffice Employee
------------------------------------------
Before any synchronization can take place, a link between a Tripletex Employee and a PowerOffice Employee must be established.

A Tripletex Employee will merge with a PowerOffice Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOffice Employee Property
   * - nationalIdentityNumber
     - SocialSecurityNumber

Once a link between a Tripletex Employee and a PowerOffice Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a PowerOffice Employee:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOffice Employee Property
     - PowerOffice Data Type


Tripletex Productgroup to PowerOffice Productgroup
--------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Productgroup and a PowerOffice Productgroup must be established.

A new PowerOffice Productgroup will be created from a Tripletex Productgroup if it is connected to a Tripletex Product that is synchronized into PowerOffice.

Once a link between a Tripletex Productgroup and a PowerOffice Productgroup is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productgroup and a PowerOffice Productgroup:

.. list-table::
   :header-rows: 1

   * - Tripletex Productgroup Property
     - PowerOffice Productgroup Property
     - PowerOffice Data Type


Tripletex Customer to PowerOffice Customer
------------------------------------------
Every Tripletex Customer will be synchronized with a PowerOffice Customer.

Once a link between a Tripletex Customer and a PowerOffice Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a PowerOffice Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOffice Customer Property
     - PowerOffice Data Type


Tripletex Supplier to PowerOffice Customer
------------------------------------------
Every Tripletex Supplier will be synchronized with a PowerOffice Customer.

Once a link between a Tripletex Supplier and a PowerOffice Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a PowerOffice Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - PowerOffice Customer Property
     - PowerOffice Data Type
   * - deliveryAddress.addressLine1
     - streetAddresses.address1
     - "string"
   * - deliveryAddress.addressLine2
     - streetAddresses.address2
     - "string"
   * - deliveryAddress.changes
     - streetAddresses.city
     - "string"
   * - deliveryAddress.city
     - streetAddresses.countryCode
     - "string"
   * - deliveryAddress.postalCode
     - streetAddresses.zipCode
     - "string"
   * - email
     - EmailAddress
     - "string"
   * - id
     - id
     - "string"
   * - invoiceEmail
     - InvoiceEmailAddress
     - "string"
   * - name
     - LegalName
     - "string"
   * - phoneNumber
     - PhoneNumber
     - "string"
   * - physicalAddress.addressLine1
     - streetAddresses.address1
     - "string"
   * - physicalAddress.addressLine2
     - streetAddresses.address2
     - "string"
   * - physicalAddress.city
     - streetAddresses.city
     - "string"
   * - physicalAddress.country.id
     - streetAddresses.countryCode
     - "string"
   * - physicalAddress.postalCode
     - streetAddresses.zipCode
     - "string"
   * - postalAddress.addressLine1
     - mailAddress.address1
     - "string"
   * - postalAddress.addressLine1
     - streetAddresses.address1
     - "string"
   * - postalAddress.addressLine2
     - mailAddress.address2
     - "string"
   * - postalAddress.addressLine2
     - streetAddresses.address2
     - "string"
   * - postalAddress.city
     - mailAddress.city
     - "string"
   * - postalAddress.city
     - streetAddresses.city
     - "string"
   * - postalAddress.country.id
     - mailAddress.countryCode
     - "string"
   * - postalAddress.country.id
     - streetAddresses.countryCode
     - "string"
   * - postalAddress.postalCode
     - mailAddress.zipCode
     - "string"
   * - postalAddress.postalCode
     - streetAddresses.zipCode
     - "string"

