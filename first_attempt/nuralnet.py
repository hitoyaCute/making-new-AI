from FUNC import ACTIVATION


class NEURON:
    def __init__(self, bias:float):
        self.bias = bias
    def __call__(self, value:float) -> float:
        return self.bias + value
    def dif(self, value: float) -> float:
        return 1 + self.bias
class EDGE:
    def __init__(self, weigth: float):
        self.weigth = weigth
    def __call__(self, value:float) -> float:
        """takes a value, apply to the parent node, the multiply that output to the weigth"""
        return value * self.weigth
    def dif(self) -> float:
        return self.weight

class Layer:
    def __init__(self,num_of_nodes:int):
        self.nodes = [NEURON(0) for i in range(num_of_nodes)]
    def forward(self, values:list[float]) -> list[float]:
        """"""
        prev_layer_num = len(values)//len(self.nodes)
        if len(values)%len(self.nodes) == 0:
            raise ValueError("incompatible value has been feed to the layer")
        return [nuron(sum(value[i:i+prev_layer_num])) for i,nuron in enumerate(self.nodes)]
    

    def backward(self, divs:list[float]) -> list[float]:
        pass


class Construct:
    def __init__(self, layers:list[Layer | ACTIVATION]):
        self.layers = layers
