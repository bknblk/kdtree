import graphviz
from dataclasses import dataclass, fields, asdict
import typing as t
from collections import deque


data = ("name", "age", "profession", "salary")


class KDerror(Exception):
    def __init__(self, msg="Error in file"):
        self.msg = msg
        super().__init__(self.msg)


@dataclass(frozen=True, slots=True, kw_only=True)
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
        return 1 + max(ldepth, rdepth)

    def show_tree(self):
        print(self.value.name)
        if self.left:
            print(f"--left of {self.value.name}--")
            self.left.show_tree()
        if self.right:
            print(f"--right of {self.value.name} --")
            self.right.show_tree()

    def append(self, new_node, iteration=0):
        node_fields = fields(self.value)
        attr = [i.name for i in node_fields][iteration % len(node_fields)]
        if getattr(new_node.value, attr) >= (getattr(self.value, attr)):
            if self.right:
                self.right = self.right.append(new_node, iteration=iteration + 1)
            else:
                self.right = new_node
        elif getattr(new_node.value, attr) < (getattr(self.value, attr)):
            if self.left:
                self.left = self.left.append(new_node, iteration=iteration + 1)
            else:
                self.left = new_node
        return self

    @classmethod
    def build_balanced(cls, data_list):
        sidx = {"name": [], "age": [], "profession": [], "salary": []}
        for key in sidx.keys():
            capture = list(enumerate(data_list))
            cap_sort = sorted(capture, key=lambda x: getattr(x[1], key))
            sidx[key] = [a[0] for a in cap_sort]
        return cls._build_recursive(sidx, data_list)

    @staticmethod
    def _build_recursive(sidx, data, iteration=0):
        med = lambda lst: lst[len(lst) // 2]
        if len(sidx["name"]) == 0:
            return None
        if len(sidx["name"]) == 1:
            idx = sidx["name"][0]
            return Node(**asdict(data[idx]))

        dimensions = ["name", "age", "profession", "salary"]
        current_dim = dimensions[iteration % len(dimensions)]
        median_idx = med(sidx[current_dim])
        median_data = data[median_idx]
        median_value = getattr(median_data, current_dim)
        node = Node(**asdict(median_data))
        left_sidx = {dim: [] for dim in dimensions}
        right_sidx = {dim: [] for dim in dimensions}
        for dim in dimensions:
            for idx in sidx[dim]:
                if idx == median_idx:
                    continue
                if getattr(data[idx], current_dim) < median_value:
                    left_sidx[dim].append(idx)
                else:
                    right_sidx[dim].append(idx)
        node.left = Node._build_recursive(left_sidx, data, iteration + 1)
        node.right = Node._build_recursive(right_sidx, data, iteration + 1)

        return node

    def vis(self, ax):  # if this vis doesnt work, take out the else statements
        out = ""
        for key, value in asdict(self.value).items():
            out += f"{key}: {value}\n"
        ax.node(self.value.name, out)
        if self.left:
            ax.edge(self.value.name, self.left.value.name)
            self.left.vis(ax)
        else:
            ax.edge(self.value.name, self.value.name, style="invis")
        if self.right:
            ax.edge(self.value.name, self.right.value.name)
            self.right.vis(ax)
        else:
            ax.edge(self.value.name, self.value.name, style="invis")


if __name__ == "__main__":
    head = Node(name="Roman", age=20, profession="Army", salary=2)
    data = []
    data.append(Data(name="Jonah", age=21, profession="Data Scientist", salary=0))
    data.append(Data(name="Ty", age=22, profession="USMC", salary=3600))
    data.append(Data(name="Nathan", age=19, profession="nerd", salary=0))
    data.append(Data(name="Evan", age=21, profession="Pilot", salary=100))
    data.append(Data(name="Faisal", age=30, profession="Professor", salary=20))
    data.append(Data(name="Robert", age=27, profession="Contruction", salary=400))
    data.append(Data(name="Sophia", age=24, profession="Designer", salary=55))
    data.append(Data(name="Liam", age=35, profession="Manager", salary=95))
    data.append(Data(name="Emma", age=22, profession="Intern", salary=15))
    data.append(Data(name="Oliver", age=29, profession="Developer", salary=80))
    data.append(Data(name="Ava", age=31, profession="Analyst", salary=65))
    data.append(Data(name="Noah", age=26, profession="Consultant", salary=70))
    data.append(Data(name="Isabella", age=23, profession="Assistant", salary=35))
    data.append(Data(name="Ethan", age=33, profession="Architect", salary=90))
    data.append(Data(name="Mia", age=25, profession="Researcher", salary=50))
    data.append(Data(name="Lucas", age=27, profession="Technician", salary=45))
    data.append(Data(name="Charlotte", age=30, profession="Director", salary=110))
    data.append(Data(name="Mason", age=24, profession="Coordinator", salary=40))
    data.append(Data(name="Amelia", age=32, profession="Specialist", salary=68))
    data.append(Data(name="James", age=29, profession="Administrator", salary=52))
    data.append(Data(name="Harper", age=26, profession="Scientist", salary=72))
    data.append(Data(name="Benjamin", age=34, profession="Supervisor", salary=85))
    data.append(Data(name="Evelyn", age=23, profession="Trainee", salary=25))
    data.append(Data(name="Logan", age=28, profession="Operator", salary=48))
    data.append(Data(name="Abigail", age=31, profession="Executive", salary=105))
    sidx = {"name": [], "age": [], "profession": [], "salary": []}
    for key, _ in sidx.items():
        capture = list(enumerate(data))
        cap_sort = sorted(capture, key=lambda x: getattr(x[1], key))
        sidx[key] = [a[0] for a in cap_sort]

    #for datum in data:
    #    head.append(datum)

    head = Node.build_balanced(data)

    dot = graphviz.Digraph()
    head.vis(dot)
    dot.render("kdtree", format="png")
