===================================
HubSpot to BusinessCentral Dataflow
===================================

Generated: 2024-09-11 09:30:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to BusinessCentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to BusinessCentral Customers company
----------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a BusinessCentral Customers company must be established.

A new BusinessCentral Customers company will be created from a HubSpot Company if it is connected to a HubSpot Deal that is synchronized into BusinessCentral.

Once a link between a HubSpot Company and a BusinessCentral Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a BusinessCentral Customers company:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - BusinessCentral Customers company Property
     - BusinessCentral Data Type
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


HubSpot Company to BusinessCentral Customers person
---------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a BusinessCentral Customers person must be established.

A new BusinessCentral Customers person will be created from a HubSpot Company if it is connected to a HubSpot Deal that is synchronized into BusinessCentral.

Once a link between a HubSpot Company and a BusinessCentral Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a BusinessCentral Customers person:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - BusinessCentral Customers person Property
     - BusinessCentral Data Type


HubSpot Contact to BusinessCentral Customers company
----------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a BusinessCentral Customers company must be established.

A new BusinessCentral Customers company will be created from a HubSpot Contact if it is connected to a HubSpot Deal that is synchronized into BusinessCentral.

Once a link between a HubSpot Contact and a BusinessCentral Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a BusinessCentral Customers company:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - BusinessCentral Customers company Property
     - BusinessCentral Data Type
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


HubSpot Contact to BusinessCentral Customers person
---------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a BusinessCentral Customers person must be established.

A new BusinessCentral Customers person will be created from a HubSpot Contact if it is connected to a HubSpot Deal that is synchronized into BusinessCentral.

Once a link between a HubSpot Contact and a BusinessCentral Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a BusinessCentral Customers person:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - BusinessCentral Customers person Property
     - BusinessCentral Data Type
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


HubSpot Company to BusinessCentral Companies
--------------------------------------------
Every HubSpot Company will be synchronized with a BusinessCentral Companies.

Once a link between a HubSpot Company and a BusinessCentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a BusinessCentral Companies:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - BusinessCentral Companies Property
     - BusinessCentral Data Type


HubSpot Deal to BusinessCentral Salesorders
-------------------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a BusinessCentral Salesorders.

Once a link between a HubSpot Deal and a BusinessCentral Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a BusinessCentral Salesorders:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - BusinessCentral Salesorders Property
     - BusinessCentral Data Type
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


HubSpot Lineitem to BusinessCentral Salesorderlines
---------------------------------------------------
Every HubSpot Lineitem will be synchronized with a BusinessCentral Salesorderlines.

Once a link between a HubSpot Lineitem and a BusinessCentral Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a BusinessCentral Salesorderlines:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - BusinessCentral Salesorderlines Property
     - BusinessCentral Data Type
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


HubSpot Product to BusinessCentral Items
----------------------------------------
Every HubSpot Product will be synchronized with a BusinessCentral Items.

Once a link between a HubSpot Product and a BusinessCentral Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a BusinessCentral Items:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - BusinessCentral Items Property
     - BusinessCentral Data Type
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

