.. _vpn-feature:

:badge:`Paid feature,badge-info badge-pill`

VPN
===

You can extend Sesam into your own network using an IPSec-based virtual private network. You can configure a VPN under Subscriptions Settings in the Management Studio. Note that there is an additional surcharge for VPN, see :ref:`pricing` for more information.

How to enable VPN
-----------------
To enable the VPN feature on your subscription:

- Login to portal.sesam.io

- Navigate to Subscription on the left menu

- Click on Products tab

- Tick the checkbox "Enable VPN"

Navigate to Subscription on the left menu and select the new VPN tab. This is where the rest of the configuration will be done.

Take note of the Sesam Peer VPN Gateway and Sesam address spaces and configure your on-premises VPN device accordingly.
You can find a list of supported VPN devices and configuration guides at `https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpn-devices <https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpn-devices>`_.

Finally under "Add or modify VPN details" fill in the required fields to setup the actual connection between Sesam and your on-premises network:

- Gateway Address:  on-premises VPN device IP address or FQDN.

- Address Spaces: Sesam will route the address range that you specify to the on-premises VPN device IP address.

- Pre-shared Key: a string of characters that is used as an authentication key between Sesam and the on-premises VPN device.

.. NOTE::

   :ref:`Multi compute <pricing-production>` subscriptions support highly available VPN configurations. This lets you set up redundant BGP (Border Gateway Protocol) enabled connections that can be failed over to. Contact support to set up this kind of VPN connection.
