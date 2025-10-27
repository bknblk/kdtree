import graphviz
from dataclasses import dataclass, fields, asdict
import typing as t
from collections import deque


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
            print(f'--left of {self.value.name}--')
            self.left.show_tree()
        if self.right:
            print(f'--right of {self.value.name} --')
            self.right.show_tree()


    def append(self, new_node,iteration=0):
        node_fields = fields(self.value)
        attr = [i.name for i in node_fields][iteration%len(node_fields)]
        if getattr(new_node.value, attr) >= (getattr(self.value, attr)):
            if self.right:
                self.right = self.right.append(new_node, iteration=iteration+1)
            else:
                self.right = new_node
        elif getattr(new_node.value, attr) < (getattr(self.value, attr)):
            if self.left:
                self.left = self.left.append(new_node, iteration=iteration+1)
            else:
                self.left = new_node
        return self._balance()

    def vis(self, ax):
        out = ''
        for key,value in asdict(self.value).items():
            out += f'{key}: {value}\n'
        ax.node(self.value.name,out)
        if self.left:
            ax.edge(self.value.name, self.left.value.name)
            self.left.vis(ax)
        if self.right:
            ax.edge(self.value.name, self.right.value.name)
            self.right.vis(ax)
    
    def _get_balance(self):
        lheight = 0
        rheight = 0
        if self.left:
            lheight = self.left.find_depth()
        if self.right:
            rheight = self.right.find_depth()
        return lheight - rheight

    def _rotate_l(self):
        new_head = self.right
        self.right = new_head.left
        new_head.left = self
        return new_head


    def _rotate_r(self):
        new_head = self.left
        self.left = new_head.right
        new_head.right = self
        return new_head
    
    def _rotate_rl(self):
        self.right = self.right._rotate_r()
        return self._rotate_l()

    def _rotate_lr(self):
        self.left = self.left._rotate_l()
        return self._rotate_r()

    def _balance(self):
        bal = self._get_balance()
        if bal > 1:
            cbal = self.left._get_balance()
            if cbal >= 0:
                return self._rotate_r()
            if cbal < 0:
                return self._rotate_lr()
        if bal < -1:
            cbal = self.right._get_balance()
            if cbal <= 0:
                return self._rotate_l()
            if cbal > 0:
                return self._rotate_rl()
        return self
        


            

if __name__ == '__main__' :
    head = Node(name = 'Roman', age = 20, profession = 'Army', salary = 2)
    head = head.append(Node(name = 'Jonah', age = 21, profession = 'Data Scientist', salary = 0))
    head = head.append(Node(name = 'Ty', age = 22, profession = 'USMC', salary = 3600))
    head = head.append(Node(name = 'Nathan', age=19, profession = 'nerd', salary = 0))
    head = head.append(Node(name = 'Evan', age=21, profession = 'Pilot', salary = 100))
    head = head.append(Node(name = 'Faisal',age=30, profession = 'Professor', salary = 20))
    head = head.append(Node(name = 'Robert', age= 27, profession = 'Contruction', salary = 400))
    head = head.append(Node(name='Sophia', age=24, profession='Designer', salary=55))
    head = head.append(Node(name='Liam', age=35, profession='Manager', salary=95))
    head = head.append(Node(name='Emma', age=22, profession='Intern', salary=15))
    head = head.append(Node(name='Oliver', age=29, profession='Developer', salary=80))
    head = head.append(Node(name='Ava', age=31, profession='Analyst', salary=65))
    head = head.append(Node(name='Noah', age=26, profession='Consultant', salary=70))
    head = head.append(Node(name='Isabella', age=23, profession='Assistant', salary=35))
    head = head.append(Node(name='Ethan', age=33, profession='Architect', salary=90))
    head = head.append(Node(name='Mia', age=25, profession='Researcher', salary=50))
    head = head.append(Node(name='Lucas', age=27, profession='Technician', salary=45))
    head = head.append(Node(name='Charlotte', age=30, profession='Director', salary=110))
    head = head.append(Node(name='Mason', age=24, profession='Coordinator', salary=40))
    head = head.append(Node(name='Amelia', age=32, profession='Specialist', salary=68))
    head = head.append(Node(name='James', age=29, profession='Administrator', salary=52))
    head = head.append(Node(name='Harper', age=26, profession='Scientist', salary=72))
    head = head.append(Node(name='Benjamin', age=34, profession='Supervisor', salary=85))
    head = head.append(Node(name='Evelyn', age=23, profession='Trainee', salary=25))
    head = head.append(Node(name='Logan', age=28, profession='Operator', salary=48))
    head = head.append(Node(name='Abigail', age=31, profession='Executive', salary=105))
    head.show_tree()
    dot = graphviz.Digraph()
    head.vis(dot)
    dot.render('kdtree', format='png')
    head.show_tree()
