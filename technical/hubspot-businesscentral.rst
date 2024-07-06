===================================
HubSpot to Businesscentral Dataflow
===================================

Generated: 2024-07-06 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Businesscentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to Businesscentral Customers company
----------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a Businesscentral Customers company must be established.

A new Businesscentral Customers company will be created from a HubSpot Company if it is connected to a HubSpot Deal that is synchronized into Businesscentral.

Once a link between a HubSpot Company and a Businesscentral Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Businesscentral Customers company:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Businesscentral Customers company Property
     - Businesscentral Data Type
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


HubSpot Company to Businesscentral Customers person
---------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a Businesscentral Customers person must be established.

A new Businesscentral Customers person will be created from a HubSpot Company if it is connected to a HubSpot Deal that is synchronized into Businesscentral.

Once a link between a HubSpot Company and a Businesscentral Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Businesscentral Customers person:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Businesscentral Customers person Property
     - Businesscentral Data Type


HubSpot Contact to Businesscentral Customers company
----------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a Businesscentral Customers company must be established.

A new Businesscentral Customers company will be created from a HubSpot Contact if it is connected to a HubSpot Deal that is synchronized into Businesscentral.

Once a link between a HubSpot Contact and a Businesscentral Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Businesscentral Customers company:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Businesscentral Customers company Property
     - Businesscentral Data Type
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


HubSpot Contact to Businesscentral Customers person
---------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a Businesscentral Customers person must be established.

A new Businesscentral Customers person will be created from a HubSpot Contact if it is connected to a HubSpot Deal that is synchronized into Businesscentral.

Once a link between a HubSpot Contact and a Businesscentral Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Businesscentral Customers person:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Businesscentral Customers person Property
     - Businesscentral Data Type
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


HubSpot Company to Businesscentral Companies
--------------------------------------------
Every HubSpot Company will be synchronized with a Businesscentral Companies.

Once a link between a HubSpot Company and a Businesscentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Businesscentral Companies:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Businesscentral Companies Property
     - Businesscentral Data Type


HubSpot Deal to Businesscentral Salesorders
-------------------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a Businesscentral Salesorders.

Once a link between a HubSpot Deal and a Businesscentral Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Businesscentral Salesorders:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Businesscentral Salesorders Property
     - Businesscentral Data Type
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


HubSpot Lineitem to Businesscentral Salesorderlines
---------------------------------------------------
Every HubSpot Lineitem will be synchronized with a Businesscentral Salesorderlines.

Once a link between a HubSpot Lineitem and a Businesscentral Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a Businesscentral Salesorderlines:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - Businesscentral Salesorderlines Property
     - Businesscentral Data Type
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


HubSpot Product to Businesscentral Items
----------------------------------------
Every HubSpot Product will be synchronized with a Businesscentral Items.

Once a link between a HubSpot Product and a Businesscentral Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a Businesscentral Items:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - Businesscentral Items Property
     - Businesscentral Data Type
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

