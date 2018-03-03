.. _gdpr_platform_configuration:

===========================
GDPR platform configuration
===========================

.. contents:: Table of Contents
   :depth: 2
   :local:

Overview
========

The GDPR platform consist of three parts; the GDPR platform management interface (management studio), the GDPR platform
datahub and the GDPR data access portal.

The management studio interface enables you to edit configuration settings of your GDPR platform and access its
datahub where all your GDPR data is collected, connected and stored.

The GDPR data access portal is the public facing interface of the GDPR platform - this is where the end user - data
subject in GDPR lingo - can log in and manage their GDPR requests, data and consents.

Logging into the GDPR platform
==============================

You can access the GDPR platform management studio by logging into the `Sesam portal <https://portal.sesam.io>`_   and clicking
on your GDPR platform subscription.

This will open the management studio GUI for your GDPR platform and datahub. Before you can start using your GDPR platform,
there are a couple of configuration elements that you might want to set up first.

Configuring the GDPR platform
=============================

There are some configuration properties that you might want to edit before starting to use the platform:

* :ref:`Domain name <gdpr_access_portal_domain_name>`
* :ref:`Data type template <gdpr_platform_data_type_template>`
* :ref:`Setup file URL and update interval <gdpr_platform_data_type_template_setup_url>`
* :ref:`GDPR Data Access portal logo <gdpr_data_access_portal_logo>`
* :ref:`Default language settings <gdpr_data_access_portal_default_language>`
* :ref:`Default phone prefix (for SMS notifications) <gdpr_data_access_portal_default_phone_prefix>`

To do this, navigate to the GDPR platform setup screen:

.. image:: images/gdpr_platform_setup_screen.png
    :width: 800px
    :align: center
    :alt: Sesam GDPR platform setup screen

This screen should contain a number of configuration properties

.. _gdpr_access_portal_domain_name:

Domain name
-----------

The domain name is the internet address (DNS name) where your GDPR data access portal should be available to the users (data
subjects in GDPR lingo). You can choose any name you want, as long as it's not already in use by someone else.
Your GDPR data access portal will be avaible on the web as https://selected-domain-name.sesamdata.com

.. _gdpr_platform_data_type_template:

Data type template
------------------

This section allows you to upload a "Data type template" file (an Excel spreadsheet) to the GDPR platform.
See the :ref:`GDPR data types and purposes configuration <gdpr_data_types_purposes_configuration>` section for more
details.

.. _gdpr_platform_data_type_template_setup_url:

Setup file URL
--------------

If you have this "Data type template" configuration data file somewhere where it can be reached using an URL
(for example as a shared file in Dropbox, Google Drive, One Drive or something similar), you can configure the GDPR
platform to update the settings from this file at regular intervals. By default this is at midnight UTC.

Setup file Cron expression
--------------------------

You configure how often the "Setup file URL" should be downloaded and updated by editing a "Cron" expression.
In this example, it will be downloaded every day at midnight and automatically update the GDPR platform setup:

::

  0 0 * * *

In this case it will be updated every hour:

::

  0 * * * *

In this case it will be updated every fifteen minutes:

::

  0/15 * * * *

By default, if a setup file has been specified it will be updated at midnight UTC.

If you are unfamiliar with `cron expressions <https://en.wikipedia.org/wiki/Cron>`_, you can read more of how
they are formatted in the :doc:`Cron Expressions <cron-expressions>` document.

.. _gdpr_data_access_portal_logo:

GDPR data access portal logo
----------------------------

You can choose a custom logo image to display on your GDPR data access portal in the "Upload new logo image" setup
section. The uploaded file will replace the default (or current) GDPR data access portal logo immediately when saved.

.. _gdpr_data_access_portal_default_language:

Default language settings
-------------------------

The GDPR platform is configured with english and norwegian message text by default. You can choose which default
language is used by setting it to either a full ISO country code (i.e. "country-dialect") or just
the country code - for example:

::

  no-NB

or

::

  en


If your language is different than the default norwegian and english locale, you can add additional
translations by editing the ``custom-translations`` pipe configuration in the GDPR platform datahub. See the later chapter on custom message texts
for more details. These texts are keyed on ISO locale codes and correspond to this setting. If you for example have
added german texts using the code "de-DE" (or just "de"), you can specify this as the default language here.

.. _gdpr_data_access_portal_default_phone_prefix:

The default phone prefix
------------------------

The default phone prefix should be matched to your country, for example if your organisation resides
in Norway, it would look like:

::

    +47


