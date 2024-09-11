===============================
HubSpot to ExactOnline Dataflow
===============================

Generated: 2024-09-11 09:30:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to ExactOnline. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to ExactOnline Accounts
---------------------------------------
Every HubSpot Company will be synchronized with a ExactOnline Accounts.

Once a link between a HubSpot Company and a ExactOnline Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a ExactOnline Accounts:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - ExactOnline Accounts Property
     - ExactOnline Data Type
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


HubSpot Contact to ExactOnline Contacts
---------------------------------------
Every HubSpot Contact will be synchronized with a ExactOnline Contacts.

Once a link between a HubSpot Contact and a ExactOnline Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a ExactOnline Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - ExactOnline Contacts Property
     - ExactOnline Data Type
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


HubSpot Contactcompanyassociation to ExactOnline Contacts
---------------------------------------------------------
Every HubSpot Contactcompanyassociation will be synchronized with a ExactOnline Contacts.

Once a link between a HubSpot Contactcompanyassociation and a ExactOnline Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociation and a ExactOnline Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     - ExactOnline Contacts Property
     - ExactOnline Data Type


HubSpot Contactcompanyassociationtype to ExactOnline Currencies
---------------------------------------------------------------
Every HubSpot Contactcompanyassociationtype will be synchronized with a ExactOnline Currencies.

Once a link between a HubSpot Contactcompanyassociationtype and a ExactOnline Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociationtype and a ExactOnline Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociationtype Property
     - ExactOnline Currencies Property
     - ExactOnline Data Type
   * - label
     - Description
     - "string"


HubSpot Deal to ExactOnline Quotations
--------------------------------------
Every HubSpot Deal will be synchronized with a ExactOnline Quotations.

Once a link between a HubSpot Deal and a ExactOnline Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a ExactOnline Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - ExactOnline Quotations Property
     - ExactOnline Data Type
   * - properties.closedate
     - DeliveryDate
     - "string"
   * - properties.deal_currency_code
     - Currency
     - "string"
   * - properties.description
     - Description
     - "string"


HubSpot Dealcompanyassociation to ExactOnline Quotations
--------------------------------------------------------
Every HubSpot Dealcompanyassociation will be synchronized with a ExactOnline Quotations.

Once a link between a HubSpot Dealcompanyassociation and a ExactOnline Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociation and a ExactOnline Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     - ExactOnline Quotations Property
     - ExactOnline Data Type


HubSpot Dealcompanyassociationtype to ExactOnline Currencies
------------------------------------------------------------
Every HubSpot Dealcompanyassociationtype will be synchronized with a ExactOnline Currencies.

Once a link between a HubSpot Dealcompanyassociationtype and a ExactOnline Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociationtype and a ExactOnline Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociationtype Property
     - ExactOnline Currencies Property
     - ExactOnline Data Type
   * - label
     - Description
     - "string"


HubSpot Dealcontactassociation to ExactOnline Quotations
--------------------------------------------------------
Every HubSpot Dealcontactassociation will be synchronized with a ExactOnline Quotations.

Once a link between a HubSpot Dealcontactassociation and a ExactOnline Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociation and a ExactOnline Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     - ExactOnline Quotations Property
     - ExactOnline Data Type


HubSpot Dealcontactassociationtype to ExactOnline Currencies
------------------------------------------------------------
Every HubSpot Dealcontactassociationtype will be synchronized with a ExactOnline Currencies.

Once a link between a HubSpot Dealcontactassociationtype and a ExactOnline Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociationtype and a ExactOnline Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociationtype Property
     - ExactOnline Currencies Property
     - ExactOnline Data Type
   * - label
     - Description
     - "string"


HubSpot Lineitem to ExactOnline Quotations
------------------------------------------
Every HubSpot Lineitem will be synchronized with a ExactOnline Quotations.

Once a link between a HubSpot Lineitem and a ExactOnline Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a ExactOnline Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - ExactOnline Quotations Property
     - ExactOnline Data Type


HubSpot Lineitemdealassociation to ExactOnline Quotations
---------------------------------------------------------
Every HubSpot Lineitemdealassociation will be synchronized with a ExactOnline Quotations.

Once a link between a HubSpot Lineitemdealassociation and a ExactOnline Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a ExactOnline Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - ExactOnline Quotations Property
     - ExactOnline Data Type


HubSpot Lineitemdealassociationtype to ExactOnline Currencies
-------------------------------------------------------------
Every HubSpot Lineitemdealassociationtype will be synchronized with a ExactOnline Currencies.

Once a link between a HubSpot Lineitemdealassociationtype and a ExactOnline Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociationtype and a ExactOnline Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociationtype Property
     - ExactOnline Currencies Property
     - ExactOnline Data Type
   * - label
     - Description
     - "string"


HubSpot Lineitemquoteassociation to ExactOnline Quotations
----------------------------------------------------------
Every HubSpot Lineitemquoteassociation will be synchronized with a ExactOnline Quotations.

Once a link between a HubSpot Lineitemquoteassociation and a ExactOnline Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociation and a ExactOnline Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociation Property
     - ExactOnline Quotations Property
     - ExactOnline Data Type


HubSpot Lineitemquoteassociationtype to ExactOnline Currencies
--------------------------------------------------------------
Every HubSpot Lineitemquoteassociationtype will be synchronized with a ExactOnline Currencies.

Once a link between a HubSpot Lineitemquoteassociationtype and a ExactOnline Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociationtype and a ExactOnline Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociationtype Property
     - ExactOnline Currencies Property
     - ExactOnline Data Type
   * - label
     - Description
     - "string"


HubSpot Quotecompanyassociation to ExactOnline Quotations
---------------------------------------------------------
Every HubSpot Quotecompanyassociation will be synchronized with a ExactOnline Quotations.

Once a link between a HubSpot Quotecompanyassociation and a ExactOnline Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociation and a ExactOnline Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     - ExactOnline Quotations Property
     - ExactOnline Data Type


HubSpot Quotecompanyassociationtype to ExactOnline Currencies
-------------------------------------------------------------
Every HubSpot Quotecompanyassociationtype will be synchronized with a ExactOnline Currencies.

Once a link between a HubSpot Quotecompanyassociationtype and a ExactOnline Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociationtype and a ExactOnline Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociationtype Property
     - ExactOnline Currencies Property
     - ExactOnline Data Type
   * - label
     - Description
     - "string"


HubSpot Quotecontactassociation to ExactOnline Quotations
---------------------------------------------------------
Every HubSpot Quotecontactassociation will be synchronized with a ExactOnline Quotations.

Once a link between a HubSpot Quotecontactassociation and a ExactOnline Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociation and a ExactOnline Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     - ExactOnline Quotations Property
     - ExactOnline Data Type


HubSpot Quotecontactassociationtype to ExactOnline Currencies
-------------------------------------------------------------
Every HubSpot Quotecontactassociationtype will be synchronized with a ExactOnline Currencies.

Once a link between a HubSpot Quotecontactassociationtype and a ExactOnline Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociationtype and a ExactOnline Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociationtype Property
     - ExactOnline Currencies Property
     - ExactOnline Data Type
   * - label
     - Description
     - "string"


HubSpot Quotedealassociation to ExactOnline Quotations
------------------------------------------------------
Every HubSpot Quotedealassociation will be synchronized with a ExactOnline Quotations.

Once a link between a HubSpot Quotedealassociation and a ExactOnline Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociation and a ExactOnline Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     - ExactOnline Quotations Property
     - ExactOnline Data Type


HubSpot Quotedealassociationtype to ExactOnline Currencies
----------------------------------------------------------
Every HubSpot Quotedealassociationtype will be synchronized with a ExactOnline Currencies.

Once a link between a HubSpot Quotedealassociationtype and a ExactOnline Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociationtype and a ExactOnline Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociationtype Property
     - ExactOnline Currencies Property
     - ExactOnline Data Type
   * - label
     - Description
     - "string"


HubSpot Quotequotetemplateassociation to ExactOnline Quotations
---------------------------------------------------------------
Every HubSpot Quotequotetemplateassociation will be synchronized with a ExactOnline Quotations.

Once a link between a HubSpot Quotequotetemplateassociation and a ExactOnline Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociation and a ExactOnline Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     - ExactOnline Quotations Property
     - ExactOnline Data Type


HubSpot Quotequotetemplateassociationtype to ExactOnline Currencies
-------------------------------------------------------------------
Every HubSpot Quotequotetemplateassociationtype will be synchronized with a ExactOnline Currencies.

Once a link between a HubSpot Quotequotetemplateassociationtype and a ExactOnline Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociationtype and a ExactOnline Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociationtype Property
     - ExactOnline Currencies Property
     - ExactOnline Data Type
   * - label
     - Description
     - "string"


HubSpot User to ExactOnline Contacts
------------------------------------
Every HubSpot User will be synchronized with a ExactOnline Contacts.

Once a link between a HubSpot User and a ExactOnline Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a ExactOnline Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - ExactOnline Contacts Property
     - ExactOnline Data Type
   * - email
     - BusinessEmail
     - "string"


HubSpot Account to ExactOnline Currencies
-----------------------------------------
Every HubSpot Account will be synchronized with a ExactOnline Currencies.

Once a link between a HubSpot Account and a ExactOnline Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Account and a ExactOnline Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Account Property
     - ExactOnline Currencies Property
     - ExactOnline Data Type
   * - accountType
     - Code
     - "string"


HubSpot Contact to ExactOnline Addresses
----------------------------------------
Every HubSpot Contact will be synchronized with a ExactOnline Addresses.

Once a link between a HubSpot Contact and a ExactOnline Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a ExactOnline Addresses:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - ExactOnline Addresses Property
     - ExactOnline Data Type
   * - properties.address
     - AddressLine1
     - "string"
   * - properties.city
     - City
     - "string"
   * - properties.country
     - Country
     - "string"


HubSpot Deal to ExactOnline Currencies
--------------------------------------
Every HubSpot Deal will be synchronized with a ExactOnline Currencies.

Once a link between a HubSpot Deal and a ExactOnline Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a ExactOnline Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - ExactOnline Currencies Property
     - ExactOnline Data Type
   * - properties.deal_currency_code
     - Code
     - "string"


HubSpot Deal to ExactOnline Salesorders
---------------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a ExactOnline Salesorders.

Once a link between a HubSpot Deal and a ExactOnline Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a ExactOnline Salesorders:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - ExactOnline Salesorders Property
     - ExactOnline Data Type
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


HubSpot Lineitem to ExactOnline Salesorderlines
-----------------------------------------------
Every HubSpot Lineitem will be synchronized with a ExactOnline Salesorderlines.

Once a link between a HubSpot Lineitem and a ExactOnline Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a ExactOnline Salesorderlines:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - ExactOnline Salesorderlines Property
     - ExactOnline Data Type
   * - properties.hs_product_id
     - Item
     - "string"


HubSpot Product to ExactOnline Items
------------------------------------
Every HubSpot Product will be synchronized with a ExactOnline Items.

Once a link between a HubSpot Product and a ExactOnline Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a ExactOnline Items:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - ExactOnline Items Property
     - ExactOnline Data Type


HubSpot Quote to ExactOnline Quotations
---------------------------------------
Every HubSpot Quote will be synchronized with a ExactOnline Quotations.

Once a link between a HubSpot Quote and a ExactOnline Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a ExactOnline Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - ExactOnline Quotations Property
     - ExactOnline Data Type
   * - properties.hs_expiration_date
     - CloseDate
     - "string"

