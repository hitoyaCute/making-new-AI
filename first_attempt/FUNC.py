import math as m
from math import e,pi
from math import tanh as mtanh
from typing import Protocol


class ACTIVATION(Protocol):
    """This is the perent class that contains call and derivetive call"""
    @staticmethod
    def __call__(x:float) -> float:
        raise TypeError("object 'ACVTIVATION' is not callable ")
    @staticmethod
    def dif(x:float) -> float:
        raise TypeError("ACVTIVATION.dif is not callable ")




class relu:
    @staticmethod
    def __call__(x:float) -> float:
        """formula
        relu = max(0, x)
        """
        return 0 if x < 0 else x
    @staticmethod
    def dif(x):
        return 1

class tanh:
    @staticmethod
    def __call__(x:float) -> float:
        """formula
                e^x - e^(-x)
        tanh = --------------
                e^x + e^(-x)
        """
        return (m.pow(e,x) - m.pow(e,-x))/(m.pow(e,x)+m.pow(e,-x))
    @staticmethod
    def dif(x:float) -> float:
        """formula 
        tanh' = 1 - tanh(x)^2
        """
        return 1 - (mtanh(x) ** 2)

