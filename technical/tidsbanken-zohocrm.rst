==============================
Tidsbanken to ZohoCRM Dataflow
==============================

Generated: 2024-07-06 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Avdeling to ZohoCRM Account
--------------------------------------
Every Tidsbanken Avdeling will be synchronized with a ZohoCRM Account.

Once a link between a Tidsbanken Avdeling and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - Navn
     - Account_Name
     - "string"


Tidsbanken Kunde to ZohoCRM Account
-----------------------------------
Every Tidsbanken Kunde will be synchronized with a ZohoCRM Account.

Once a link between a Tidsbanken Kunde and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - LevPostNr
     - Billing_Code
     - "string"
   * - LevPostNr
     - Shipping_Code
     - "string"
   * - LevPoststed
     - Billing_City
     - "string"
   * - LevPoststed
     - Shipping_City
     - "string"
   * - Navn
     - Account_Name
     - "string"
   * - Postnr
     - Billing_Code
     - "string"
   * - Postnr
     - Shipping_Code
     - "string"
   * - Poststed
     - Billing_City
     - "string"
   * - Poststed
     - Shipping_City
     - "string"
   * - Telefon
     - Phone
     - "string"
   * - Url
     - Website
     - "string"

