=================================
Poweroffice to Tripletex Dataflow
=================================

Generated: 2023-08-17 08:57:39

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

