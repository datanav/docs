===========================================
Business Central to PowerOffice GO Dataflow
===========================================

Generated: 2024-09-17 07:26:52

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Central Customers to PowerOffice GO Contactperson
----------------------------------------------------------
Before any synchronization can take place, a link between a Business Central Customers and a PowerOffice GO Contactperson must be established.

A new PowerOffice GO Contactperson will be created from a Business Central Customers if it is connected to a Business Central Businesscentral-salesorders that is synchronized into PowerOffice GO.

Once a link between a Business Central Customers and a PowerOffice GO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers and a PowerOffice GO Contactperson:

.. list-table::
   :header-rows: 1

   * - Business Central Customers Property
     - PowerOffice GO Contactperson Property
     - PowerOffice GO Data Type


Business Central Customers to PowerOffice GO Customers
------------------------------------------------------
Before any synchronization can take place, a link between a Business Central Customers and a PowerOffice GO Customers must be established.

A new PowerOffice GO Customers will be created from a Business Central Customers if it is connected to a Business Central Businesscentral-customers, Businesscentral-salesorders, Businesscentral-contact-person, or Businesscentral-contacts-person that is synchronized into PowerOffice GO.

Once a link between a Business Central Customers and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - Business Central Customers Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type


Business Central Customers to PowerOffice GO Customers person
-------------------------------------------------------------
Before any synchronization can take place, a link between a Business Central Customers and a PowerOffice GO Customers person must be established.

A new PowerOffice GO Customers person will be created from a Business Central Customers if it is connected to a Business Central Businesscentral-customers, Businesscentral-salesorders, Businesscentral-contact-person, or Businesscentral-contacts-person that is synchronized into PowerOffice GO.

Once a link between a Business Central Customers and a PowerOffice GO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers and a PowerOffice GO Customers person:

.. list-table::
   :header-rows: 1

   * - Business Central Customers Property
     - PowerOffice GO Customers person Property
     - PowerOffice GO Data Type


Business Central Items to PowerOffice GO Product
------------------------------------------------
Before any synchronization can take place, a link between a Business Central Items and a PowerOffice GO Product must be established.

A new PowerOffice GO Product will be created from a Business Central Items if it is connected to a Business Central Businesscentral-salesorderlines that is synchronized into PowerOffice GO.

Once a link between a Business Central Items and a PowerOffice GO Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Items and a PowerOffice GO Product:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     - PowerOffice GO Product Property
     - PowerOffice GO Data Type


Business Central Salesorders to PowerOffice GO Salesorders
----------------------------------------------------------
Before any synchronization can take place, a link between a Business Central Salesorders and a PowerOffice GO Salesorders must be established.

A new PowerOffice GO Salesorders will be created from a Business Central Salesorders if it is connected to a Business Central Businesscentral-salesorderlines that is synchronized into PowerOffice GO.

Once a link between a Business Central Salesorders and a PowerOffice GO Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorders and a PowerOffice GO Salesorders:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
     - PowerOffice GO Salesorders Property
     - PowerOffice GO Data Type


Business Central Contacts person to PowerOffice GO Contactperson
----------------------------------------------------------------
Every Business Central Contacts person will be synchronized with a PowerOffice GO Contactperson.

Once a link between a Business Central Contacts person and a PowerOffice GO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contacts person and a PowerOffice GO Contactperson:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts person Property
     - PowerOffice GO Contactperson Property
     - PowerOffice GO Data Type


Business Central Contacts person to PowerOffice GO Customers
------------------------------------------------------------
Every Business Central Contacts person will be synchronized with a PowerOffice GO Customers.

Once a link between a Business Central Contacts person and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contacts person and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts person Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type


Business Central Contacts person to PowerOffice GO Customers person
-------------------------------------------------------------------
Every Business Central Contacts person will be synchronized with a PowerOffice GO Customers person.

Once a link between a Business Central Contacts person and a PowerOffice GO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contacts person and a PowerOffice GO Customers person:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts person Property
     - PowerOffice GO Customers person Property
     - PowerOffice GO Data Type


Business Central Customers company to PowerOffice GO Customers
--------------------------------------------------------------
Every Business Central Customers company will be synchronized with a PowerOffice GO Customers.

Once a link between a Business Central Customers company and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers company and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - Business Central Customers company Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type
   * - addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - city
     - MailAddress.City
     - "string"
   * - country
     - MailAddress.CountryCode
     - "string"
   * - displayName
     - Name
     - "string"
   * - id
     - Id
     - "integer"
   * - phoneNumber
     - PhoneNumber
     - "string"
   * - postalCode
     - MailAddress.ZipCode
     - "string"
   * - type
     - IsPerson
     - "boolean"
   * - website
     - WebsiteUrl
     - "string"


Business Central Customers company to PowerOffice GO Customers person
---------------------------------------------------------------------
Every Business Central Customers company will be synchronized with a PowerOffice GO Customers person.

Once a link between a Business Central Customers company and a PowerOffice GO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers company and a PowerOffice GO Customers person:

.. list-table::
   :header-rows: 1

   * - Business Central Customers company Property
     - PowerOffice GO Customers person Property
     - PowerOffice GO Data Type


Business Central Customers person to PowerOffice GO Customers
-------------------------------------------------------------
Every Business Central Customers person will be synchronized with a PowerOffice GO Customers.

Once a link between a Business Central Customers person and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers person and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - Business Central Customers person Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type


Business Central Customers person to PowerOffice GO Customers
-------------------------------------------------------------
Every Business Central Customers person will be synchronized with a PowerOffice GO Customers.

Once a link between a Business Central Customers person and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers person and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - Business Central Customers person Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type


Business Central Customers person to PowerOffice GO Customers person
--------------------------------------------------------------------
Every Business Central Customers person will be synchronized with a PowerOffice GO Customers person.

Once a link between a Business Central Customers person and a PowerOffice GO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers person and a PowerOffice GO Customers person:

.. list-table::
   :header-rows: 1

   * - Business Central Customers person Property
     - PowerOffice GO Customers person Property
     - PowerOffice GO Data Type


Business Central Customers person to PowerOffice GO Customers person
--------------------------------------------------------------------
Every Business Central Customers person will be synchronized with a PowerOffice GO Customers person.

Once a link between a Business Central Customers person and a PowerOffice GO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers person and a PowerOffice GO Customers person:

.. list-table::
   :header-rows: 1

   * - Business Central Customers person Property
     - PowerOffice GO Customers person Property
     - PowerOffice GO Data Type


Business Central Employees to PowerOffice GO Employees
------------------------------------------------------
Every Business Central Employees will be synchronized with a PowerOffice GO Employees.

Once a link between a Business Central Employees and a PowerOffice GO Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Employees and a PowerOffice GO Employees:

.. list-table::
   :header-rows: 1

   * - Business Central Employees Property
     - PowerOffice GO Employees Property
     - PowerOffice GO Data Type


Business Central Items to PowerOffice GO Product
------------------------------------------------
Every Business Central Items will be synchronized with a PowerOffice GO Product.

Once a link between a Business Central Items and a PowerOffice GO Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Items and a PowerOffice GO Product:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     - PowerOffice GO Product Property
     - PowerOffice GO Data Type


Business Central Salesorderlines to PowerOffice GO Salesorderlines
------------------------------------------------------------------
Every Business Central Salesorderlines will be synchronized with a PowerOffice GO Salesorderlines.

Once a link between a Business Central Salesorderlines and a PowerOffice GO Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorderlines and a PowerOffice GO Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorderlines Property
     - PowerOffice GO Salesorderlines Property
     - PowerOffice GO Data Type


Business Central Salesorders to PowerOffice GO Salesorders
----------------------------------------------------------
Every Business Central Salesorders will be synchronized with a PowerOffice GO Salesorders.

Once a link between a Business Central Salesorders and a PowerOffice GO Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorders and a PowerOffice GO Salesorders:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
     - PowerOffice GO Salesorders Property
     - PowerOffice GO Data Type

