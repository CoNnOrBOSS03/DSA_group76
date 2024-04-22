from bridges.data_src_dependent import data_source
from bridges.bridges import Bridges
from math import sqrt
from location_coords import *
import os
import queue as Q

gainesville_bounding_box = [29.69267, -82.38941, 29.65922, -82.32507]

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
def shortestPathArray(gr, root):

    vertices = gr.vertices

    # need to initialize the arrays and sets
    # set S: initially empty

    # FIXME: doesnt work because the same distance, being of the root, is always found
    # need to save distances somehow with the vertices to process

    computed_vertices = set()
    # set V-S: need to place all vertices into it
    vertices_to_process = set()
    for vertex in vertices:
        vertices_to_process.add(vertex)
    # d[v]: need to set all to infinity besides source, which will be set to 0
    distances = [1e6] * len(vertices)
    distances[root] = 0
    # p[v]: need to set all to -1
    predecessors = [-1] * len(vertices)

    # time for the actual algorithm

    while min(distances) != 1e6:

        # first, start w/ vertex w/ minimum distance in d[v], THAT HASN'T BEEN COMPUTED, and add to set S
        # index should directly correlate with vertex id so should work?

        minVertexID = distances.index(min(distances))

        # test to see if this is correct
        # print(minVertexID)
        # print(root)
        # print(f"[{gr.get_vertex_data(root).latitude}, {gr.get_vertex_data(root).longitude}]")
        # print(f"[{gr.get_vertex_data(minVertexID).latitude}, {gr.get_vertex_data(minVertexID).longitude}]")

        # need to move vertex from not computed set to computed set
        # FIXME: removing vertex fucks up the indexing?
        vertices_to_process.remove(minVertexID)
        computed_vertices.add(minVertexID)

        #print(computed_vertices)

        # now, need to process edges adjacent to the first vertex, and update distances based on relaxation!

        # testing getting adjacent edges
        # for edge in gr.out_going_edge_set_of(minVertexID):
        #     print(f"{edge.fromv} ---> {edge.tov}, weight = {edge._edge_data}")
        #     gr.get_vertex(edge.tov).color = "orange"

        # gets outgoing edges
        for edge in gr.out_going_edge_set_of(minVertexID):
            # relaxation!
            if distances[edge.tov] > distances[edge.fromv] + edge._edge_data:
                distances[edge.tov] = distances[edge.fromv] + edge._edge_data
                predecessors[edge.tov] = edge.fromv
                print(f"Predecessor: {predecessors[edge.tov]}")
                print(f"Distance: {distances[edge.tov]}")


    # TODO

    #return (distance, parent)


# style the graph based on distance
def style_distance(gr, distance):
    # TODO
    # find the maximum distance which is not infinity

    # style the color of vertices with a linear scale
    pass


# style the path between the root and the destination (root is not given because all parent path goes to root)
def style_parent(gr, parent, dest):
    # TODO

    # style all vertices to almost invisible

    # style all edges to almost invisible

    # Style the path between parent and dest in black
    ##style node

    ##style edge along the path
    pass


def main():

    # get data
    bridges = Bridges(209, "CoNnOrBOSS03", "996702144742")
    bridges.set_title("Graph : Gainesville Map Graph Test")
    bridges.set_description("Shows residential paths in Gainesville!")

    osm_data = data_source.get_osm_data("Gainesville, Florida", "residential")
    # alternatively, use bounding box for more specified region
    #osm_data = data_source.get_osm_data(gainesville_bounding_box[0], gainesville_bounding_box[1],
                                        #gainesville_bounding_box[2], gainesville_bounding_box[3], "residential")

    gr = osm_data.get_graph()
    gr.force_large_visualization(True)

    # #find and style the root of the Shortest Path
    root = getClosest(gr, LocationDictionary["Turlington Hall"][0], LocationDictionary["Turlington Hall"][1])  # sets origin to turlington
    # print(root)
    # vertex = gr.get_vertex_data(root)
    # print(f"[{vertex.latitude}, {vertex.longitude}]")

    for key in gr.vertices:
        gr.get_vertex(key).opacity = 0.5

    style_root(gr, root)


    # TODO: Uncomment for part 3
    # #run Shortest Path
    # Shouldn't we give an option between Dijkstra's algorithm and another shortest path algorithm so that we can compare the two? - Andres
    # (distance,parent) =
    shortestPathArray(gr, root)

    # #style vertices based on distances
    # style_distance(gr, distance)
    bridges.set_data_structure(gr)
    bridges.visualize()

    # TODO Uncomment for part 4
    # #find a destination
    # dest = getClosest(gr,
    #                   (osm_data.latitude_range[0]+(osm_data.latitude_range[1]-osm_data.latitude_range[0])/4),
    #                   (osm_data.longitude_range[0]+(osm_data.longitude_range[1]-osm_data.longitude_range[0])/4))

    # #style the path from root to destination
    # style_parent(gr,parent, dest)

    # bridges.set_data_structure(gr)
    # bridges.visualize()


if __name__ == "__main__":
    main()
