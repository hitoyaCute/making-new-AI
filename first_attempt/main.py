import FUNC

class node:
    def __init__(self, bias):
        self.bias = bias
    def __call__(self, value):
        return value + self.bias
class edge:
    def __init__(self, wiegth):
        self.weigth = weigth
    def __call__(self, value):
        return self.weigth * value
class node_layer:
    def __init__(self, node_count:int):
        ...
class edge_layer:
    def __init__(self, edge_count:int):
        ...
class construct:
    def __init__(self, input_count, *network: ACTIVATION | node_layer | edge_layer):
        self.input = input_count
        self.network = network
    def forward(self, input_val: list[float]):
        ...
    def loss(self, target: list[float], input_val:list[float])::
        ...
