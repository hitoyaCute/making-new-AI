import FUNC
from exception import *


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
    def forward(self, edges: list[list[float]]):
        ...
class edge_layer:
    def __init__(self, edge_count:int):
        self.edges = tuple([edge(1) for _ range(edge_count)])
        self.__len = edge_count
    def __call__(self, values: list[float]) -> list[list[float]]:
        val_len = len(values)
        if self.__len % val_len != 0:
            raise ShapeError("invalid value shape")
        
        sub_group = []
        output : list[list[float]] = []
        for i in range(self.__len):
            sub_group.append(values[i%val_len] * self.edges[i])
            if i % val_len == 0:
                output.append(sub_group.copy())
                sub_group.clear()
        return output

class construct:
    def __init__(self, input_count, *network: ACTIVATION | node_layer | edge_layer):
        self.input = input_count
        self.network = network
    def forward(self, input_val: list[float]):
        ...
    def loss(self, target: list[float], input_val:list[float])::
        ...
