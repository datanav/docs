Introduction
============

The Data Transformation Language (DTL) has been created as a means to allow developers to clearly describe transformations that should be performed on streams of data in order to create new datasets.

Core Concepts
-------------

DTL allows developers to describe a data transform. The DTL processor applies the transform to a stream of entities. For each entity in the stream the same transform is applied. The result of processing is a stream of new entities.

An entity coming into a DTL transform is called the *source entity*. The DTL transform describes how to construct new entities from the source entity. A transform can also perform hops that range across datasets in the datahub. These hops must start from the source entity.

DTL consists of 'functions' that can pick and transform data and 'hops' that can traverse the data in the datahub. In combination these offer a powerful way to construct new data entities from existing data. DTL functions are composable and thus allowing complex computation to be expressed.

Syntax
------

DTL uses a JSON syntax to describe the transforms to perform. This allows us to define it directly in the pipe's configuration, which is also written in JSON. In general, DTL uses functions over keywords and as such there are just a few terms that are baked into the language.

An example using the ``add`` transform:

.. code-block:: json

  ["add", "name", "_S.firstname"]

And composing functions:

.. code-block:: json

  ["add", "name", ["concat", ["upper", "_S.lastname"], ", ", "_S.firstname"]]
