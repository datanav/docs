======================
Tripletex to  Dataflow
======================

Generated: 2024-08-29 10:36:42

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer person to  Contacts
--------------------------------------
Every Tripletex Customer person will be synchronized with a  Contacts.

Once a link between a Tripletex Customer person and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     -  Contacts Property
     -  Data Type
   * - deliveryAddress.city
     - City
     - "string"
   * - deliveryAddress.country.id
     - Country
     - "string"
   * - email
     - Email
     - "string"
   * - name
     - FullName
     - "string"
   * - phoneNumber
     - Phone
     - "string"
   * - phoneNumberMobile
     - Mobile
     - "string"
   * - physicalAddress.city
     - City
     - "string"
   * - physicalAddress.country.id
     - Country
     - "string"
   * - postalAddress.city
     - City
     - "string"
   * - postalAddress.country.id
     - Country
     - "string"


Tripletex Employee to  Contacts
-------------------------------
Every Tripletex Employee will be synchronized with a  Contacts.

Once a link between a Tripletex Employee and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     -  Contacts Property
     -  Data Type
   * - address.city
     - City
     - "string"
   * - address.country.id
     - Country
     - "string"
   * - dateOfBirth
     - BirthDate
     - "string"
   * - email
     - BusinessEmail
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - lastName
     - LastName
     - "string"
   * - phoneNumberMobile
     - Mobile
     - "string"
   * - phoneNumberWork
     - Phone
     - "string"


Tripletex Contact to  Contacts
------------------------------
Every Tripletex Contact will be synchronized with a  Contacts.

Once a link between a Tripletex Contact and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     -  Contacts Property
     -  Data Type
   * - email
     - Email
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - lastName
     - LastName
     - "string"
   * - phoneNumberMobile
     - Mobile
     - "string"
   * - phoneNumberWork
     - Phone
     - "string"

