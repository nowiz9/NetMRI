from ..remote import RemoteModel


class ProxyModelNetworkExplorerInventorySummaryGridRemote(RemoteModel):
    """



    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPDotted:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``DeviceName:`` none
    |  ``attribute type:`` string

    |  ``DeviceType:`` none
    |  ``attribute type:`` string

    |  ``DeviceVersion:`` none
    |  ``attribute type:`` string

    |  ``PhysicalSerialNum:`` none
    |  ``attribute type:`` string

    |  ``DeviceVendor:`` none
    |  ``attribute type:`` string

    |  ``DeviceModel:`` none
    |  ``attribute type:`` string

    """

    properties = ("DeviceID",
                  "DeviceIPNumeric",
                  "DeviceIPDotted",
                  "VirtualNetworkID",
                  "Network",
                  "DeviceName",
                  "DeviceType",
                  "DeviceVersion",
                  "PhysicalSerialNum",
                  "DeviceVendor",
                  "DeviceModel",
                  )
