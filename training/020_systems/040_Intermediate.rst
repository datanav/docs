
.. _systems-intermediate-2-3:

Intermediate
------------

.. _microservice-system-2-3:

Microservice System
~~~~~~~~~~~~~~~~~~~


How does Sesam look at microservices?

What is a microservice?

How do I use one?

Don’t go too deep, we have a whole module for these.

Probably want to wait with this subchapter until we’ve written the
microservices module.

.. seealso::

  TODO

.. _http-transforms-2-3:

HTTP Transforms
~~~~~~~~~~~~~~~

When you need to transform or append information which Sesam isn’t good
at handling, you’d use an http_transform.

When you don’t want all the data from a system, but need to append it to
the data you’re processing, you’d typically do a http_transform.

Example: You want to get the current weather for a location, but you
don’t want to read all the weather around the world constantly into
sesam. What you’re interested in is the weather for a location specified
by an entity at runtime. You can get this by querying an API per entity
being processed.vor

Example: You need to convert UTM to LatLong coordinates. Sesam doesn’t
have a function to do this built in, so you make a microservice to do
the conversion and call this with an http_transform.

General Example: appending time-dependent datapoints to your output
without reading absolutely all of the time-dependented data.

.. seealso::

  TODO

.. _chaining-of-systems-2-3:

Chaining of Systems
~~~~~~~~~~~~~~~~~~~

Microservices are easily re-used if they do generic stuff.

The point of chaining microservices or API’s is to use multiple generic,
simple services to solve a bigger complex problem.

Pros: Usually re-use of microservices makes development time shorter

Cons: Debugging can be complex and unforeseen issues hard to find &
pinpoint. Can’t see it in the graph, need to search the whole node
configuration to find the systems.

.. seealso::

  TODO

.. _tasks-for-systems-intermediate-2-3:

Tasks for Systems: Intermediate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
