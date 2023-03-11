from info import info
import networkx as nx

def compute_tree_decomposition(graph):
  """
  Computes the tree decomposition of a given graph.
  Returns a list of bags for each node in the tree.
  """

  # http://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.approximation.treewidth.treewidth_min_degree.html
  _, td = nx.algorithms.approximation.treewidth_min_degree(graph)
  bags = [td[node] for node in td]
  return bags

def handle(pb2_request, repo_path):
  # https://pacechallenge.wordpress.com/pace-2016/track-a-treewidth/
  graph = nx.Graph()
  graph.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5)])

  bags = compute_tree_decomposition(graph)

  for i, bag in enumerate(bags):
    print(f"Node {i}: {bag}")
