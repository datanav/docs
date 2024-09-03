======================
Tripletex to  Dataflow
======================

Generated: 2024-09-03 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer to  Companies
--------------------------------
Every Tripletex Customer will be synchronized with a  Companies.

Once a link between a Tripletex Customer and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a  Companies:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     -  Companies Property
     -  Data Type
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


Tripletex Department to  Companies
----------------------------------
Every Tripletex Department will be synchronized with a  Companies.

Once a link between a Tripletex Department and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a  Companies:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     -  Companies Property
     -  Data Type
   * - name
     - company_name
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
   * - dateOfBirth
     - birthday
     - "string"


Tripletex Product to  Product
-----------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a  Product.

Once a link between a Tripletex Product and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a  Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     -  Product Property
     -  Data Type
   * - description
     - product_desc
     - "string"
   * - name
     - product_name
     - "string"
   * - priceExcludingVatCurrency
     - product_price
     - "string"

