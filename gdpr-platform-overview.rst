.. _gdpr_platform_overview:

===========================
GDPR platform overview
===========================

With Sesam's GDPR Platform you can handle many of your company's GDPR `responsibilities <https://www.datatilsynet.no/rettigheter-og-plikter/virksomhetenes-plikter/>`_.
For more details read about `Sesam and privacy <https://sesam.io/privacy/howitworks/technical-features.html>`_ and
`Data Subject rights that the Sesam platform delivers on <https://sesam.io/privacy/howitworks/technical-features.html>`_
Here you will also find information about pricing. 

You can contact `info(at)sesam.io <mailto:info@sesam.io>`_ if 
you want to talk about what Sesam GDPR Platform can do for your organization. Use https://support.sesam.io/ for 
support questions. 

Sesam is also `integrated by partners <https://sesam.io/privacy/partners/>`_ to streamline privacy management.

Most of the Sesam's GDPR Platform is regular Sesam node with some preconfigured Systems, Variables and Pipes. 

You can manage the GDPR Platform as a regular Sesam node in the `Management Studio <https://portal.sesam.io>`_.
In the left menu, you will have two elements that you don't have in a regular Sesam node.

- GDPR
- GDPR data access portal

.. image:: images/gdpr-getting-started/setup.png
    :width: 800px
    :align: center
    :alt: GDPR setup page

The GDPR platform comes in two main ``flavorers``. 
A manually updated workflow and automatic handling of data access requests.

The ``GDPR`` menu element enables you to edit configuration settings of your GDPR platform.
It is also the place to handle requests from data subjects if you have a manually updated workflow.

The GDPR data access portal is the public facing interface of the GDPR platform - this is where the end user - data
subject in GDPR lingo - can log in and manage their GDPR requests, data and consents.
With the ``GDPR data access portal`` menu element you manage this access portal.

To use automatic handling, all the data we want to make available for the GDPR platform must be pulled into the 
GDPR platform (Sesam node). Once the data is available in the node, the system can serve data access requests on
it's own. You can use the GDPR platform as a regular Sesam node with the benefit of automatic handling of data
access requests. You can use this to e.g. make sure that you only analyze/process data if you have proper lawful
basis (e.g. consent, contract, legal obligation ...) for processing. 

**Be aware** that uploading a config like described in the general Sesam getting started guide replaces the 
existing config. This **can destroy the preconfigured GDPR pipes and systems**. It is safest to use copy and paste
in pipe config editor.