.. co-existing_with_other_integration_services:

===========================================
Co-existing with other integration services
===========================================


Having multiple integration/data sync services running between the same systems is generally not recommended as this can lead to an artificial influx in duplicate entities unless you configure the other services correctly.

For example, using HubSpot Data Sync (HSDS) or Zapier to detect if a new product has been created in HubSpot, and then onboard Sesam Talk, the consequences will be duplicate products in each system. Some systems have logics preventing this from growing indefinitely, but we have seen examples of this getting out of hand.

If you still want to use another integration service alongside of Sesam Talk, please ensure that the two solutions aren’t synchronizing the same data/properties.
