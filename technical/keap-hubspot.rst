========================
Keap to Hubspot Dataflow
========================

Generated: 2024-09-07 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Keap to Hubspot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Keap Companies to Hubspot Company
---------------------------------
Every Keap Companies will be synchronized with a Hubspot Company.

Once a link between a Keap Companies and a Hubspot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Companies and a Hubspot Company:

.. list-table::
   :header-rows: 1

   * - Keap Companies Property
     - Hubspot Company Property
     - Hubspot Data Type
   * - address.locality
     - properties.city
     - "string"
   * - address.zip_code
     - properties.zip
     - "string"
   * - company_name
     - properties.name
     - "string"
   * - id
     - id
     - "string"


Keap Contacts to Hubspot Contact
--------------------------------
Every Keap Contacts will be synchronized with a Hubspot Contact.

Once a link between a Keap Contacts and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Contacts and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - Keap Contacts Property
     - Hubspot Contact Property
     - Hubspot Data Type
   * - birthday
     - properties.date_of_birth
     - "string"


Keap Opportunity to Hubspot Deal
--------------------------------
Every Keap Opportunity will be synchronized with a Hubspot Deal.

Once a link between a Keap Opportunity and a Hubspot Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Opportunity and a Hubspot Deal:

.. list-table::
   :header-rows: 1

   * - Keap Opportunity Property
     - Hubspot Deal Property
     - Hubspot Data Type
   * - contact.id
     - properties.hubspot_owner_id
     - "string"
   * - opportunity_title
     - properties.dealname
     - "string"


Keap Product to Hubspot Product
-------------------------------
Every Keap Product will be synchronized with a Hubspot Product.

Once a link between a Keap Product and a Hubspot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Product and a Hubspot Product:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     - Hubspot Product Property
     - Hubspot Data Type
   * - product_desc
     - properties.description
     - "string"
   * - product_name
     - properties.name
     - "string"
   * - product_price
     - properties.price
     - "string"


Keap Users to Hubspot User
--------------------------
Every Keap Users will be synchronized with a Hubspot User.

Once a link between a Keap Users and a Hubspot User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Users and a Hubspot User:

.. list-table::
   :header-rows: 1

   * - Keap Users Property
     - Hubspot User Property
     - Hubspot Data Type
   * - email_address
     - email
     - "string"

