.. _self-hosted-k8s:

=========================
Self-hosted on Kubernetes
=========================

.. Note::
   This is a draft document and is subject to change.

Introduction
------------

Sesam is offered as service that is either hosted for you in the cloud or you host it yourself. We generally
recommend the former, but there are scenarios where you would want to host it yourself. This document explains the
requirements and the installation steps necessary to get Sesam running on your Kubernetes cluster.

.. Note::
   Self hosted subscriptions are required to run the latest image of their chosen :ref:`software channel <software-channels>`.


Hardware requirements
---------------------

- One worker node with at least 8 CPU cores and 32 GB of RAM.

Software requirements
---------------------

- Kubernetes cluster running version 1.22 or newer.

Run Sesam in Google Kubernetes Engine(gke)
------------------------------------------

.. Note::
   As of now we only support `Azure Storage Accounts <https://docs.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal>`_ as backend for backing up the data in the cluster.


- Spin up the cluster with a dedicated node-pool consisting of at least one worker-node. We recommend using machine type n2-standard-8.
- Add the following label to the node-pool: sesam.io/nodepool: primary

.. Note::
   Before you proceed make sure you have access to the cluster with `kubectl <https://kubernetes.io/docs/reference/kubectl/kubectl/>`_.

Namespace
^^^^^^^^^
``kubectl create namespace sesam``

Durable storage
^^^^^^^^^^^^^^^
In order to persist the data in the cluster we need to configure a persistent volume (pvc).

::

    # pvc-sesam.yaml
    kind: PersistentVolumeClaim
    apiVersion: v1
    metadata:
      name: pvc-host-<worker-node-name-goes-here>
      namespace: sesam
    spec:
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 512Gi
      storageClassName: standard

Apply the pvc to the cluster: ``kubectl -n sesam apply -f pvc-sesam.yaml``

Install Sesam and other needed services to the cluster
------------------------------------------------------
We use helm-charts to install and manage the needed software in the cluster. Install `helm <https://helm.sh/docs/intro/install/>`_ on a client that has access to the cluster.

Add and initialize the needed Helm Chart Repositories:

| ``helm repo add bitnami https://charts.bitnami.com/bitnami`` 
| ``helm repo add traefik https://helm.traefik.io/traefik`` 
| ``helm repo add vm https://victoriametrics.github.io/helm-charts/`` 
| ``helm repo add sesam https://https://github.com/sesam-io/helm-charts/`` 

``helm repo update``

Install the helm-charts
-----------------------
In order to install the helm-charts you will need a license and various secrets. Contact `Sesam support <https://support.sesam.io/hc/en-us>`_ for assistance.

