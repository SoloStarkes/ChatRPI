import networkx as nx
import matplotlib.pyplot as plt

def create_dag():
    # Create a directed acyclic graph (DAG)
    dag = nx.DiGraph()

    # Define nodes and edges for the DAG
    nodes = ["a", "b", "c", "d", "e"]
    edges = [("a", "b"), ("a", "c"), ("b", "d"), ("c", "d"), ("d", "e")]

    # Add nodes and edges to the DAG
    dag.add_nodes_from(nodes)
    dag.add_edges_from(edges)

    return dag

def visualize_dag(dag):
    # Visualize the DAG
    pos = nx.spring_layout(dag)
    nx.draw(dag, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=8)
    plt.title("Directed Acyclic Graph (DAG)")
    plt.show()

def main():
    # Create a DAG
    my_dag = create_dag()

    # Visualize the DAG
    visualize_dag(my_dag)

if __name__ == "__main__":
    main()

    """
    The create_dag function creates a simple directed acyclic graph (DAG) with nodes "a" through "e" and edges connecting them.

    The visualize_dag function uses the networkx library to visualize the DAG using matplotlib.

    In the main function, we create a DAG and visualize it.

    To run this example, you'll need to have Python installed along with the networkx library (pip install networkx) and 
    matplotlib (pip install matplotlib). After running the program, you should see a visualization of the DAG, illustrating 
    the relationships between nodes.
    
    """