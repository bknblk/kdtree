#TODO: im scared to test it
# The goal is that the KDTree cna be called like an sklearn object
# Like kd = KDTree(), then appended onto with the append command
# The network of classes should provide a decent framework with safety

#imports I think we'll need:
#import networkx
#import numpy as np
#from sklearn.neighbors import KNeighborsClassifier
#import pandas as pd
from dataclasses import dataclass
import typing as t


data = ('name','age','profession','salary')

class KDerror(Exception):
    def __init__(self, msg="Error in file"):
        self.msg = msg
        super().__init__(self.msg)


@dataclass(frozen = True, slots = True, kw_only = True)
class Data:
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
                KDerror(f"{key} not recognized in keyword arguments")
                exit
        self.value = Data(**kwargs)

    def __str__(self):
        return f"Node containing {self.value}"

    def __gt__(self, other, by):
        for f in self.value.Fields():
            if f.name == by:
                type_of_by = f.type
        if type_of_by == int:
            if self.value.by > self.value.by:
                return True
            if self.value.by < self.value.by:
                return False
        elif type_of_by == str: #implemented backwards so A is greater then B
            if self.value.by > self.value.by:
                return False
            if self.value.by < self.value.by:
                return True
        else:
            KDError("Error in function")
            exit
            
    def __lt__(self == other, by):
        for f in self.value.Fields():
            if f.name == by:
                type_of_by = f.type
        if type_of_by == int:
            if self.value.by < self.value.by:
                return True
            if self.value.by > self.value.by:
                return False
        elif type_of_by == str: #implemented backwards so A is greater then B
            if self.value.by < self.value.by:
                return False
            if self.value.by > self.value.by:
                return True
        else:
            KDError("Error in function")
            exit
            

    def depth(self):
        ldepth = depth(self.left)
        rdepth = depth(self.right)
        return (1 + max(ldepth + rdepth))


class KDTree:

    def __init__(self, head, data):
        self.head = head
        self.data = data

    def append(self, data:Node): 
        max_depth = self.head.depth()
        curr_node = self.head
        curr_depth = 0
        for i in range(len(curr_depth)):
            attr = data[i+1%len(data)]
            if data.attr > curr_node.attr:
                curr_node = curr_node.right
            if data.attr < curr_node.attr:
                curr_node = curr_node.left
        if data.attr > curr_node.attr:
            curr_node.right = data
        if data.attr < curr_node.attr:
            curr_node.left = data
    def __str__(self):
        return f"KD tree with dimension {len(self.data)} and depth {self.head.depth}"
