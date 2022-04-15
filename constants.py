WORKING_DIRECTORY = "C:/Users/bfrem/Documents/CloudComputing/omnetpp-5.7-windows-x86_64/omnetpp-5.7/samples/inet4/examples/inet/DatacenterTopologies"
GENERATED_FILES_DIR = "generated_files"

PACKAGE = "inet.examples.inet.DatacenterTopologies"

IMPORTS = [
    "inet.networklayer.configurator.ipv4.Ipv4NetworkConfigurator",
    "inet.node.inet.Router",
    "inet.node.inet.StandardHost",
    "ned.DatarateChannel",
    "inet.visualizer.integrated.IntegratedVisualizer"
]

DEFAULT_CHANNEL = "defaultline"
DEFAULT_LINE_PARAMS = {
    "delay": "1us",
    "datarate": "8Mbps",
    "per": "0"
}

INFINITE_CHANNEL = "infiniteline"
INFINITE_LINE_PARAMS = {
    "delay": "0s",
    "datarate": "1000Gbps",
    "per": "0"
}

TAB = "    "

SIZE_SMALL = "s"
SIZE_VERY_SMALL = "vs"

ICON_ROUTER = "abstract/router"
ICON_SOURCE = "block/source"
ICON_SINK = "block/sink"
ICON_PC = "device/pc"
ICON_LAPTOP = "device/laptop"
ICON_SERVER = "device/server"
ICON_CONFIGURATOR = "block/cogwheel"
ICON_VISUALIZER = "block/app"
ICON_SWITCH = "device/switch"

NED_CONFIGURATOR = "Ipv4NetworkConfigurator"
NED_VISUALIZER = "IntegratedVisualizer"
NED_ROUTER = "Router"
NED_STANDARD_HOST = "StandardHost"

"""
ROUTER_NED = "Router"
ROUTER_TYPE = "Router"
ROUTER_SIZE = "s"
ROUTER_ICON = "abstract/router"

STANDARD_HOST_NED = "StandardHost"
CLIENT_TYPE = "Client"
SERVER_TYPE = "Server"
STANDARD_HOST_SIZE = "s"
CLIENT_ICON = "device/laptop"
SERVER_ICON = "device/server"
"""

SERVER_PORT = 1100
REQUEST_SIZE = 1300
RESPONSE_SIZE = 20
SIMULATION_TIME = 1000