.. _superoffice_connector:

===========
SuperOffice
===========

`SuperOffice <https://www.superoffice.com/>`_ is a CRM system, combining all customer-facing processes – sales, marketing and customer service – into one technology stack.

The SuperOffice connector configuration can be found in the  `superoffice-connector github repository <https://github.com/sesam-io/superoffice-connector>`_. The `playground branch <https://github.com/sesam-io/superoffice-connector/tree/playground>`_ is typically the most complete branch.

|

Frequently Asked Questions
--------------------------

Why do I sometimes have to re-authorise?
****************************************

SuperOffice uses a token concept called SOTicket, which will expire if it's not used every 6 hours. If Sesam is having operational issues that last more than 6 hours, the token might expire and the user will have to re-authorize to provide us with a new valid token. For more information see `SuperOffice System User <https://docs.superoffice.com/en/authentication/online/auth-application/index.html?tabs=rest>`_.
