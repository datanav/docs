=============================
Tripletex to Zendesk Dataflow
=============================

Generated: 2023-10-10 21:00:00

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Zendesk. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to Zendesk Users
----------------------------------
Every Tripletex Contact will be synchronized with a Zendesk Users.

If a matching Zendesk Users already exists, the Tripletex Contact will be merged with the existing one.
If no matching Zendesk Users is found, a new Zendesk Users will be created.

A Tripletex Contact will merge with a Zendesk Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Zendesk Users Property
   * - email
     - email

Once a link between a Tripletex Contact and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Zendesk Users Property
     - Zendesk Data Type
   * - customer.id
     - organization_id
     - "string"


Tripletex Employee to Zendesk Users
-----------------------------------
Every Tripletex Employee will be synchronized with a Zendesk Users.

If a matching Zendesk Users already exists, the Tripletex Employee will be merged with the existing one.
If no matching Zendesk Users is found, a new Zendesk Users will be created.

A Tripletex Employee will merge with a Zendesk Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Zendesk Users Property
   * - email
     - email

Once a link between a Tripletex Employee and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Zendesk Users Property
     - Zendesk Data Type
   * - department.id
     - organization_id
     - "string"
   * - phoneNumberHome
     - phone
     - "string"


Tripletex Customer to Zendesk Organisations
-------------------------------------------
Every Tripletex Customer will be synchronized with a Zendesk Organisations.

Once a link between a Tripletex Customer and a Zendesk Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Zendesk Organisations:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Zendesk Organisations Property
     - Zendesk Data Type
   * - name
     - name
     - "string"


Tripletex Customer to Zendesk Organizations
-------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a Zendesk Organizations must be established.

A new Zendesk Organizations will be created from a Tripletex Customer if it is connected to a Tripletex Contact, or Employee that is synchronized into Zendesk.

Once a link between a Tripletex Customer and a Zendesk Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Zendesk Organizations:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Zendesk Organizations Property
     - Zendesk Data Type
   * - name
     - name
     - "string"


Tripletex Department to Zendesk Organisations
---------------------------------------------
Every Tripletex Department will be synchronized with a Zendesk Organisations.

Once a link between a Tripletex Department and a Zendesk Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Zendesk Organisations:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Zendesk Organisations Property
     - Zendesk Data Type
   * - name
     - name
     - "string"


Tripletex Department to Zendesk Organizations
---------------------------------------------
Before any synchronization can take place, a link between a Tripletex Department and a Zendesk Organizations must be established.

A new Zendesk Organizations will be created from a Tripletex Department if it is connected to a Tripletex Contact, or Employee that is synchronized into Zendesk.

Once a link between a Tripletex Department and a Zendesk Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Zendesk Organizations:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Zendesk Organizations Property
     - Zendesk Data Type
   * - name
     - name
     - "string"


Tripletex Project to Zendesk Ticketcomments
-------------------------------------------
Every Tripletex Project will be synchronized with a Zendesk Ticketcomments.

Once a link between a Tripletex Project and a Zendesk Ticketcomments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Project and a Zendesk Ticketcomments:

.. list-table::
   :header-rows: 1

   * - Tripletex Project Property
     - Zendesk Ticketcomments Property
     - Zendesk Data Type


Tripletex Supplier to Zendesk Organisations
-------------------------------------------
Every Tripletex Supplier will be synchronized with a Zendesk Organisations.

Once a link between a Tripletex Supplier and a Zendesk Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a Zendesk Organisations:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - Zendesk Organisations Property
     - Zendesk Data Type
   * - name
     - name
     - "string"

