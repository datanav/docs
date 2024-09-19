:badge:`Free feature,badge-success badge-pill`

.. _integrated_search:

Integrated Search
=================

Integrated data browsing gives you more insight into your data and the relationships within. Once enabled, globals are
indexed and available for free text search and navigation. Note that this incurs a 2x increase in data size needed for
global pipes.

Integrated Search is now available for all subscriptions with clustered architecture. This is how you can activate the new feature:

.. note::

	You need to be the payment method owner in order to enable this feature.

- Login to portal.sesam.io

- Select the subscription you want to use

- Navigate to Subscription on the left menu

- Click on Products tab

- Click on “Enable Integrated Search”

If your subscription is not yet on clustered architecture please contact support to start the migration.

.. admonition:: Read data permissions

   Integrated search results are limited to the data that users have permission to read.

.. _integrated_search_query_syntax:

Query syntax
------------

The text search field in Integrated Search supports the following syntax. The default operator is ``OR``. Search results are ranked by relevance.

- ``+``: AND operation. Example: ``John + Doe`` means find results that matches both terms.
- ``|``: OR operation. Example: ``John | Doe`` means find results that matches at least one term.
- ``-``: negation. Example: ``John -Doe`` means find results that matches only the first term, but not the second term.
- ``"``: phrase search. Example: ``"John Doe"`` means find results that matches the first term directly followed by the second term.
- ``~N``: used after phrase to specifiy slop amount. Example: ``"John Doe"~2`` means find results that matches the first term directly followed by the second term with up to two terms in between.
- ``*``: prefix search. Example: ``"Joh*"`` means find results that matches the first term prefix.
- ``~N``: edit distance / fuzziness. Example: ``John~2`` means find results that matches the term but with up to two character edits.
- ``(`` and ``)``: precedence. Example: ``(John + Doe) | (Jane Doe)`` means find results that matches the first criteria or the second criteria.
