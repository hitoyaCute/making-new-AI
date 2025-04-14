import math as m
from math import e,pi


class ACTIVATION:
    """This is the perent class that contains call and derivetive call"""
    @staticmethod
    def __call__(x:float) -> float:
        raise TypeError("object 'ACVTIVATION' is not callable ")
    @staticmethod
    def dif(x:float) -> float:
        raise TypeError("ACVTIVATION.dif is not callable ")




class relu(ACTIVATION):
    @staticmethod
    def __call__(x):
        """formula
        relu = max(0, x)
        """
        return 0 if x < 0 else x
    @staticmethod
    def dif(x):
        return 1

class tanh(ACTIVATION):
    @staticmethod
    def __call__(x):
        """formula
                e^x - e^(-x)
        tanh = --------------
                e^x + e^(-x)
        """
        return (m.pow(e,x) - m.pow(e,-x))/(m.pow(e,x)+m.pow(e,-x))
    @staticmethod
    def dif(x):
        """formula 
        tanh' = 1 - tanh(x)^2
        """
        return 1 - (tanh(x) ^ 2)

