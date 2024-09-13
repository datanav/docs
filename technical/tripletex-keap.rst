==========================
Tripletex to Keap Dataflow
==========================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer to Keap Companies
------------------------------------
Every Tripletex Customer will be synchronized with a Keap Companies.

Once a link between a Tripletex Customer and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Keap Companies Property
     - Keap Data Type
   * - deliveryAddress.city
     - address.locality
     - "string"
   * - deliveryAddress.postalCode
     - address.zip_code
     - "string"
   * - id
     - id
     - "string"
   * - name
     - company_name
     - "string"
   * - physicalAddress.city
     - address.locality
     - "string"
   * - physicalAddress.postalCode
     - address.zip_code
     - "string"
   * - postalAddress.city
     - address.locality
     - "string"
   * - postalAddress.postalCode
     - address.zip_code
     - "string"


Tripletex Contact to Keap Contacts
----------------------------------
Every Tripletex Contact will be synchronized with a Keap Contacts.

Once a link between a Tripletex Contact and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Keap Contacts Property
     - Keap Data Type


Tripletex Customer person to Keap Contacts
------------------------------------------
Every Tripletex Customer person will be synchronized with a Keap Contacts.

Once a link between a Tripletex Customer person and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - Keap Contacts Property
     - Keap Data Type


Tripletex Department to Keap Companies
--------------------------------------
Every Tripletex Department will be synchronized with a Keap Companies.

Once a link between a Tripletex Department and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Keap Companies Property
     - Keap Data Type
   * - name
     - company_name
     - "string"


Tripletex Employee to Keap Contacts
-----------------------------------
Every Tripletex Employee will be synchronized with a Keap Contacts.

Once a link between a Tripletex Employee and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Keap Contacts Property
     - Keap Data Type
   * - dateOfBirth
     - birthday
     - "string"


Tripletex Product to Keap Product
---------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a Keap Product.

Once a link between a Tripletex Product and a Keap Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a Keap Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Keap Product Property
     - Keap Data Type
   * - description
     - product_desc
     - "string"
   * - name
     - product_name
     - "string"
   * - priceExcludingVatCurrency
     - product_price
     - "string"

