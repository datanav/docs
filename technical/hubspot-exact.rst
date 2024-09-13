================================
HubSpot to Exact Online Dataflow
================================

Generated: 2024-09-13 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Exact Online. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to Exact Online Accounts
----------------------------------------
Every HubSpot Company will be synchronized with a Exact Online Accounts.

Once a link between a HubSpot Company and a Exact Online Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Exact Online Accounts:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Exact Online Accounts Property
     - Exact Online Data Type
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


HubSpot Contact to Exact Online Contacts
----------------------------------------
Every HubSpot Contact will be synchronized with a Exact Online Contacts.

Once a link between a HubSpot Contact and a Exact Online Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Exact Online Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Exact Online Contacts Property
     - Exact Online Data Type
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


HubSpot Contactcompanyassociation to Exact Online Contacts
----------------------------------------------------------
Every HubSpot Contactcompanyassociation will be synchronized with a Exact Online Contacts.

Once a link between a HubSpot Contactcompanyassociation and a Exact Online Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociation and a Exact Online Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     - Exact Online Contacts Property
     - Exact Online Data Type


HubSpot Contactcompanyassociationtype to Exact Online Currencies
----------------------------------------------------------------
Every HubSpot Contactcompanyassociationtype will be synchronized with a Exact Online Currencies.

Once a link between a HubSpot Contactcompanyassociationtype and a Exact Online Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociationtype and a Exact Online Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociationtype Property
     - Exact Online Currencies Property
     - Exact Online Data Type
   * - label
     - Description
     - "string"


HubSpot Deal to Exact Online Quotations
---------------------------------------
Every HubSpot Deal will be synchronized with a Exact Online Quotations.

Once a link between a HubSpot Deal and a Exact Online Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Exact Online Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Exact Online Quotations Property
     - Exact Online Data Type
   * - properties.closedate
     - DeliveryDate
     - "string"
   * - properties.deal_currency_code
     - Currency
     - "string"
   * - properties.description
     - Description
     - "string"


HubSpot Dealcompanyassociation to Exact Online Quotations
---------------------------------------------------------
Every HubSpot Dealcompanyassociation will be synchronized with a Exact Online Quotations.

Once a link between a HubSpot Dealcompanyassociation and a Exact Online Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociation and a Exact Online Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     - Exact Online Quotations Property
     - Exact Online Data Type


HubSpot Dealcompanyassociationtype to Exact Online Currencies
-------------------------------------------------------------
Every HubSpot Dealcompanyassociationtype will be synchronized with a Exact Online Currencies.

Once a link between a HubSpot Dealcompanyassociationtype and a Exact Online Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociationtype and a Exact Online Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociationtype Property
     - Exact Online Currencies Property
     - Exact Online Data Type
   * - label
     - Description
     - "string"


HubSpot Dealcontactassociation to Exact Online Quotations
---------------------------------------------------------
Every HubSpot Dealcontactassociation will be synchronized with a Exact Online Quotations.

Once a link between a HubSpot Dealcontactassociation and a Exact Online Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociation and a Exact Online Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     - Exact Online Quotations Property
     - Exact Online Data Type


HubSpot Dealcontactassociationtype to Exact Online Currencies
-------------------------------------------------------------
Every HubSpot Dealcontactassociationtype will be synchronized with a Exact Online Currencies.

Once a link between a HubSpot Dealcontactassociationtype and a Exact Online Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociationtype and a Exact Online Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociationtype Property
     - Exact Online Currencies Property
     - Exact Online Data Type
   * - label
     - Description
     - "string"


HubSpot Lineitem to Exact Online Quotations
-------------------------------------------
Every HubSpot Lineitem will be synchronized with a Exact Online Quotations.

Once a link between a HubSpot Lineitem and a Exact Online Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a Exact Online Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - Exact Online Quotations Property
     - Exact Online Data Type


HubSpot Lineitemdealassociation to Exact Online Quotations
----------------------------------------------------------
Every HubSpot Lineitemdealassociation will be synchronized with a Exact Online Quotations.

Once a link between a HubSpot Lineitemdealassociation and a Exact Online Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a Exact Online Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - Exact Online Quotations Property
     - Exact Online Data Type


HubSpot Lineitemdealassociationtype to Exact Online Currencies
--------------------------------------------------------------
Every HubSpot Lineitemdealassociationtype will be synchronized with a Exact Online Currencies.

Once a link between a HubSpot Lineitemdealassociationtype and a Exact Online Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociationtype and a Exact Online Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociationtype Property
     - Exact Online Currencies Property
     - Exact Online Data Type
   * - label
     - Description
     - "string"


HubSpot Lineitemquoteassociation to Exact Online Quotations
-----------------------------------------------------------
Every HubSpot Lineitemquoteassociation will be synchronized with a Exact Online Quotations.

Once a link between a HubSpot Lineitemquoteassociation and a Exact Online Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociation and a Exact Online Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociation Property
     - Exact Online Quotations Property
     - Exact Online Data Type


HubSpot Lineitemquoteassociationtype to Exact Online Currencies
---------------------------------------------------------------
Every HubSpot Lineitemquoteassociationtype will be synchronized with a Exact Online Currencies.

Once a link between a HubSpot Lineitemquoteassociationtype and a Exact Online Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociationtype and a Exact Online Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociationtype Property
     - Exact Online Currencies Property
     - Exact Online Data Type
   * - label
     - Description
     - "string"


HubSpot Quotecompanyassociation to Exact Online Quotations
----------------------------------------------------------
Every HubSpot Quotecompanyassociation will be synchronized with a Exact Online Quotations.

Once a link between a HubSpot Quotecompanyassociation and a Exact Online Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociation and a Exact Online Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     - Exact Online Quotations Property
     - Exact Online Data Type


HubSpot Quotecompanyassociationtype to Exact Online Currencies
--------------------------------------------------------------
Every HubSpot Quotecompanyassociationtype will be synchronized with a Exact Online Currencies.

Once a link between a HubSpot Quotecompanyassociationtype and a Exact Online Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociationtype and a Exact Online Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociationtype Property
     - Exact Online Currencies Property
     - Exact Online Data Type
   * - label
     - Description
     - "string"


HubSpot Quotecontactassociation to Exact Online Quotations
----------------------------------------------------------
Every HubSpot Quotecontactassociation will be synchronized with a Exact Online Quotations.

Once a link between a HubSpot Quotecontactassociation and a Exact Online Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociation and a Exact Online Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     - Exact Online Quotations Property
     - Exact Online Data Type


HubSpot Quotecontactassociationtype to Exact Online Currencies
--------------------------------------------------------------
Every HubSpot Quotecontactassociationtype will be synchronized with a Exact Online Currencies.

Once a link between a HubSpot Quotecontactassociationtype and a Exact Online Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociationtype and a Exact Online Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociationtype Property
     - Exact Online Currencies Property
     - Exact Online Data Type
   * - label
     - Description
     - "string"


HubSpot Quotedealassociation to Exact Online Quotations
-------------------------------------------------------
Every HubSpot Quotedealassociation will be synchronized with a Exact Online Quotations.

Once a link between a HubSpot Quotedealassociation and a Exact Online Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociation and a Exact Online Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     - Exact Online Quotations Property
     - Exact Online Data Type


HubSpot Quotedealassociationtype to Exact Online Currencies
-----------------------------------------------------------
Every HubSpot Quotedealassociationtype will be synchronized with a Exact Online Currencies.

Once a link between a HubSpot Quotedealassociationtype and a Exact Online Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociationtype and a Exact Online Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociationtype Property
     - Exact Online Currencies Property
     - Exact Online Data Type
   * - label
     - Description
     - "string"


HubSpot Quotequotetemplateassociation to Exact Online Quotations
----------------------------------------------------------------
Every HubSpot Quotequotetemplateassociation will be synchronized with a Exact Online Quotations.

Once a link between a HubSpot Quotequotetemplateassociation and a Exact Online Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociation and a Exact Online Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     - Exact Online Quotations Property
     - Exact Online Data Type


HubSpot Quotequotetemplateassociationtype to Exact Online Currencies
--------------------------------------------------------------------
Every HubSpot Quotequotetemplateassociationtype will be synchronized with a Exact Online Currencies.

Once a link between a HubSpot Quotequotetemplateassociationtype and a Exact Online Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociationtype and a Exact Online Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociationtype Property
     - Exact Online Currencies Property
     - Exact Online Data Type
   * - label
     - Description
     - "string"


HubSpot User to Exact Online Contacts
-------------------------------------
Every HubSpot User will be synchronized with a Exact Online Contacts.

Once a link between a HubSpot User and a Exact Online Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a Exact Online Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - Exact Online Contacts Property
     - Exact Online Data Type
   * - email
     - BusinessEmail
     - "string"


HubSpot Account to Exact Online Currencies
------------------------------------------
Every HubSpot Account will be synchronized with a Exact Online Currencies.

Once a link between a HubSpot Account and a Exact Online Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Account and a Exact Online Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Account Property
     - Exact Online Currencies Property
     - Exact Online Data Type
   * - accountType
     - Code
     - "string"


HubSpot Contact to Exact Online Addresses
-----------------------------------------
Every HubSpot Contact will be synchronized with a Exact Online Addresses.

Once a link between a HubSpot Contact and a Exact Online Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Exact Online Addresses:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Exact Online Addresses Property
     - Exact Online Data Type
   * - properties.address
     - AddressLine1
     - "string"
   * - properties.city
     - City
     - "string"
   * - properties.country
     - Country
     - "string"


HubSpot Deal to Exact Online Currencies
---------------------------------------
Every HubSpot Deal will be synchronized with a Exact Online Currencies.

Once a link between a HubSpot Deal and a Exact Online Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Exact Online Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Exact Online Currencies Property
     - Exact Online Data Type
   * - properties.deal_currency_code
     - Code
     - "string"


HubSpot Deal to Exact Online Salesorders
----------------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a Exact Online Salesorders.

Once a link between a HubSpot Deal and a Exact Online Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Exact Online Salesorders:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Exact Online Salesorders Property
     - Exact Online Data Type
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


HubSpot Lineitem to Exact Online Salesorderlines
------------------------------------------------
Every HubSpot Lineitem will be synchronized with a Exact Online Salesorderlines.

Once a link between a HubSpot Lineitem and a Exact Online Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a Exact Online Salesorderlines:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - Exact Online Salesorderlines Property
     - Exact Online Data Type
   * - properties.hs_product_id
     - Item
     - "string"


HubSpot Product to Exact Online Items
-------------------------------------
Every HubSpot Product will be synchronized with a Exact Online Items.

Once a link between a HubSpot Product and a Exact Online Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a Exact Online Items:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - Exact Online Items Property
     - Exact Online Data Type


HubSpot Quote to Exact Online Quotations
----------------------------------------
Every HubSpot Quote will be synchronized with a Exact Online Quotations.

Once a link between a HubSpot Quote and a Exact Online Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a Exact Online Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - Exact Online Quotations Property
     - Exact Online Data Type
   * - properties.hs_expiration_date
     - CloseDate
     - "string"

