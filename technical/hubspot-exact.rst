=========================
HubSpot to Exact Dataflow
=========================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Exact. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to Exact Accounts
---------------------------------
Every HubSpot Company will be synchronized with a Exact Accounts.

Once a link between a HubSpot Company and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Exact Accounts Property
     - Exact Data Type
   * - properties.address
     - AddressLine1
     - "string"
   * - properties.address2
     - AddressLine2
     - "string"
   * - properties.city
     - City
     - "string"
   * - properties.country
     - Country
     - "string"
   * - properties.name
     - Name
     - "string"
   * - properties.phone
     - Phone
     - "string"
   * - properties.website
     - Website
     - "string"
   * - properties.zip
     - Postcode
     - "string"


HubSpot Contact to Exact Contacts
---------------------------------
Every HubSpot Contact will be synchronized with a Exact Contacts.

Once a link between a HubSpot Contact and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Exact Contacts Property
     - Exact Data Type
   * - properties.city
     - City
     - "string"
   * - properties.country
     - Country
     - "string"
   * - properties.date_of_birth
     - BirthDate
     - "string"
   * - properties.email
     - Email
     - "string"
   * - properties.firstname
     - FirstName
     - "string"
   * - properties.lastname
     - LastName
     - "string"
   * - properties.mobilephone
     - Mobile
     - "string"
   * - properties.phone
     - Phone
     - "string"


HubSpot Contactcompanyassociation to Exact Contacts
---------------------------------------------------
Every HubSpot Contactcompanyassociation will be synchronized with a Exact Contacts.

Once a link between a HubSpot Contactcompanyassociation and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociation and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     - Exact Contacts Property
     - Exact Data Type


HubSpot Contactcompanyassociationtype to Exact Currencies
---------------------------------------------------------
Every HubSpot Contactcompanyassociationtype will be synchronized with a Exact Currencies.

Once a link between a HubSpot Contactcompanyassociationtype and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociationtype and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociationtype Property
     - Exact Currencies Property
     - Exact Data Type
   * - label
     - Description
     - "string"


HubSpot Deal to Exact Quotations
--------------------------------
Every HubSpot Deal will be synchronized with a Exact Quotations.

Once a link between a HubSpot Deal and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Exact Quotations Property
     - Exact Data Type
   * - properties.closedate
     - DeliveryDate
     - "string"
   * - properties.deal_currency_code
     - Currency
     - "string"
   * - properties.description
     - Description
     - "string"


HubSpot Dealcompanyassociation to Exact Quotations
--------------------------------------------------
Every HubSpot Dealcompanyassociation will be synchronized with a Exact Quotations.

Once a link between a HubSpot Dealcompanyassociation and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociation and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     - Exact Quotations Property
     - Exact Data Type


HubSpot Dealcompanyassociationtype to Exact Currencies
------------------------------------------------------
Every HubSpot Dealcompanyassociationtype will be synchronized with a Exact Currencies.

Once a link between a HubSpot Dealcompanyassociationtype and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociationtype and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociationtype Property
     - Exact Currencies Property
     - Exact Data Type
   * - label
     - Description
     - "string"


HubSpot Dealcontactassociation to Exact Quotations
--------------------------------------------------
Every HubSpot Dealcontactassociation will be synchronized with a Exact Quotations.

Once a link between a HubSpot Dealcontactassociation and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociation and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     - Exact Quotations Property
     - Exact Data Type


HubSpot Dealcontactassociationtype to Exact Currencies
------------------------------------------------------
Every HubSpot Dealcontactassociationtype will be synchronized with a Exact Currencies.

Once a link between a HubSpot Dealcontactassociationtype and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociationtype and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociationtype Property
     - Exact Currencies Property
     - Exact Data Type
   * - label
     - Description
     - "string"


HubSpot Lineitem to Exact Quotations
------------------------------------
Every HubSpot Lineitem will be synchronized with a Exact Quotations.

Once a link between a HubSpot Lineitem and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - Exact Quotations Property
     - Exact Data Type


HubSpot Lineitemdealassociation to Exact Quotations
---------------------------------------------------
Every HubSpot Lineitemdealassociation will be synchronized with a Exact Quotations.

Once a link between a HubSpot Lineitemdealassociation and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - Exact Quotations Property
     - Exact Data Type


HubSpot Lineitemdealassociationtype to Exact Currencies
-------------------------------------------------------
Every HubSpot Lineitemdealassociationtype will be synchronized with a Exact Currencies.

Once a link between a HubSpot Lineitemdealassociationtype and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociationtype and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociationtype Property
     - Exact Currencies Property
     - Exact Data Type
   * - label
     - Description
     - "string"


HubSpot Lineitemquoteassociation to Exact Quotations
----------------------------------------------------
Every HubSpot Lineitemquoteassociation will be synchronized with a Exact Quotations.

Once a link between a HubSpot Lineitemquoteassociation and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociation and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociation Property
     - Exact Quotations Property
     - Exact Data Type


HubSpot Lineitemquoteassociationtype to Exact Currencies
--------------------------------------------------------
Every HubSpot Lineitemquoteassociationtype will be synchronized with a Exact Currencies.

Once a link between a HubSpot Lineitemquoteassociationtype and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociationtype and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociationtype Property
     - Exact Currencies Property
     - Exact Data Type
   * - label
     - Description
     - "string"


HubSpot Quotecompanyassociation to Exact Quotations
---------------------------------------------------
Every HubSpot Quotecompanyassociation will be synchronized with a Exact Quotations.

Once a link between a HubSpot Quotecompanyassociation and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociation and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     - Exact Quotations Property
     - Exact Data Type


HubSpot Quotecompanyassociationtype to Exact Currencies
-------------------------------------------------------
Every HubSpot Quotecompanyassociationtype will be synchronized with a Exact Currencies.

Once a link between a HubSpot Quotecompanyassociationtype and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociationtype and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociationtype Property
     - Exact Currencies Property
     - Exact Data Type
   * - label
     - Description
     - "string"


HubSpot Quotecontactassociation to Exact Quotations
---------------------------------------------------
Every HubSpot Quotecontactassociation will be synchronized with a Exact Quotations.

Once a link between a HubSpot Quotecontactassociation and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociation and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     - Exact Quotations Property
     - Exact Data Type


HubSpot Quotecontactassociationtype to Exact Currencies
-------------------------------------------------------
Every HubSpot Quotecontactassociationtype will be synchronized with a Exact Currencies.

Once a link between a HubSpot Quotecontactassociationtype and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociationtype and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociationtype Property
     - Exact Currencies Property
     - Exact Data Type
   * - label
     - Description
     - "string"


HubSpot Quotedealassociation to Exact Quotations
------------------------------------------------
Every HubSpot Quotedealassociation will be synchronized with a Exact Quotations.

Once a link between a HubSpot Quotedealassociation and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociation and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     - Exact Quotations Property
     - Exact Data Type


HubSpot Quotedealassociationtype to Exact Currencies
----------------------------------------------------
Every HubSpot Quotedealassociationtype will be synchronized with a Exact Currencies.

Once a link between a HubSpot Quotedealassociationtype and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociationtype and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociationtype Property
     - Exact Currencies Property
     - Exact Data Type
   * - label
     - Description
     - "string"


HubSpot Quotequotetemplateassociation to Exact Quotations
---------------------------------------------------------
Every HubSpot Quotequotetemplateassociation will be synchronized with a Exact Quotations.

Once a link between a HubSpot Quotequotetemplateassociation and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociation and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     - Exact Quotations Property
     - Exact Data Type


HubSpot Quotequotetemplateassociationtype to Exact Currencies
-------------------------------------------------------------
Every HubSpot Quotequotetemplateassociationtype will be synchronized with a Exact Currencies.

Once a link between a HubSpot Quotequotetemplateassociationtype and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociationtype and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociationtype Property
     - Exact Currencies Property
     - Exact Data Type
   * - label
     - Description
     - "string"


HubSpot User to Exact Contacts
------------------------------
Every HubSpot User will be synchronized with a Exact Contacts.

Once a link between a HubSpot User and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - Exact Contacts Property
     - Exact Data Type
   * - email
     - BusinessEmail
     - "string"


HubSpot Account to Exact Currencies
-----------------------------------
Every HubSpot Account will be synchronized with a Exact Currencies.

Once a link between a HubSpot Account and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Account and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Account Property
     - Exact Currencies Property
     - Exact Data Type
   * - accountType
     - Code
     - "string"


HubSpot Contact to Exact Addresses
----------------------------------
Every HubSpot Contact will be synchronized with a Exact Addresses.

Once a link between a HubSpot Contact and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Exact Addresses Property
     - Exact Data Type
   * - properties.address
     - AddressLine1
     - "string"
   * - properties.city
     - City
     - "string"
   * - properties.country
     - Country
     - "string"


HubSpot Deal to Exact Currencies
--------------------------------
Every HubSpot Deal will be synchronized with a Exact Currencies.

Once a link between a HubSpot Deal and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Exact Currencies Property
     - Exact Data Type
   * - properties.deal_currency_code
     - Code
     - "string"


HubSpot Deal to Exact Salesorders
---------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a Exact Salesorders.

Once a link between a HubSpot Deal and a Exact Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Exact Salesorders:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Exact Salesorders Property
     - Exact Data Type
   * - properties.closedate
     - DeliveryDate
     - "string"
   * - properties.closedate
     - OrderDate
     - "string"
   * - properties.deal_currency_code
     - Currency
     - "string"
   * - properties.description
     - Description
     - "string"


HubSpot Lineitem to Exact Salesorderlines
-----------------------------------------
Every HubSpot Lineitem will be synchronized with a Exact Salesorderlines.

Once a link between a HubSpot Lineitem and a Exact Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a Exact Salesorderlines:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - Exact Salesorderlines Property
     - Exact Data Type
   * - properties.hs_product_id
     - Item
     - "string"


HubSpot Product to Exact Items
------------------------------
Every HubSpot Product will be synchronized with a Exact Items.

Once a link between a HubSpot Product and a Exact Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a Exact Items:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - Exact Items Property
     - Exact Data Type


HubSpot Quote to Exact Quotations
---------------------------------
Every HubSpot Quote will be synchronized with a Exact Quotations.

Once a link between a HubSpot Quote and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - Exact Quotations Property
     - Exact Data Type
   * - properties.hs_expiration_date
     - CloseDate
     - "string"

