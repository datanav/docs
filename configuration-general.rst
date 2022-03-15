General
=======

The *Sesam* service is configured using one or more `JSON <https://en.wikipedia.org/wiki/JSON>`_ files.
These configuration files can be imported through the service API. They can also be created and edited using the :doc:`Sesam Management Studio <management-studio>`.

Conceptually, the configuration files contains definitions for *Systems* and *Pipes*.

The configuration is a *JSON array* of :ref:`system <system_section>` and :ref:`pipe configurations <pipe_section>`. The configuration :doc:`entities <entitymodel>` are
*JSON objects* of the form:

::

    [
        {
            "_id": "some-solution-wide-unique-id",
            "name": "Name of component",
            "type": "component-type",
            "some-property": "some value"
        },
        {
            "_id": "some-other-solution-wide-unique-id",
            "name": "Name of other component",
            "type": "component-type",
            "some-other-property": "some other value"
        }
    ]

It should be noted that all ``_id`` property values must be unique across across the solution. This means unique within the *sesam.conf.json* file but also across all files when a multiple file configuration is used.
