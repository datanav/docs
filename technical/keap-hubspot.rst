========================
Keap to HubSpot Dataflow
========================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Keap to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Keap Companies to HubSpot Company
---------------------------------
Every Keap Companies will be synchronized with a HubSpot Company.

Once a link between a Keap Companies and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Companies and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Keap Companies Property
     - HubSpot Company Property
     - HubSpot Data Type
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


Keap Contacts to HubSpot Contact
--------------------------------
Every Keap Contacts will be synchronized with a HubSpot Contact.

Once a link between a Keap Contacts and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Contacts and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Keap Contacts Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - birthday
     - properties.date_of_birth
     - "string"


Keap Opportunity to HubSpot Deal
--------------------------------
Every Keap Opportunity will be synchronized with a HubSpot Deal.

Once a link between a Keap Opportunity and a HubSpot Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Opportunity and a HubSpot Deal:

.. list-table::
   :header-rows: 1

   * - Keap Opportunity Property
     - HubSpot Deal Property
     - HubSpot Data Type
   * - contact.id
     - properties.hubspot_owner_id
     - "string"
   * - opportunity_title
     - properties.dealname
     - "string"


Keap Product to HubSpot Product
-------------------------------
Every Keap Product will be synchronized with a HubSpot Product.

Once a link between a Keap Product and a HubSpot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Product and a HubSpot Product:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     - HubSpot Product Property
     - HubSpot Data Type
   * - product_desc
     - properties.description
     - "string"
   * - product_name
     - properties.name
     - "string"
   * - product_price
     - properties.price
     - "string"


Keap Users to HubSpot User
--------------------------
Every Keap Users will be synchronized with a HubSpot User.

Once a link between a Keap Users and a HubSpot User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Users and a HubSpot User:

.. list-table::
   :header-rows: 1

   * - Keap Users Property
     - HubSpot User Property
     - HubSpot Data Type
   * - email_address
     - email
     - "string"

