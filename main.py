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
        self.value = Data(**kwargs)

    def __str__(self):
        return f"Node containing {self.value}"
            
    def find_depth(self):
        ldepth = 0
        rdepth = 0
        if self.left:
            ldepth = self.left.find_depth()
        if self.right:
            rdepth = self.right.find_depth()
        return (1 + max(ldepth, rdepth))

    def show_tree(self):
        print(self.value.name)
        if self.left:
            print('--left--')
            self.left.show_tree()
        if self.right:
            print('--right--')
            self.right.show_tree()


    def append(self, new_node,iteration=0):
        node_fields = fields(self.value)
        attr = [i.name for i in node_fields][iteration%len(node_fields)]
        if getattr(new_node.value, attr) >= (getattr(self.value, attr)):
            if self.right:
                self.right.append(new_node, iteration=iteration+1)
            else:
                self.right = new_node
        if getattr(new_node.value, attr) < (getattr(self.value, attr)):
            if self.left:
                self.left.append(new_node, iteration=iteration+1)
            else:
                self.left = new_node
        print(f'{new_node.value.name} added to tree')
            

if __name__ == '__main__' :
    head = Node(name = 'Roman', age = 20, profession = 'Army', salary = 2)
    head.append(Node(name = 'Jonah', age = 21, profession = 'Data Scientist', salary = 0))
    head.append(Node(name = 'Ty', age = 22, profession = 'USMC', salary = 3600))
    head.append(Node(name = 'Nathan', age=19, profession = 'nerd', salary = 0))
    head.show_tree()

