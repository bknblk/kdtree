#imports I think we'll need:
#import graphviz
#import numpy as np
#from sklearn.neighbors import KNeighborsClassifier
#import pandas as pd
from dataclasses import dataclass, fields
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
    def __init__(self, **kwargs):
        self.value = None
        self.right = None
        self.left = None
        self.depth = None
        for key in list(kwargs.keys()):
            if key not in data:
                KDerror(f"{key} not recognized in keyword arguments")
                exit
        print(kwargs)
        self.value = Data(**kwargs)

    def __str__(self):
        return f"Node containing {self.value}"


    def __gt__(self, other, by):
        for f in self.value.fields():
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
            
    def __lt__(self, other, by):
        for f in self.value.fields():
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
        ldepth = 0
        rdepth = 0
        if self.left is not None:
            ldepth = depth(self.left)
        if self.right is not None:
            rdepth = depth(self.right)
        return (1 + max(ldepth, rdepth))


class KDTree:
# there might be an indexing problem, unsure honestly. Root node should be 0, but I think in the for loop its represented as 1. TODO
    def __init__(self, head):
        self.head = head
        self.head.depth = 0

    def append(self, new_node:Node):
        print(self.head)
        max_depth = self.head.depth()
        curr_node = self.head
        curr_depth = 1
        for i in range(max_depth):
            attr = [i.name for i in fields(new_node.value)][i%len(data)]
            print(f'attr={attr}')
            if getattr(new_node.value, attr) > getattr(curr_node.value, attr) and curr_node.right!=None:
                curr_node = curr_node.right
            if getattr(new_node.value, attr) < getattr(curr_node.value, attr) and curr_node.left!=None:
                curr_node = curr_node.left
        if getattr(new_node.value, attr) > getattr(curr_node.value, attr):
            curr_node.right = new_node
            curr_node.right.depth = i+1#idk if these are accurate yet
        if getattr(new_node.value, attr) < getattr(curr_node.value, attr):
            curr_node.left = new_node
            curr_node.left.depth = i+1#idk if these are accurate yet

    def __str__(self):
        for i in range(self.head.depth()):
            pass #TODO: implement, thinking like an ascii image with just the name



if __name__ == '__main__' :
    start_node = Node(name = 'Roman', age = '20', profession = 'Army', salary = '2')
    kd = KDTree(head = start_node)
    kd.append(Node(name = 'Jonah', age = '21', profession = 'Data Scientist', salary = '0'))

