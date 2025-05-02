import FUNC

class node:
    def __init__(self, bias):
        ...
class edge:
    def __init__(self, wieght):
        ...
class node_layer:
    def __init__(self, node_count:int):
        ...
class edge_layer:
    def __init__(self, edge_count:int):
        ...
class construct:
    def __init__(self, input_count, *netqork: ACTIVATION | node_layer | edge_layer):
        ...
