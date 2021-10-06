
.. _sesam-in-the-wild-beginner-6-1:

Sesam in the Wild: Beginner
---------------------------

.. _case_intro:

The situation
~~~~~~~~~~~~~


brainstormV1
^^^^^^^^^^^^

We have a situation where a company which sells stuff online handle their
orders and shipping manually.
Currently we look at the current orders in our order system daily and manually
place them into both our accounting and shipping system.

The order system has an API making the data in it available.
The accounting system's backend is a SQL database.
The shipping system is provided by the shipping company also has an API making
machine interactions possible.

With Sesam we will automate the transfer of information between these systems.

Later on we will add a customer management system which makes users able to login
and see their current orders etc.
We will also add a analytics system.

We can connect the shipping, customer management and analytics data because they
all store entities representing the customer.
The analytics system knows what type of products customers most often buy and
uses ML to generate customized offers for each of our customers.
The Customer Management system lets users change their information such as
login information, email, billing address, shipping address, store wishlists, etc.

We can f.ex send the billing address info to a payment system we can introduce.
We can also prioritize the shipping address from the customer management system
to the shipping system.

.. seealso::

  TODO

.. _tasks-for-sesam-in-the-wild-beginner-6-1:

Tasks for Sesam in the Wild: Beginner
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
