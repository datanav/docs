===========================
Wix.com to HubSpot Dataflow
===========================

Generated: 2023-09-05 14:00:20

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to HubSpot Contact
-----------------------------------
Every Wix.com Contacts will be synchronized with a HubSpot Contact.

If a matching HubSpot Contact already exists, the Wix.com Contacts will be merged with the existing one.
If no matching HubSpot Contact is found, a new HubSpot Contact will be created.

A Wix.com Contacts will merge with a HubSpot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - HubSpot Contact Property
   * - info.emails
     - properties.email
   * - primaryInfo.email
     - properties.email

Once a link between a Wix.com Contacts and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - info.emails
     - properties.email
     - "string"
   * - info.name.first
     - properties.firstname
     - "string"
   * - info.name.last
     - properties.lastname
     - "string"
   * - info.phones
     - properties.mobilephone
     - "string"
   * - primaryInfo.email
     - properties.email
     - "string"
   * - primaryInfo.phone
     - properties.mobilephone
     - "string"


Wix.com Members to HubSpot Contact
----------------------------------
Every Wix.com Members will be synchronized with a HubSpot Contact.

If a matching HubSpot Contact already exists, the Wix.com Members will be merged with the existing one.
If no matching HubSpot Contact is found, a new HubSpot Contact will be created.

A Wix.com Members will merge with a HubSpot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - HubSpot Contact Property
   * - loginEmail
     - properties.email

Once a link between a Wix.com Members and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - loginEmail
     - properties.email
     - "string"


Wix.com Products to HubSpot Product
-----------------------------------
Every Wix.com Products will be synchronized with a HubSpot Product.

Once a link between a Wix.com Products and a HubSpot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a HubSpot Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - HubSpot Product Property
     - HubSpot Data Type
   * - costRange.maxValue
     - properties.hs_cost_of_goods_sold
     - "string"
   * - description
     - properties.description
     - "string"
   * - name
     - properties.name
     - "string"
   * - price.price
     - properties.price
     - "string"
   * - sku
     - properties.hs_sku
     - "string"

