=========================================
Powerofficego to PowerOfficeGov1 Dataflow
=========================================

Generated: 2023-08-17 08:32:31

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to PowerOfficeGov1. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customer to PowerOfficeGov1 Customer
--------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customer and a PowerOfficeGov1 Customer must be established.

A new PowerOfficeGov1 Customer will be created from a Powerofficego Customer if it is connected to a Powerofficego Customer, Supplier, Customers, or Contactperson that is synchronized into PowerOfficeGov1.

A Powerofficego Customer will merge with a PowerOfficeGov1 Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - PowerOfficeGov1 Customer Property
   * - id
     - id

Once a link between a Powerofficego Customer and a PowerOfficeGov1 Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a PowerOfficeGov1 Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - PowerOfficeGov1 Customer Property
     - PowerOfficeGov1 Data Type


Powerofficego Suppliers to PowerOfficeGov1 Address
--------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Suppliers and a PowerOfficeGov1 Address must be established.

A Powerofficego Suppliers will merge with a PowerOfficeGov1 Address if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers Property
     - PowerOfficeGov1 Address Property
   * - MailAddress.Id
     - id

Once a link between a Powerofficego Suppliers and a PowerOfficeGov1 Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers and a PowerOfficeGov1 Address:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers Property
     - PowerOfficeGov1 Address Property
     - PowerOfficeGov1 Data Type


Powerofficego Suppliers to PowerOfficeGov1 Location
---------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Suppliers and a PowerOfficeGov1 Location must be established.

A Powerofficego Suppliers will merge with a PowerOfficeGov1 Location if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers Property
     - PowerOfficeGov1 Location Property
   * - MailAddress.Id
     - id

Once a link between a Powerofficego Suppliers and a PowerOfficeGov1 Location is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers and a PowerOfficeGov1 Location:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers Property
     - PowerOfficeGov1 Location Property
     - PowerOfficeGov1 Data Type


Powerofficego Customer to PowerOfficeGov1 Department
----------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customer and a PowerOfficeGov1 Department must be established.

A new PowerOfficeGov1 Department will be created from a Powerofficego Customer if it is connected to a Powerofficego Employee that is synchronized into PowerOfficeGov1.

Once a link between a Powerofficego Customer and a PowerOfficeGov1 Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a PowerOfficeGov1 Department:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - PowerOfficeGov1 Department Property
     - PowerOfficeGov1 Data Type


Powerofficego Supplier to PowerOfficeGov1 Contact
-------------------------------------------------
Every Powerofficego Supplier will be synchronized with a PowerOfficeGov1 Contact.

Once a link between a Powerofficego Supplier and a PowerOfficeGov1 Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Supplier and a PowerOfficeGov1 Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Supplier Property
     - PowerOfficeGov1 Contact Property
     - PowerOfficeGov1 Data Type
   * - EmailAddress
     - Emails.Value
     - "string"
   * - InternationalIdNumber (Dependant on having superoffice-contactid in poweroffice-customer:InternationalIdType)
     - ContactId
     - "string"
   * - LegalName
     - Name
     - "string"
   * - PhoneNumber
     - Phones.Value
     - "string"
   * - WebsiteUrl
     - Domains
     - "list"
   * - WebsiteUrl
     - Urls.Value
     - "string"

