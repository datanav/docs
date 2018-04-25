.. _gdpr_data_types_purposes_configuration:

=======================
GDPR data access portal
=======================

.. contents:: Table of Contents
   :depth: 2
   :local:

Logging into the GDPR data access portal
========================================

By default, the end user (subject) can log into the GDPR data access portal by accessing its public URL.
For example, if your public URL is https://datahub-subscription_id.domain.com the data access portal URL should be
https://gdpr-dap-subscription_id.domain.com

You can find the public URL of your GDPR platform by navigating to the "GDPR data access portal" section on the left hand
side of the management studion and clicking on the "Network" tab. Under the heading "Data Access Portal backend"
you can find the public URL of the GDPR data access portal. It will look something like this:

::

   https://gdpr-dap-subscription_id.sesam.cloud


When accessing this page the user must first identify themselves by logging on using a predefined credential such
as email or mobile phone number. After doing this, the user will be sent a one-time passcode to be used to log in.
This pass code will expire when the user ends their session or after a certain idle time. If the session expires
the user has to log on again.

After having logged in the first time, the user can either send a request for their data or they can request that their data
be deleted.

Making a data access request
============================

A end user requesting data results in a GDPR access request being sent to the GDPR platform. This will trigger an email being
sent to all unique contacts entered into the Data types and purposes setup Excel spreadsheet mentioned in the
:doc:`previous section <gdpr-data-types-purposes-configuration>`.

The email contains a link to an Excel file that the recipient of the mail can download and fill out.
Once filled out, it can then be uploaded through the GDPR platform and the contained data will be made available to the
subject through the GDPR data access portal interface.

.. _gdpr_data_access_request_template:

The data access request excel template
======================================

Each responsible person receiving the email about a data access request must be a member of the GDPR platform so they
can log in to download the Excel template they need to fill out with the subject's data.

The first sheet of the spreadsheet is called "DataSubject" and contains information about the subject of the data
access request, such as "DataSubjectId" which should be a field containing a value that reflects the logged in user
(for example email, phone number, customer number or similar). It also contains a timestamp for when the request
was made (in the UTC time zone), in case multiple requests have been made one can choose the fill out the newest
template.

Note that none of the fields in the first "DataSubject" field should be changed manually - they are needed as-is when uploading
the completed spreadsheet.

The rest of the sheets in the spreadsheet is enumerated by data type, one per system in the "Data type" sheet of the
configuration setup spreadsheet, see :ref:`the previous section <gdpr-data-types-purposes-configuration>` for details.

These are the sheets that must be filled out by the receiver of the template and uploaded when finished.

The data is assumed to be tabular and in a form where each row has a unique id. Thus each sheet contains a single,
obligatory column ``id``. The other columns must be defined by the person filling out the data and will typically
be columns from a SQL database or some other tabular datasource.

After setting up the columns, the person must then extract the relevant data for the data subject somehow from the
system(s) in a form suitable for entering into Excel and insert one row in the Excel sheet per tabular data row in
the source data (the values must be in the correct sequence so the column names match the source data).

After all the sheets per data type has been extracted and filled in the spreadsheet, the resulting file can then
be uploaded to the GDPR platform by navigating to the "GDPR" section on the left hand side and using the
"Upload data request template" form under the "Access request" tab.

The result of this action is two-fold:

* The data is encrypted using the data subjects public key, stored in the GDPR platform datahub and then sent to the GDPR data access portal (where
  it can only be decrypted by the data subject's private key, which is only stored on the subject's computer).
* A notification email is sent to the subject that the requested data is available, if the subject has a registered email address.

Note that there is an half-an-hour delay between uploading data and the notification email being sent. This is to ensure
that the GDPR data access portal has been fully updated with the uploaded data before notifying the subject.

If there is more than one spreadsheet to be filled out (for example if there are multiple data types with multiple different
contact persons), one notification email is sent each time a new filled-out spreadsheet is uploaded.

Making a data deletion request
==============================

TODO


Making a data change request
============================

The GDPR data access portal can be configured so the subject is able to request specific changes to their data, for example
a wrong address, correct spelling and so on. See the :doc:`Databrowser guide <databrowser-guide>` for how to configure
which properties can be editable by the logged-in subject.

Any such changes to the data by the subject result in a notification email sent to the contact registered for
the particular data type where this data originated.

The notification email contains a link to a page in the GDPR platform where the person responsible for the data type
can download a list of requested changes. This list contains information such as subject id, data id(s), old data value,
requested (new) value for the data, a timestamp for when the request was made and so on.

If the request is accepted and the data is changed as per the request, the spreadsheet from where the changed data came
from must be re-filled out and re-uploaded to reflect the change, see the
:ref:`data access request excel template <gdpr_data_access_request_template>` section for details on this process.

Making a consent change request
===============================

TODO
