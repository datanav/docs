.. _bring-your-own-key:
.. _bring_your_own_key:

:badge:`Free feature,badge-success badge-pill`

Bring Your Own Key
==================

In a hosted Sesam subscription data is stored on disks and backups are written to a remote geo-replicated storage account. By default these disks and the associated storage account are encrypted by a platform managed key. In practice this means that it is the cloud provider that manages the encryption keys. Sesam has also implemented support for bring your own key (BYOK). In practice Sesam then manages the encryption key for you. The advantage is that you can then decide to revoke the key when you need to. Note that this generally requires that the data then must be able to be reloaded by Sesam afterwards. This is an opt-in feature that can be enabled on new single subscriptions. It is not yet supported for multi subscriptions. Contact `support <https://support.sesam.io/>`_ if you would like to enable BYOK for a new subscription.