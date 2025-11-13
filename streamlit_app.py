'''
File: streamlit_app.py
Purpose: Streamlit web interface for KD tree visualization and interaction
Version: See github.com/bknblk/kdtree
Resources: Claude AI was used to verify the integrity of the KD tree.
'''
import streamlit as st
import graphviz
from dataclasses import dataclass, fields, asdict
from main import Node, Data, data as data_fields
import io

st.set_page_config(page_title="KD Tree Visualizer", layout="wide")

# data storage
if 'data_list' not in st.session_state:
    st.session_state.data_list = []
if 'tree' not in st.session_state:
    st.session_state.tree = None

# title and footnote
st.title("KD Tree Visualizer")
st.markdown("Interactive visualization of a balanced K-Dimensional tree")

# sidebar for data input
st.sidebar.header("Add Data Points")

with st.sidebar.form("add_data_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=120, value=25)
    profession = st.text_input("Profession")
    salary = st.number_input("Salary (in thousands)", min_value=0, value=50)

    submitted = st.form_submit_button("Add Person")
    if submitted and name and profession:
        new_data = Data(name=name, age=age, profession=profession, salary=salary)
        st.session_state.data_list.append(new_data)
        st.success(f"Added {name}!")

# sidebar actions
st.sidebar.header("Actions")
if st.sidebar.button("Build Balanced Tree"):
    if len(st.session_state.data_list) > 0:
        st.session_state.tree = Node.build_balanced(st.session_state.data_list)
        st.sidebar.success("Tree built successfully")
    else:
        st.sidebar.error("Add some data first")

if st.sidebar.button("Load Sample Data"):
    st.session_state.data_list = [
        Data(name="Jonah", age=21, profession="Data Scientist", salary=0),
        Data(name="Ty", age=22, profession="USMC", salary=3600),
        Data(name="Nathan", age=19, profession="nerd", salary=0),
        Data(name="Evan", age=21, profession="Pilot", salary=100),
        Data(name="Faisal", age=30, profession="Professor", salary=20),
        Data(name="Robert", age=27, profession="Construction", salary=400),
        Data(name="Sophia", age=24, profession="Designer", salary=55),
        Data(name="Liam", age=35, profession="Manager", salary=95),
        Data(name="Emma", age=22, profession="Intern", salary=15),
        Data(name="Oliver", age=29, profession="Developer", salary=80),
        Data(name="Ava", age=31, profession="Analyst", salary=65),
        Data(name="Noah", age=26, profession="Consultant", salary=70),
        Data(name="Isabella", age=23, profession="Assistant", salary=35),
        Data(name="Ethan", age=33, profession="Architect", salary=90),
        Data(name="Mia", age=25, profession="Researcher", salary=50),
        Data(name="Lucas", age=27, profession="Technician", salary=45),
        Data(name="Charlotte", age=30, profession="Director", salary=110),
        Data(name="Mason", age=24, profession="Coordinator", salary=40),
        Data(name="Amelia", age=32, profession="Specialist", salary=68),
        Data(name="James", age=29, profession="Administrator", salary=52),
        Data(name="Harper", age=26, profession="Scientist", salary=72),
        Data(name="Benjamin", age=34, profession="Supervisor", salary=85),
        Data(name="Evelyn", age=23, profession="Trainee", salary=25),
        Data(name="Logan", age=28, profession="Operator", salary=48),
        Data(name="Abigail", age=31, profession="Executive", salary=105),
    ]
    st.sidebar.success("Sample data loaded!")
    st.rerun()

if st.sidebar.button("Clear All Data"):
    st.session_state.data_list = []
    st.session_state.tree = None
    st.sidebar.success("Data cleared")
    st.rerun()

#  main area
col1, col2 = st.columns([1, 2])

with col1:
    st.header("Current Data")
    if st.session_state.data_list:
        st.write(f"**Total entries:** {len(st.session_state.data_list)}")

        # displaying data in a table
        for i, person in enumerate(st.session_state.data_list):
            with st.expander(f"{i + 1}. {person.name}"):
                st.write(f"**Age:** {person.age}")
                st.write(f"**Profession:** {person.profession}")
                st.write(f"**Salary:** ${person.salary}k")
    else:
        st.info("No data added yet. Use the sidebar to add people or load sample data.")

with col2:
    st.header("Tree Visualization")

    if st.session_state.tree:
        # creating graphviz
        dot = graphviz.Digraph()
        dot.attr(rankdir='TB')
        dot.attr('node', shape='box', style='rounded,filled', fillcolor='lightblue')

        st.session_state.tree.vis(dot)

        st.graphviz_chart(dot)

        # Using find_depth to display some stats
        st.subheader("Tree Statistics")
        depth = st.session_state.tree.find_depth()
        st.metric("Tree Depth", depth)

    # The subheading that displays isntructions
    else:
        st.info("Build a KD tree to see the visualization")
        st.markdown("""
        ### How to use:
        1. **Add data points** using the sidebar
        2. click **'Load Sample Data'** for some sample data
        3. Click **'Build Balanced Tree'** to create the KD tree
        """)

# footer
st.sidebar.markdown("---")
st.sidebar.markdown("**KD Tree Project**")
st.sidebar.markdown("Authors: Roman Zalewski, Jonah Taylor")