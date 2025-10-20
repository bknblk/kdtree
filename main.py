import networkx
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from dataclasses import dataclass
import typing as t

data = ('name','age','profession','salary')

class KDerror(Exception):
    def __init__(self, msg="Error in file"):
        self.msg = msg
        super().__init__(self.msg)

@dataclass
class data:
    name: str
    age: int
    profession: str
    salary: int

class Node:
    def __init__(self, by, **kwargs):
        self.by = None
        self.value = None
        self.right = None
        self.left = None
        for key in list(kwargs.keys()):
            if key not in data:
                KDerror("key not recognized in keyword arguments")
                exit
        self.value = data(**kwargs)

class KDTree:
    def __init__(self, head):
        self.head = head
    def depth(self): #TODO: this is broke
        first_node = self.head
        ldepth = depth(first_node.left)
        rdepth = depth(first_node.right)
        return (1 + max(ldepth + rdepth))
    def append(self, data:Node): #TODO: this is broke bc depth is broke. If you fix depth it should work fine
        curr_depth = depth()
        curr_node = self.head
        curr_depth = 0
        for _ in range(len(curr_depth)):
            attr = data[curr_depth%len(data)]
            if data.attr > curr_node.attr:
                curr_node = curr_node.right
            if data.attr < curr_node.attr:
                curr_node = curr_node.left
        if data.attr > curr_node.attr:
            curr_node.right = data
        if data.attr < curr_node.attr:
            curr_node.left = data
