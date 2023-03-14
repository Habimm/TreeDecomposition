from info import info
import networkx

# Examples are here:
# https://github.com/PACE-challenge/Treewidth-PACE-2017-instances/blob/master/gr/exact/ex001.gr.xz

def compute_tree_decomposition(graph):
  # Compute the tree decomposition using the treewidth_min_degree algorithm
  _, tree_decomposition = networkx.algorithms.approximation.treewidth_min_degree(graph)
  info(tree_decomposition)

  # Compute the bags for each node in the tree decomposition
  bags = tree_decomposition.nodes()
  info(bags)

  bag_numbers = {}
  for i, bag in enumerate(bags):
    bag_numbers[bag] = i + 1

  # Compute the maximum bag size
  max_bag_size = max(len(bag) for bag in bags)
  info(max_bag_size)

  # Output the tree decomposition in the specified format
  output = f"c This file describes a tree decomposition with {len(bags)} bags, width {max_bag_size - 1}, for a graph with {len(graph)} vertices\n"
  output += f"s td {len(bags)} {max_bag_size} {len(graph)}\n"

  for bag in tree_decomposition:
    bag_str = " ".join(str(vertex) for vertex in bag)
    bag_number = bag_numbers[bag]
    output += f"b {bag_number} {bag_str}\n"

  for bag in tree_decomposition:
    bag_number = bag_numbers[bag]
    for neighbor in tree_decomposition.neighbors(bag):
      neighbor_number = bag_numbers[neighbor]
      if neighbor_number > bag_number:
        output += f"{bag_number} {neighbor_number}\n"

  return output

def handle(pb2_request, repo_path):
  gr_format = pb2_request.input.decode('utf-8')
  info(gr_format)

  graph = networkx.Graph()
  lines = gr_format.split('\n')
  for line in lines:
    if line.startswith('c'):
      continue
    elif line.startswith('p'):
      p, tw, n_nodes, _ = line.split()
      assert p == 'p' and tw == 'tw'
      n_nodes = int(n_nodes)
      graph.add_nodes_from(range(1, n_nodes+1))
    elif line:
      u, v = map(int, line.split())
      graph.add_edge(u, v)

  tree_decomp_str = compute_tree_decomposition(graph)

  print(tree_decomp_str)
  return tree_decomp_str
