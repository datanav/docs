.. _concepts-systems:

Systems
=======

A :ref:`system <system_section>` is any database or API that could be used as a source of data for Sesam or as the target of entities coming out of Sesam. The system components provide a way to represent the actual systems being connected or integrated.

The system component has a couple of uses. Firstly it can be used to introspect the underlying system and provide back lists of possible source or sink targets. Often this information can be used on the command line or in the *Sesam Management Studio* to quickly and efficiently configure how Sesam consumes or delivers data.

The other use of the *system* is that it allows configuration that may apply to many *source* definitions, e.g. connection strings, to be located and managed in just one place.

Systems also provide services like connection pooling and rate limiting.

You can also run your own :ref:`extension systems <extensions-feature>`.
