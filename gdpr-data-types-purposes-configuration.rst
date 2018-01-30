.. _gdpr_data_types_purposes_configuration:

==========================================
GDPR data types and purposes configuration
==========================================

.. contents:: Table of Contents
   :depth: 2
   :local:

Note that this document assumes you are familiar with GDPR concepts and nomenclature.

Configuring the GDPR data types and purposes
============================================

Before the end users/customers can start using your GDPR portal, you must configure the
data types, purposes and consents for your organisation.

You do this by editing a :download:`GDPR Excel setup template file <files/GDPR setup data.xlsx>`. Download this template
to you computer and edit it to reflect your needs. After it has been edited you can upload the result to the GDPR
portal to configure it.

The spreadsheet contains two sheets; "Purpose" and "Data type".

The purpose sheet
-----------------

The purpose sheet contains information about your business activities and the legal grounds of why
you are collecting this information. The data you enter here is used by the "Data types" sheet. The data in this
sheet are information about the GDPR "purpose" and is visible to the user as a navigational "tab" in the data access
portal user interface and, if the purpose is a consent type of purpose, as something the user can potentially opt in or out
of.

The purpose sheet is divided into two sets of columns; "Processing activity" and "Legal grounds".
These sets are further divided into columns:

.. image:: images/purpose_sheet.png
    :width: 800px
    :align: center
    :alt: Purpose sheet

Processing activity
^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30, 70

   * - Column
     - Description

   * - ``ID``
     - The ID of the purpose - it is automatically computed from the other columns. Do not edit it manually.

   * - ``BusinessProcess``
     - A short description of which high level business proccess/group the purpose belongs to,
       for example "Marketing" or "Employment".

   * - ``Name``
     - A short name describing the the purpose at a more detailed level than ``BusinessProces``, for example if the
       ``BusinessProcess`` is "Employment", it can be "Salary" or "Payroll". It is used as a property heading/label in the
       end-user interface.

   * - ``PurposeDescription``
     - A longer description describing the purpose in more detail. It should be long enough that the end user can understand
       the purpose. For example "Handling salary informastion for employees" or "To survey employee satisfaction".

   * - ``ThirdParties``
     - With which third party organisations or entities is information gathered for this purpose shared (leave blank
       if the data is not shared).

Legal grounds
^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30, 70

   * - Column
     - Description

   * - ``LegalType``
     - TODO

   * - ``LegalDetail``
     - TODO

   * - ``DataSource``
     - Where the data stored is gathered from, and/or how it is gathered.

   * - ``LegalDays``
     - The number of days the data stored for this purpose is stored.

   * - ``Criteria``
     - TODO


The data type sheet
-------------------

The data type sheet contains all the types of data your organisation stores about GDPR subjects.
It is linked to one or more of the purposes you have defined in the purposes sheet.

.. image:: images/data_type_sheet.png
    :width: 800px
    :align: center
    :alt: Data type sheet

The sheet is divided into two parts; the leftmost columns are properties for the data type, the rightmost part
is a matrix where you enter a "x" value for each purpose the data type is governed by. These latter columns are automatically
generated from the purposes you set up in the "purposes" sheet.

The data type properties
^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30, 70

   * - Column
     - Description

   * - ``ID``
     - The ID of the data type - it is automatically computed from the other columns. Do not edit it manually.

   * - ``Type``
     - A short description what type of data this is (for example "Customer" or "Employee")

   * - ``System``
     - A short name of the system where the data is residing (for example "CRM" or "ActiveDirectory").

   * - ``Description``
     - A longer description of the type of data to make it easier for the data subject to understand what the data is

   * - ``Level``
     - The "level" of the data - it can be either "Personal" or "Related", i.e. directly about the data subject or
       indirectly (for example data about the customer such as address or orders for the customer, respectively)

   * - ``Identifiers``
     - TODO

   * - ``Exclude``
     - TODO

   * - ``Contact``
     - An comma separated list of email-addresses for who should get notified when a GDPR data access request or change
       request is received by the GDPR portal.

   * - ``Purposes``
     - All columns to the right hand side is automatically generated from the "purposes" sheet. It creates a matrix
       where putting in an "x" value for a specific purpose for a specific data type indicates that this data type
       is covered by that specific purpose.


Updating GDPR data types and purposes
=====================================

When the spreadsheet is filled out, you can upload it to the GDPR portal by navigating to the "GDPR" section on
the right hand side of the management studio GUI. Here you can upload the setup excel file in the tab called "Data Types".

After uploading the file, the portal data structures will be updated with this information and the data access portal
user interface will reflect the purposes and data types defined in the spreadsheet (note that this process can take a
few minutes after upload).

In the management studio of the portal you can inspect the current configuration by navigating to the ``global-data-type``
and ``global-purpose`` datasets.
