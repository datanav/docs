====================================
HubSpot to Business Central Dataflow
====================================

Generated: 2024-09-14 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to Business Central Customers company
-----------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a Business Central Customers company must be established.

A new Business Central Customers company will be created from a HubSpot Company if it is connected to a HubSpot Deal that is synchronized into Business Central.

Once a link between a HubSpot Company and a Business Central Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Business Central Customers company:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Business Central Customers company Property
     - Business Central Data Type
   * - id
     - id
     - "string"
   * - properties.address
     - addressLine1
     - "string"
   * - properties.address2
     - addressLine2
     - "string"
   * - properties.city
     - address.city
     - "string"
   * - properties.city
     - city
     - "string"
   * - properties.country
     - address.countryLetterCode
     - "string"
   * - properties.country
     - country
     - "string"
   * - properties.name
     - displayName
     - "string"
   * - properties.phone
     - phoneNumber
     - "string"
   * - properties.website
     - website
     - "string"
   * - properties.zip
     - address.postalCode
     - "string"
   * - properties.zip
     - postalCode
     - "string"


HubSpot Company to Business Central Customers person
----------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a Business Central Customers person must be established.

A new Business Central Customers person will be created from a HubSpot Company if it is connected to a HubSpot Deal that is synchronized into Business Central.

Once a link between a HubSpot Company and a Business Central Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Business Central Customers person:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Business Central Customers person Property
     - Business Central Data Type


HubSpot Contact to Business Central Customers company
-----------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a Business Central Customers company must be established.

A new Business Central Customers company will be created from a HubSpot Contact if it is connected to a HubSpot Deal that is synchronized into Business Central.

Once a link between a HubSpot Contact and a Business Central Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Business Central Customers company:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Business Central Customers company Property
     - Business Central Data Type
   * - id
     - id
     - "string"
   * - properties.address
     - addressLine1
     - "string"
   * - properties.city
     - city
     - "string"
   * - properties.country
     - country
     - "string"
   * - properties.zip
     - postalCode
     - "string"


HubSpot Contact to Business Central Customers person
----------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a Business Central Customers person must be established.

A new Business Central Customers person will be created from a HubSpot Contact if it is connected to a HubSpot Deal that is synchronized into Business Central.

Once a link between a HubSpot Contact and a Business Central Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Business Central Customers person:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Business Central Customers person Property
     - Business Central Data Type
   * - id
     - id
     - "string"
   * - properties.address
     - addressLine1
     - "string"
   * - properties.city
     - address.city
     - "string"
   * - properties.city
     - addressLine2
     - "string"
   * - properties.city
     - city
     - "string"
   * - properties.country
     - country
     - "string"
   * - properties.email
     - email
     - "string"
   * - properties.email
     - id (Dependant on having wd:Q1273217 in type)
     - "string"
   * - properties.phone
     - phoneNumber
     - "string"
   * - properties.zip
     - address.postalCode
     - "string"
   * - properties.zip
     - postalCode
     - "string"


HubSpot Company to Business Central Companies
---------------------------------------------
Every HubSpot Company will be synchronized with a Business Central Companies.

Once a link between a HubSpot Company and a Business Central Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Business Central Companies:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Business Central Companies Property
     - Business Central Data Type


HubSpot Deal to Business Central Salesorders
--------------------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a Business Central Salesorders.

Once a link between a HubSpot Deal and a Business Central Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Business Central Salesorders:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Business Central Salesorders Property
     - Business Central Data Type
   * - properties.amount
     - totalAmountExcludingTax
     - "string"
   * - properties.closedate
     - orderDate
     - N/A
   * - properties.closedate
     - requestedDeliveryDate
     - N/A
   * - properties.deal_currency_code
     - billToCountry
     - "string"
   * - properties.deal_currency_code
     - billingPostalAddress.countryLetterCode
     - "string"
   * - properties.deal_currency_code
     - currencyId
     - "string"
   * - properties.deal_currency_code
     - shipToCountry
     - "string"
   * - properties.deal_currency_code
     - shippingPostalAddress.countryLetterCode
     - "string"


HubSpot Lineitem to Business Central Salesorderlines
----------------------------------------------------
Every HubSpot Lineitem will be synchronized with a Business Central Salesorderlines.

Once a link between a HubSpot Lineitem and a Business Central Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a Business Central Salesorderlines:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - Business Central Salesorderlines Property
     - Business Central Data Type
   * - properties.description
     - description
     - "string"
   * - properties.hs_discount_percentage
     - discountPercent
     - N/A
   * - properties.hs_product_id
     - itemId
     - "string"
   * - properties.name
     - description
     - "string"
   * - properties.price
     - amountExcludingTax
     - "string"
   * - properties.price
     - unitPrice
     - "float"
   * - properties.quantity
     - invoiceQuantity
     - "string"
   * - properties.quantity
     - quantity
     - N/A


HubSpot Product to Business Central Items
-----------------------------------------
Every HubSpot Product will be synchronized with a Business Central Items.

Once a link between a HubSpot Product and a Business Central Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a Business Central Items:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - Business Central Items Property
     - Business Central Data Type
   * - properties.hs_cost_of_goods_sold
     - unitCost
     - N/A
   * - properties.name
     - displayName
     - "string"
   * - properties.name
     - displayName.string
     - "string"
   * - properties.name
     - displayName2
     - "string"
   * - properties.price
     - unitPrice
     - N/A

