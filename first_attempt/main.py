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
        self.nodes = [node(0) for _ in range(node_count)]

class edge_layer:
    def __init__(self, edge_count:int):
        self.edges = [edge(1) for _ range(edge_count)]
    def __call__(self, values: list[float]):
        ...
class construct:
    def __init__(self, input_count, *network: ACTIVATION | node_layer | edge_layer):
        self.input = input_count
        self.network = network
    def forward(self, input_val: list[float]):
        ...
    def loss(self, target: list[float], input_val:list[float])::
        ...
