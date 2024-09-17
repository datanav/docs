=================================
Wave to Business Central Dataflow
=================================

Generated: 2024-09-17 07:26:52

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to Business Central Customers company
---------------------------------------------------
Before any synchronization can take place, a link between a Wave Customer and a Business Central Customers company must be established.

A new Business Central Customers company will be created from a Wave Customer if it is connected to a Wave Invoice that is synchronized into Business Central.

Once a link between a Wave Customer and a Business Central Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Business Central Customers company:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Business Central Customers company Property
     - Business Central Data Type


Wave Customer to Business Central Customers person
--------------------------------------------------
Before any synchronization can take place, a link between a Wave Customer and a Business Central Customers person must be established.

A new Business Central Customers person will be created from a Wave Customer if it is connected to a Wave Invoice that is synchronized into Business Central.

Once a link between a Wave Customer and a Business Central Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Business Central Customers person:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Business Central Customers person Property
     - Business Central Data Type
   * - address.addressLine1
     - addressLine1
     - "string"
   * - address.addressLine2
     - addressLine2
     - "string"
   * - address.city
     - address.city
     - "string"
   * - address.city
     - addressLine2
     - "string"
   * - address.city
     - city
     - "string"
   * - address.country.code
     - country
     - "string"
   * - address.postalCode
     - address.postalCode
     - "string"
   * - address.postalCode
     - postalCode
     - "string"
   * - id
     - id
     - "string"
   * - shippingDetails.address.addressLine1
     - addressLine1
     - "string"
   * - shippingDetails.address.addressLine2
     - addressLine2
     - "string"
   * - shippingDetails.address.city
     - address.city
     - "string"
   * - shippingDetails.address.city
     - addressLine2
     - "string"
   * - shippingDetails.address.city
     - city
     - "string"
   * - shippingDetails.address.country.code
     - country
     - "string"
   * - shippingDetails.address.postalCode
     - address.postalCode
     - "string"
   * - shippingDetails.address.postalCode
     - postalCode
     - "string"


Wave Invoice to Business Central Salesorders
--------------------------------------------
Before any synchronization can take place, a link between a Wave Invoice and a Business Central Salesorders must be established.

A new Business Central Salesorders will be created from a Wave Invoice if it is connected to a Wave Invoice that is synchronized into Business Central.

Once a link between a Wave Invoice and a Business Central Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Business Central Salesorders:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Business Central Salesorders Property
     - Business Central Data Type


Wave Product to Business Central Items
--------------------------------------
Before any synchronization can take place, a link between a Wave Product and a Business Central Items must be established.

A new Business Central Items will be created from a Wave Product if it is connected to a Wave Invoice that is synchronized into Business Central.

Once a link between a Wave Product and a Business Central Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a Business Central Items:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - Business Central Items Property
     - Business Central Data Type


Wave Customer to Business Central Companies
-------------------------------------------
Every Wave Customer will be synchronized with a Business Central Companies.

Once a link between a Wave Customer and a Business Central Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Business Central Companies:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Business Central Companies Property
     - Business Central Data Type


Wave Customer to Business Central Contacts person
-------------------------------------------------
Every Wave Customer will be synchronized with a Business Central Contacts person.

Once a link between a Wave Customer and a Business Central Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Business Central Contacts person:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Business Central Contacts person Property
     - Business Central Data Type


Wave Customer to Business Central Customers company
---------------------------------------------------
Every Wave Customer will be synchronized with a Business Central Customers company.

Once a link between a Wave Customer and a Business Central Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Business Central Customers company:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Business Central Customers company Property
     - Business Central Data Type


Wave Customer to Business Central Customers person
--------------------------------------------------
Every Wave Customer will be synchronized with a Business Central Customers person.

Once a link between a Wave Customer and a Business Central Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Business Central Customers person:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Business Central Customers person Property
     - Business Central Data Type


Wave Customer person to Business Central Customers company
----------------------------------------------------------
Every Wave Customer person will be synchronized with a Business Central Customers company.

Once a link between a Wave Customer person and a Business Central Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a Business Central Customers company:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Business Central Customers company Property
     - Business Central Data Type


Wave Customer person to Business Central Customers person
---------------------------------------------------------
Every Wave Customer person will be synchronized with a Business Central Customers person.

Once a link between a Wave Customer person and a Business Central Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a Business Central Customers person:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Business Central Customers person Property
     - Business Central Data Type


Wave Invoice to Business Central Salesorderlines
------------------------------------------------
Every Wave Invoice will be synchronized with a Business Central Salesorderlines.

Once a link between a Wave Invoice and a Business Central Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Business Central Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Business Central Salesorderlines Property
     - Business Central Data Type


Wave Invoice to Business Central Salesorders
--------------------------------------------
Every Wave Invoice will be synchronized with a Business Central Salesorders.

Once a link between a Wave Invoice and a Business Central Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Business Central Salesorders:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Business Central Salesorders Property
     - Business Central Data Type


Wave Product to Business Central Items
--------------------------------------
Every Wave Product will be synchronized with a Business Central Items.

Once a link between a Wave Product and a Business Central Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a Business Central Items:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - Business Central Items Property
     - Business Central Data Type


Wave Vendor to Business Central Contacts person
-----------------------------------------------
Every Wave Vendor will be synchronized with a Business Central Contacts person.

Once a link between a Wave Vendor and a Business Central Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Business Central Contacts person:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Business Central Contacts person Property
     - Business Central Data Type

