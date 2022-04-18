import networkx as nx
import random, copy

class RoutingAlgorithm:
    ECMP = "ECMP"
    KSP = "KSP"
    VLB = "VLB"

    @staticmethod
    def get_nx_graph(network):
        G = nx.Graph()
        for node in sorted(network._node_map.values(), key=lambda n: n.get_name()):
            G.add_node(node.get_name())
        for node in sorted(network._node_map.values(), key=lambda n: n.get_name()):
            for edge in node.get_nx_edges():
                if not G.has_edge(*edge):
                    G.add_edge(*edge)
        return G

    @staticmethod
    def k_shortest_paths(G, source, target, k):
        paths = []
        for path in nx.shortest_simple_paths(G, source, target):
            if len(paths) < k:
                paths.append(path)
            else:
                break
        return paths
    
    @staticmethod
    def all_shortest_paths(G, source, target):
        paths = []
        min_path_length = 999
        for path in nx.shortest_simple_paths(G, source, target):
            if len(path) < min_path_length:
                min_path_length = len(path)
                paths.append(path)
            elif len(path) == min_path_length:
                paths.append(path)
            else:
                break
        return paths

    @staticmethod
    def xml_route(from_node, to_node, dest_node):
        from_gate_index = from_node.gate_index_to(to_node)
        to_gate_index = to_node.gate_index_to(from_node)
        return f"<route hosts='{from_node.get_name()}' destination='{dest_node._ip_root}.0.8' netmask='255.255.255.255' gateway='{to_node._ip_root}.{to_gate_index}.8' interface='ppp{from_gate_index}' metric='0'/>"

    @staticmethod
    def path_route_xml_generator(network, path_finder, flow_src, flow_dest):
        server_src = network._node_map[flow_src].get_server_name()
        server_dest = network._node_map[flow_dest].get_server_name()
        path = path_finder(server_src, server_dest)
        path.insert(0, flow_src)
        path.append(flow_dest)
        if "source" in flow_src:
            network._node_map[flow_src]._flows[0]._path = path
        flow_dest_node = network._node_map[flow_dest]
        routes = [f"<!-- Route [ {', '.join(path)} ] -->"]
        for i in range(len(path) - 1):
            from_node = network._node_map[path[i]]
            to_node = network._node_map[path[i + 1]]
            routes.append(RoutingAlgorithm.xml_route(from_node, to_node, flow_dest_node))
        return routes

    @staticmethod
    def network_route_xml_generator(network, path_finder):
        routes = []
        # routes have the form below:
        # <route hosts="router0" destination="1.0.1.8" netmask="255.255.255.255" gateway="1.0.7.8" interface="ppp2" metric="0"/>
        for node in sorted(network._node_map.values(), key=lambda n: n.get_name()):
            for flow_src, flow_dest in node.get_flows_endpoints():
                routes.extend(RoutingAlgorithm.path_route_xml_generator(network, path_finder, flow_src, flow_dest))
                routes.extend(RoutingAlgorithm.path_route_xml_generator(network, path_finder, flow_dest, flow_src))
        return routes

    @staticmethod
    def ecmp_xml_routes(network):
        graph = RoutingAlgorithm.get_nx_graph(network)
        shortest_paths_sets = {}
        def path_finder(server_src, server_dest):
            server_src_dest = (server_src, server_dest) 
            if server_src_dest not in shortest_paths_sets.keys():
                shortest_paths_sets[server_src_dest] = RoutingAlgorithm.all_shortest_paths(graph, server_src_dest[0], server_src_dest[1])
            randomly_selected_path = random.sample(shortest_paths_sets[server_src_dest], 1)[0]
            return copy.deepcopy(randomly_selected_path)
        return RoutingAlgorithm.network_route_xml_generator(network, path_finder)
    
    @staticmethod
    def ksp_xml_routes(network, k):
        graph = RoutingAlgorithm.get_nx_graph(network)
        shortest_paths_sets = {}
        def path_finder(server_src, server_dest):
            server_src_dest = (server_src, server_dest) 
            if server_src_dest not in shortest_paths_sets.keys():
                shortest_paths_sets[server_src_dest] = RoutingAlgorithm.k_shortest_paths(graph, server_src_dest[0], server_src_dest[1], k)
            randomly_selected_path = random.sample(shortest_paths_sets[server_src_dest], 1)[0]
            return copy.deepcopy(randomly_selected_path)
        return RoutingAlgorithm.network_route_xml_generator(network, path_finder)
    
    @staticmethod
    def vlb_xml_routes(network):
        graph = RoutingAlgorithm.get_nx_graph(network)
        shortest_paths_sets = {}
        intermediate_nodes = [node.get_name() for node in network.get_categorized_nodes()['core']]
        def path_finder(server_src, server_dest):
            # Select a random intermeddiate node
            randomly_selected_intermediate = random.sample(intermediate_nodes, 1)[0]

            # ECMP routing from source to intermeddiate node
            src_dest = (server_src, randomly_selected_intermediate)
            if src_dest not in shortest_paths_sets.keys():
                shortest_paths_sets[src_dest] = RoutingAlgorithm.all_shortest_paths(graph, src_dest[0], src_dest[1])
            randomly_selected_path = random.sample(shortest_paths_sets[src_dest], 1)[0]
            path = copy.deepcopy(randomly_selected_path)
            path = path[:-1]  # remove last element because so that intermeddiate node isn't dupliacted

            # ECMP routing from intermediate node to dest
            src_dest = (randomly_selected_intermediate, server_dest)
            if src_dest not in shortest_paths_sets.keys():
                shortest_paths_sets[src_dest] = RoutingAlgorithm.all_shortest_paths(graph, src_dest[0], src_dest[1])
            randomly_selected_path = random.sample(shortest_paths_sets[src_dest], 1)[0]
            path.extend(copy.deepcopy(randomly_selected_path))
            
            # remove cycles
            if len(path) != len(set(path)):
                for i, vertex in enumerate(path):
                    if vertex in path[i+1:]:
                        front = copy.deepcopy(path[0:i+1])
                        back = copy.deepcopy(path[i+1:])
                        path_start = front
                        path_end = copy.deepcopy(back[back.index(vertex) + 1:])
                        path_start.extend(path_end)
                        path = path_start
                        break           

            return path
        return RoutingAlgorithm.network_route_xml_generator(network, path_finder)
    
def routing_algorithm(algorithm, **kwargs):
    if algorithm == RoutingAlgorithm.ECMP:
        return RoutingAlgorithm.ecmp_xml_routes
    elif algorithm == RoutingAlgorithm.KSP and 'k' in kwargs.keys():
        def algo(network):
            return RoutingAlgorithm.ksp_xml_routes(network, kwargs['k'])
        return algo
    elif algorithm == RoutingAlgorithm.VLB:
        return RoutingAlgorithm.vlb_xml_routes
    else:
        print("ERROR: Unknown Algorithm or kwargs")
        print(algorithm)
        print(kwargs)
    