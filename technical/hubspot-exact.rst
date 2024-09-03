=========================
HubSpot to Exact Dataflow
=========================

Generated: 2024-09-03 08:16:35

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Exact. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to  Accounts
----------------------------
Every HubSpot Company will be synchronized with a  Accounts.

Once a link between a HubSpot Company and a  Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a  Accounts:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     -  Accounts Property
     -  Data Type
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


HubSpot Contact to  Contacts
----------------------------
Every HubSpot Contact will be synchronized with a  Contacts.

Once a link between a HubSpot Contact and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a  Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     -  Contacts Property
     -  Data Type
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


HubSpot Contactcompanyassociation to  Contacts
----------------------------------------------
Every HubSpot Contactcompanyassociation will be synchronized with a  Contacts.

Once a link between a HubSpot Contactcompanyassociation and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociation and a  Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     -  Contacts Property
     -  Data Type


HubSpot Contactcompanyassociationtype to  Currencies
----------------------------------------------------
Every HubSpot Contactcompanyassociationtype will be synchronized with a  Currencies.

Once a link between a HubSpot Contactcompanyassociationtype and a  Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociationtype and a  Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociationtype Property
     -  Currencies Property
     -  Data Type
   * - label
     - Description
     - "string"


HubSpot Deal to  Quotations
---------------------------
Every HubSpot Deal will be synchronized with a  Quotations.

Once a link between a HubSpot Deal and a  Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a  Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     -  Quotations Property
     -  Data Type
   * - properties.closedate
     - DeliveryDate
     - "string"
   * - properties.deal_currency_code
     - Currency
     - "string"
   * - properties.description
     - Description
     - "string"


HubSpot Dealcompanyassociation to  Quotations
---------------------------------------------
Every HubSpot Dealcompanyassociation will be synchronized with a  Quotations.

Once a link between a HubSpot Dealcompanyassociation and a  Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociation and a  Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     -  Quotations Property
     -  Data Type


HubSpot Dealcompanyassociationtype to  Currencies
-------------------------------------------------
Every HubSpot Dealcompanyassociationtype will be synchronized with a  Currencies.

Once a link between a HubSpot Dealcompanyassociationtype and a  Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociationtype and a  Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociationtype Property
     -  Currencies Property
     -  Data Type
   * - label
     - Description
     - "string"


HubSpot Dealcontactassociation to  Quotations
---------------------------------------------
Every HubSpot Dealcontactassociation will be synchronized with a  Quotations.

Once a link between a HubSpot Dealcontactassociation and a  Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociation and a  Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     -  Quotations Property
     -  Data Type


HubSpot Dealcontactassociationtype to  Currencies
-------------------------------------------------
Every HubSpot Dealcontactassociationtype will be synchronized with a  Currencies.

Once a link between a HubSpot Dealcontactassociationtype and a  Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociationtype and a  Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociationtype Property
     -  Currencies Property
     -  Data Type
   * - label
     - Description
     - "string"


HubSpot Lineitem to  Quotations
-------------------------------
Every HubSpot Lineitem will be synchronized with a  Quotations.

Once a link between a HubSpot Lineitem and a  Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a  Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     -  Quotations Property
     -  Data Type


HubSpot Lineitemdealassociation to  Quotations
----------------------------------------------
Every HubSpot Lineitemdealassociation will be synchronized with a  Quotations.

Once a link between a HubSpot Lineitemdealassociation and a  Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a  Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     -  Quotations Property
     -  Data Type


HubSpot Lineitemdealassociationtype to  Currencies
--------------------------------------------------
Every HubSpot Lineitemdealassociationtype will be synchronized with a  Currencies.

Once a link between a HubSpot Lineitemdealassociationtype and a  Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociationtype and a  Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociationtype Property
     -  Currencies Property
     -  Data Type
   * - label
     - Description
     - "string"


HubSpot Lineitemquoteassociation to  Quotations
-----------------------------------------------
Every HubSpot Lineitemquoteassociation will be synchronized with a  Quotations.

Once a link between a HubSpot Lineitemquoteassociation and a  Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociation and a  Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociation Property
     -  Quotations Property
     -  Data Type


HubSpot Lineitemquoteassociationtype to  Currencies
---------------------------------------------------
Every HubSpot Lineitemquoteassociationtype will be synchronized with a  Currencies.

Once a link between a HubSpot Lineitemquoteassociationtype and a  Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociationtype and a  Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociationtype Property
     -  Currencies Property
     -  Data Type
   * - label
     - Description
     - "string"


HubSpot Quotecompanyassociation to  Quotations
----------------------------------------------
Every HubSpot Quotecompanyassociation will be synchronized with a  Quotations.

Once a link between a HubSpot Quotecompanyassociation and a  Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociation and a  Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     -  Quotations Property
     -  Data Type


HubSpot Quotecompanyassociationtype to  Currencies
--------------------------------------------------
Every HubSpot Quotecompanyassociationtype will be synchronized with a  Currencies.

Once a link between a HubSpot Quotecompanyassociationtype and a  Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociationtype and a  Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociationtype Property
     -  Currencies Property
     -  Data Type
   * - label
     - Description
     - "string"


HubSpot Quotecontactassociation to  Quotations
----------------------------------------------
Every HubSpot Quotecontactassociation will be synchronized with a  Quotations.

Once a link between a HubSpot Quotecontactassociation and a  Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociation and a  Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     -  Quotations Property
     -  Data Type


HubSpot Quotecontactassociationtype to  Currencies
--------------------------------------------------
Every HubSpot Quotecontactassociationtype will be synchronized with a  Currencies.

Once a link between a HubSpot Quotecontactassociationtype and a  Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociationtype and a  Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociationtype Property
     -  Currencies Property
     -  Data Type
   * - label
     - Description
     - "string"


HubSpot Quotedealassociation to  Quotations
-------------------------------------------
Every HubSpot Quotedealassociation will be synchronized with a  Quotations.

Once a link between a HubSpot Quotedealassociation and a  Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociation and a  Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     -  Quotations Property
     -  Data Type


HubSpot Quotedealassociationtype to  Currencies
-----------------------------------------------
Every HubSpot Quotedealassociationtype will be synchronized with a  Currencies.

Once a link between a HubSpot Quotedealassociationtype and a  Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociationtype and a  Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociationtype Property
     -  Currencies Property
     -  Data Type
   * - label
     - Description
     - "string"


HubSpot Quotequotetemplateassociation to  Quotations
----------------------------------------------------
Every HubSpot Quotequotetemplateassociation will be synchronized with a  Quotations.

Once a link between a HubSpot Quotequotetemplateassociation and a  Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociation and a  Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     -  Quotations Property
     -  Data Type


HubSpot Quotequotetemplateassociationtype to  Currencies
--------------------------------------------------------
Every HubSpot Quotequotetemplateassociationtype will be synchronized with a  Currencies.

Once a link between a HubSpot Quotequotetemplateassociationtype and a  Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociationtype and a  Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociationtype Property
     -  Currencies Property
     -  Data Type
   * - label
     - Description
     - "string"


HubSpot User to  Contacts
-------------------------
Every HubSpot User will be synchronized with a  Contacts.

Once a link between a HubSpot User and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a  Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     -  Contacts Property
     -  Data Type
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

