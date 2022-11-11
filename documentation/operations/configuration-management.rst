========================
Configuration Management
========================

When setting up a new Sesam project there are several tasks that needs to be done in order to ensure a good working environment for the project and its team. One thing is the Sesam installation itself, but in every software development project, concepts such as version control, continuous integration (CI) testing and automatic deployment are key factors for a successful project.

As a product, Sesam in itself does not contain any features that supports versioning of its configuration, local or automated CI testing and automatic deployment, but it provides a set of features (mostly through its API) that can be used in regular development tools or scripts for this purpose. This is flexible in terms of requirements set by the various customer, whose development platforms might vary. It does, however, mean that some time must be spent at the beginning of the project. In this document we will go through how to setup a Sesam project with these features, with examples and links to more in-depth documents.
 
.. toctree::
   :maxdepth: 2

   Using Sesam with a version control system <version-control-system>
   Testing a Sesam configuration locally <testing-locally>
   Continuous integration <continuous-integration>
   Automatic deployment <automatic-deployment>
