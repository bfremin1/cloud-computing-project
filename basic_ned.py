from constants import *

class Connection:
    def __init__(self, gate_strings, channel):
        assert len(gate_strings) == 2
        self._gates = sorted(gate_strings)
        self._channel = channel
    
    def ned_connection(self):
        return f"{self._gates[0]} <--> {self._channel} <--> {self._gates[1]};"

class Line:
    def __init__(self, channel=DEFAULT_CHANNEL, params=DEFAULT_LINE_PARAMS):
        self._channel = channel
        self._params = params
    
    def ned_type(self):
        return (
            f"channel {self._channel} extends DatarateChannel" +
            " { " +
            "; ".join([f"{k} = {v}" for (k, v) in self._params.items()]) +
            "; }"
        )
    
    def get_channel(self):
        return self._channel

class Configurator:
    def __init__(self, x, y, name="configurator"):
        self._name = name
        self._x = int(x)
        self._y = int(y)
        self._size = "s"
        self._icon = ICON_CONFIGURATOR
    
    def ned_submodule(self):
        return (
            f"{self._name}: Ipv4NetworkConfigurator" +
            " { parameters:" +
            f" @display(\"p={self._x},{self._y};i={self._icon};is={self._size}\");" +
            " }"
        )

class Visualizer:
    def __init__(self, x, y, name="visualizer"):
        self._name = name
        self._x = int(x)
        self._y = int(y)
        self._size = "s"
        self._icon = ICON_VISUALIZER
    
    def ned_submodule(self):
        return (
            f"{self._name}: IntegratedVisualizer" +
            " { parameters:" +
            f" @display(\"p={self._x},{self._y};i={self._icon};is={self._size}\");" +
            " }"
        )