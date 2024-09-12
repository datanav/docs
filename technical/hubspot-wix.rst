=======================
HubSpot to Wix Dataflow
=======================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Contact to Wix Contacts
-------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a Wix Contacts must be established.

A new Wix Contacts will be created from a HubSpot Contact if it is connected to a HubSpot Deal, Quote, Lineitem, Quotedealassociation, Dealcompanyassociation, Dealcontactassociation, Lineitemdealassociation, Quotecompanyassociation, Quotecontactassociation, Lineitemquoteassociation, Ticketcompanyassociation, or Quotequotetemplateassociation that is synchronized into Wix.

A HubSpot Contact will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Wix Contacts Property
   * - properties.email
     - primaryInfo.email

Once a link between a HubSpot Contact and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Wix Contacts Property
     - Wix Data Type
   * - id
     - id
     - "string"
   * - properties.address
     - info.addresses.items.address.addressLine
     - "string"
   * - properties.city
     - info.addresses.items.address.city
     - "string"
   * - properties.email
     - info.emails
     - "string"
   * - properties.email
     - primaryInfo.email
     - "string"
   * - properties.firstname
     - info.name.first
     - "string"
   * - properties.lastname
     - info.name.last
     - "string"
   * - properties.mobilephone
     - info.phones
     - "string"
   * - properties.mobilephone
     - primaryInfo.phone
     - "string"
   * - properties.phone
     - primaryInfo.phone
     - "string"
   * - properties.zip
     - info.addresses.items.address.postalCode
     - "string"


HubSpot Contact to Wix Members
------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a Wix Members must be established.

A HubSpot Contact will merge with a Wix Members if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Wix Members Property
   * - properties.email
     - loginEmail

Once a link between a HubSpot Contact and a Wix Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Wix Members:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Wix Members Property
     - Wix Data Type
   * - properties.email
     - loginEmail
     - "string"


HubSpot Company to Wix Contacts
-------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a Wix Contacts must be established.

A new Wix Contacts will be created from a HubSpot Company if it is connected to a HubSpot Deal, Quote, Lineitem, Quotedealassociation, Dealcompanyassociation, Dealcontactassociation, Lineitemdealassociation, Quotecompanyassociation, Quotecontactassociation, Lineitemquoteassociation, Ticketcompanyassociation, or Quotequotetemplateassociation that is synchronized into Wix.

Once a link between a HubSpot Company and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Wix Contacts Property
     - Wix Data Type
   * - id
     - id
     - "string"
   * - properties.address
     - info.addresses.items.address.addressLine
     - "string"
   * - properties.address2
     - info.addresses.items.address.addressLine2
     - "string"
   * - properties.city
     - info.addresses.items.address.city
     - "string"
   * - properties.country
     - info.addresses.items.address.countryFullname
     - "string"
   * - properties.industry
     - info.addresses.items.address.countryFullname
     - "string"
   * - properties.state
     - info.addresses.items.address.countryFullname
     - "string"
   * - properties.type
     - info.addresses.items.address.countryFullname
     - "string"
   * - properties.zip
     - info.addresses.items.address.postalCode
     - "string"


HubSpot Account to Wix Currencies
---------------------------------
Every HubSpot Account will be synchronized with a Wix Currencies.

If a matching Wix Currencies already exists, the HubSpot Account will be merged with the existing one.
If no matching Wix Currencies is found, a new Wix Currencies will be created.

A HubSpot Account will merge with a Wix Currencies if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Account Property
     - Wix Currencies Property
   * - companyCurrency
     - code

Once a link between a HubSpot Account and a Wix Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Account and a Wix Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Account Property
     - Wix Currencies Property
     - Wix Data Type


HubSpot Deal to Wix Currencies
------------------------------
Every HubSpot Deal will be synchronized with a Wix Currencies.

If a matching Wix Currencies already exists, the HubSpot Deal will be merged with the existing one.
If no matching Wix Currencies is found, a new Wix Currencies will be created.

A HubSpot Deal will merge with a Wix Currencies if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Wix Currencies Property
   * - properties.deal_currency_code
     - code

Once a link between a HubSpot Deal and a Wix Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Wix Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Wix Currencies Property
     - Wix Data Type


HubSpot Deal to Wix Orders
--------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a Wix Orders.

Once a link between a HubSpot Deal and a Wix Orders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Wix Orders:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Wix Orders Property
     - Wix Data Type
   * - properties.amount
     - totals.total
     - "string"
   * - properties.deal_currency_code
     - currency
     - "string"


HubSpot Product to Wix Products
-------------------------------
Every HubSpot Product will be synchronized with a Wix Products.

Once a link between a HubSpot Product and a Wix Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a Wix Products:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - Wix Products Property
     - Wix Data Type
   * - properties.description
     - description
     - "string"
   * - properties.hs_cost_of_goods_sold
     - costAndProfitData.itemCost
     - N/A
   * - properties.hs_cost_of_goods_sold
     - costRange.maxValue
     - "string"
   * - properties.hs_sku
     - sku
     - "string"
   * - properties.name
     - name
     - "string"
   * - properties.price
     - price.price
     - "string"
   * - properties.price
     - priceData.price
     - N/A

