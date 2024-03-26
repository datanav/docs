====================
HubSpot to  Dataflow
====================

Generated: 2024-03-26 00:00:19

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to  Customers company
-------------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a  Customers company must be established.

A new  Customers company will be created from a HubSpot Company if it is connected to a HubSpot Deal that is synchronized into .

Once a link between a HubSpot Company and a  Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a  Customers company:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     -  Customers company Property
     -  Data Type
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


HubSpot Company to  Customers person
------------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a  Customers person must be established.

A new  Customers person will be created from a HubSpot Company if it is connected to a HubSpot Deal that is synchronized into .

Once a link between a HubSpot Company and a  Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a  Customers person:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     -  Customers person Property
     -  Data Type


HubSpot Contact to  Customers company
-------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a  Customers company must be established.

A new  Customers company will be created from a HubSpot Contact if it is connected to a HubSpot Deal that is synchronized into .

Once a link between a HubSpot Contact and a  Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a  Customers company:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     -  Customers company Property
     -  Data Type
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


HubSpot Contact to  Customers person
------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a  Customers person must be established.

A new  Customers person will be created from a HubSpot Contact if it is connected to a HubSpot Deal that is synchronized into .

Once a link between a HubSpot Contact and a  Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a  Customers person:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     -  Customers person Property
     -  Data Type
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


HubSpot Company to  Companies
-----------------------------
Every HubSpot Company will be synchronized with a  Companies.

Once a link between a HubSpot Company and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a  Companies:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     -  Companies Property
     -  Data Type


HubSpot Deal to  Salesorders
----------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a  Salesorders.

Once a link between a HubSpot Deal and a  Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a  Salesorders:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     -  Salesorders Property
     -  Data Type
   * - properties.amount
     - totalAmountExcludingTax
     - "string"
   * - properties.closedate
     - orderDate
     - "datetime-parse", "%Y-%m-%dT%H:%M:%S.%fZ"
   * - properties.closedate
     - requestedDeliveryDate
     - "datetime-parse", "%Y-%m-%dT%H:%M:%S.%fZ"
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


HubSpot Lineitem to  Salesorderlines
------------------------------------
Every HubSpot Lineitem will be synchronized with a  Salesorderlines.

Once a link between a HubSpot Lineitem and a  Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a  Salesorderlines:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     -  Salesorderlines Property
     -  Data Type
   * - properties.description
     - description
     - "string"
   * - properties.hs_discount_percentage
     - discountPercent
     - "decimal"
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
     - "integer", "decimal"]


HubSpot Product to  Items
-------------------------
Every HubSpot Product will be synchronized with a  Items.

Once a link between a HubSpot Product and a  Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a  Items:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     -  Items Property
     -  Data Type
   * - properties.hs_cost_of_goods_sold
     - unitCost
     - "decimal"
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
     - "decimal"

