from bridges.data_src_dependent import data_source
from bridges.bridges import Bridges
from math import sqrt
from location_coords import *
from heapq import *
import time

# helper function: returns distance between vertex and given coordinates using pythagorean theorem
def getDistance(vertex, lat, lon):
    return sqrt((vertex.latitude - lat) ** 2 + (vertex.longitude - lon) ** 2)


# return the key to the closest vertex to a given point
# can use this to figure out a defined vertex based on the location the user wants to start from/end at
def getClosest(gr, lat, lon):
    vertices = gr.vertices
    current_closest_vertex = vertices[0]
    current_shortest_distance = 100  # arbitrary big number

    # find distance from using pythagorean theorem ig right?
    for vertex in vertices:
        distance = getDistance(gr.get_vertex_data(vertex), lat, lon)
        if distance < current_shortest_distance:
            current_closest_vertex = vertex
            current_shortest_distance = distance

    return current_closest_vertex


# styling the source vertex
def style_root(gr, root):
    gr.get_vertex(root).color = "crimson"
    gr.get_vertex(root).opacity = 1.0

# shortest path function
def shortestPathArray(gr, root, destination):

    vertices = gr.vertices
    start_time = time.time()

    # need to initialize the arrays and sets
    # set S: initially empty
    # need to save distances somehow with the vertices to process
    computed_vertices = set()
    # set V-S: need to place all vertices into it
    vertices_to_process = set()
    for vertex in vertices:
        vertices_to_process.add(vertex)
    # d[v]: need to set all to infinity besides source, which will be set to 0
    distances = [1e6] * len(vertices)
    not_computed_distances = [1e6] * len(vertices)
    distances[root] = 0
    not_computed_distances[root] = 0
    # p[v]: need to set all to -1
    predecessors = [-1] * len(vertices)

    # time for the actual algorithm

    while destination not in computed_vertices:

        # first, start w/ vertex w/ minimum distance in d[v], THAT HASN'T BEEN COMPUTED, and add to set S
        # index should directly correlate with vertex id so should work?

        minVertexID = not_computed_distances.index(min(not_computed_distances))
        # make the distance at that index arbitrary large so we don't reselect it
        not_computed_distances[minVertexID] = 1e6

        # need to move vertex from not computed set to computed set
        vertices_to_process.remove(minVertexID)
        computed_vertices.add(minVertexID)

        # print(computed_vertices)

        # now, need to process edges adjacent to the first vertex, and update distances based on relaxation!

        # gets outgoing edges
        for edge in gr.out_going_edge_set_of(minVertexID):
            # relaxation!
            if distances[edge.tov] > distances[edge.fromv] + edge._edge_data:
                distances[edge.tov] = distances[edge.fromv] + edge._edge_data
                not_computed_distances[edge.tov] = distances[edge.fromv] + edge._edge_data
                predecessors[edge.tov] = edge.fromv
                #print(f"Predecessor: {predecessors[edge.tov]}")
               # print(f"Distance: {distances[edge.tov]}")

    #print(f"Distance of chosen path is {distances[destination]}")
    return distances[destination], round((round(time.time() - start_time, 10)) * 10e3, 3)

def ShortestPathHeap(gr, root, destination):

    vertices = gr.vertices
    start_time = time.time()

    # need to initialize the arrays and sets
    # set S: initially empty
    # need to save distances somehow with the vertices to process
    computed_vertices = set()
    # set V-S: need to place all vertices into it
    vertices_to_process = set()
    for vertex in vertices:
        vertices_to_process.add(vertex)
    # d[v]: need to set all to infinity besides source, which will be set to 0
    distances = [1e6] * len(vertices)
    not_computed_distances = [(vertex, 1e6) for vertex in vertices]
    not_computed_distances[root] = (root, 0)
    not_computed_distances_heap = [(item[1], item) for item in not_computed_distances]
    heapify(not_computed_distances_heap)
    distances[root] = 0
    # p[v]: need to set all to -1
    predecessors = [-1] * len(vertices)

    # time for the actual algorithm

    while destination not in computed_vertices:

        # first, start w/ vertex w/ minimum distance in d[v], THAT HASN'T BEEN COMPUTED, and add to set S
        # index should directly correlate with vertex id so should work?

        minVertexID = heappop(not_computed_distances_heap)[1][0]
        #print(minVertexID)
        # make the distance at that index arbitrary large so we don't reselect it
        not_computed_distances[minVertexID] = 1e6

        # need to move vertex from not computed set to computed set
        computed_vertices.add(minVertexID)

        # print(computed_vertices)

        # now, need to process edges adjacent to the first vertex, and update distances based on relaxation!

        # gets outgoing edges
        for edge in gr.out_going_edge_set_of(minVertexID):
            # relaxation!
            if distances[edge.tov] > distances[edge.fromv] + edge._edge_data:
                distances[edge.tov] = distances[edge.fromv] + edge._edge_data
                not_computed_distances[edge.tov] = distances[edge.fromv] + edge._edge_data
                predecessors[edge.tov] = edge.fromv

    return round((round(time.time() - start_time, 10)) * 10e3, 3)

# style the graph based on distance

