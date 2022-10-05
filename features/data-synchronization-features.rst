.. _data-synchronization-features:

.. rst-class:: center-title

====================
Data synchronization
====================

Sesam offer a set of features that will give you the edge when it comes to Master Data synchronization. Below is a list of core features Sesam offers.

|
|
|


.. panels::
    :body: text-left
    :container: container-lg pb-3
    :column: col-lg-4 col-md-4 col-sm-6 col-xs-12 p-2 custom-card
    
    :badge:`Free feature,badge-success badge-pill`

    **Scheduling and Signalling**

    Automatically signals downstream pipes when data changes upstream.

    .. link-button:: /features/scheduling-and-signalling
            :type: ref
            :text: Read more
            :classes: read-more
    ---
    :badge:`Free feature,badge-success badge-pill`

    **Change tracking**

    Compare incoming entities with the existing version and only apply updates if the version are different.

    .. link-button:: /features/change-tracking
            :type: ref
            :text: Read more
            :classes: read-more
    ---
    :badge:`Free feature,badge-success badge-pill`

    **Extensions**

    Build and run your own microservice extension systems.

    .. link-button:: /features/extensions-feature
            :type: ref
            :text: Read more
            :classes: read-more
    ---
    :badge:`Free feature,badge-success badge-pill`

    **Continuation Support**

    Allows a pipe to process changes incrementally. The next time the pipe runs it will continue where the previous run finished.

    .. link-button:: /features/continuation-support
            :type: ref
            :text: Read more
            :classes: read-more
    ---
    :badge:`Free feature,badge-success badge-pill`

    **Deletion Tracking**

    Allows a dataset sink to effectively detect if entities have disappeared from the source.

    .. link-button:: /features/deletion-tracking
            :type: ref
            :text: Read more
            :classes: read-more
    ---
    :badge:`Free feature,badge-success badge-pill`

    **Circuit Breakers**

    A circuit breaker will trip if a larger than expected number of entities are written to a dataset in a pipe run.

    .. link-button:: /features/circuit-breakers
            :type: ref
            :text: Read more
            :classes: read-more
    ---
    :badge:`Free feature,badge-success badge-pill`
    
    **Transit Encoding**

    Transit Encoding is a technique for encoding a larger set of data types in JSON.

    .. link-button:: /features/transit-encoding
            :type: ref
            :text: Read more
            :classes: read-more

|

.. toctree::
   :maxdepth: 1
   :hidden:

   Scheduling and Signalling <scheduling-and-signalling>
   Change Tracking <change-tracking>
   Extensions <extensions-feature>
   Continuation Support <continuation-support>
   Deletion Tracking <deletion-tracking>
   Circuit breakers <circuit-breakers>
   Transit Encoding <transit-encoding>
