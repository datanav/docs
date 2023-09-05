=========================
Tripletex to Wix Dataflow
=========================

Generated: 2023-09-05 08:47:45

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to Wix Contacts
---------------------------------
Every Tripletex Contact will be synchronized with a Wix Contacts.

If a matching Wix Contacts already exists, the Tripletex Contact will be merged with the existing one.
If no matching Wix Contacts is found, a new Wix Contacts will be created.

A Tripletex Contact will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Wix Contacts Property
   * - email
     - info.emails

Once a link between a Tripletex Contact and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Wix Contacts Property
     - Wix Data Type
   * - email
     - info.emails
     - "string"
   * - phoneNumberMobile
     - info.phones
     - "string"


Tripletex Contact to Wix Members
--------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a Wix Members must be established.

A Tripletex Contact will merge with a Wix Members if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Wix Members Property
   * - email
     - loginEmail

Once a link between a Tripletex Contact and a Wix Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Wix Members:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Wix Members Property
     - Wix Data Type
   * - email
     - loginEmail
     - "string"


Tripletex Employee to Wix Contacts
----------------------------------
Every Tripletex Employee will be synchronized with a Wix Contacts.

If a matching Wix Contacts already exists, the Tripletex Employee will be merged with the existing one.
If no matching Wix Contacts is found, a new Wix Contacts will be created.

A Tripletex Employee will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Wix Contacts Property
   * - email
     - info.emails

Once a link between a Tripletex Employee and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Wix Contacts Property
     - Wix Data Type
   * - email
     - info.emails
     - "string"
   * - phoneNumberMobile
     - info.phones
     - "string"


Tripletex Employee to Wix Members
---------------------------------
Before any synchronization can take place, a link between a Tripletex Employee and a Wix Members must be established.

A Tripletex Employee will merge with a Wix Members if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Wix Members Property
   * - email
     - loginEmail

Once a link between a Tripletex Employee and a Wix Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Wix Members:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Wix Members Property
     - Wix Data Type
   * - email
     - loginEmail
     - "string"

