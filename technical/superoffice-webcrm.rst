========================
SuperOffice to  Dataflow
========================

Generated: 2024-08-29 08:04:11

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to  Organisations
-------------------------------------
Every SuperOffice Contact will be synchronized with a  Organisations.

Once a link between a SuperOffice Contact and a  Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a  Organisations:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     -  Organisations Property
     -  Data Type
   * - Address.Postal.Address1
     - OrganisationAddress
     - "string"
   * - Address.Postal.Address1
     - OrganisationDeliveryAddress
     - "string"
   * - Address.Postal.City
     - OrganisationCity
     - "string"
   * - Address.Postal.City
     - OrganisationDeliveryCity
     - "string"
   * - Address.Postal.Zipcode
     - OrganisationDeliveryPostCode
     - "string"
   * - Address.Postal.Zipcode
     - OrganisationPostCode
     - "string"
   * - Address.Street.Address1
     - OrganisationAddress
     - "string"
   * - Address.Street.Address1
     - OrganisationDeliveryAddress
     - "string"
   * - Address.Street.City
     - OrganisationCity
     - "string"
   * - Address.Street.City
     - OrganisationDeliveryCity
     - "string"
   * - Address.Street.Zipcode
     - OrganisationDeliveryPostCode
     - "string"
   * - Address.Street.Zipcode
     - OrganisationPostCode
     - "string"
   * - ContactId
     - OrganisationId
     - "string"
   * - Name
     - OrganisationName
     - "string"
   * - Phones.Value
     - OrganisationTelephone
     - "string"


SuperOffice Product to  Products
--------------------------------
Every SuperOffice Product will be synchronized with a  Products.

Once a link between a SuperOffice Product and a  Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a  Products:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     -  Products Property
     -  Data Type


SuperOffice Quoteline to  Quotationline
---------------------------------------
Every SuperOffice Quoteline will be synchronized with a  Quotationline.

Once a link between a SuperOffice Quoteline and a  Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a  Quotationline:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     -  Quotationline Property
     -  Data Type


SuperOffice Sale to  Opportunities
----------------------------------
Every SuperOffice Sale will be synchronized with a  Opportunities.

Once a link between a SuperOffice Sale and a  Opportunities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale and a  Opportunities:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     -  Opportunities Property
     -  Data Type


SuperOffice User to  Users
--------------------------
Every SuperOffice User will be synchronized with a  Users.

Once a link between a SuperOffice User and a  Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a  Users:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     -  Users Property
     -  Data Type

