.. _wave_connector:

====
Wave
====

`Wave <https://waveapps.com>`_ provides financial software and services for small businesses, with services include direct bank data imports, invoicing and expense tracking, customizable chart of accounts, and journal transactions.

The Wave connector configuration can be found in the  `wave-connector github repository <https://github.com/sesam-io/wave-connector>`_. The `playground branch <https://github.com/sesam-io/wave-connector/tree/playground>`_ is typically the most complete branch.

Frequently Asked Questions
--------------------------

Why is my list of products growing without me adding new products?
******************************************************************

This can happen if you have another integration running in parallel with Sesam. For example if you are using HubSpot Data Sync (HSDS) alongside Sesam to exchange data between Wave and HubSpot – both Sesam and HSDS will detect products that the other service creates, and interpret this as a new product that needs to be inserted in the other system. The use of other integration tools that are overlapping the functionality of Sesam is not recommended for these reasons.
 
Please see `Co-existing <https://docs.sesam.io/talk/co-existence/index.html>`_ with other integration services.


Why is the order of my order lines different than in the other systems?
***********************************************************************
The order that the order lines appear in Wave is based on when they were created or updated. The most recent updated order line will appear as the last one in your Wave invoice draft. When creating a completely new order in a another system, all order lines will be given the same timestamp. This makes it impossible to determine in what sequence the order lines originally were created, resulting in a arbitrary succession of your order lines in Wave.
