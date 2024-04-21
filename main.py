from bridges.data_src_dependent import data_source
from bridges.bridges import Bridges
from math import sqrt
from location_coords import *
import os
import queue as Q


# helper function: returns distance between vertex and given coordinates using pythagorean theorem
def getDistance(vertex, lat, lon):
    return sqrt((vertex.latitude - lat) ** 2 + (vertex.longtitude - lon) ** 2)


# return the vertex the closest to some lat/lon coordinate
# can use this to figure out a defined vertex based on the location the user wants to start from/end at
def getClosest(gr, lat, lon):
    # TODO
    # this makes sense but doesn't work, something wrong with what's passed in as gp
    vertices = gr.vertices
    current_closest_vertex = vertices[0]
    current_shortest_distance = 100  # arbitrary big number

    # find distance from using pythagorean theorem ig right?
    for vertex in vertices:
        distance = getDistance(current_closest_vertex, lat, lon)
        if distance < current_shortest_distance:
            current_closest_vertex = vertex
            current_shortest_distance = distance

    return current_closest_vertex


# styling the source vertex
def style_root(gr, root):
    # TODO
    pass


# shortest path function
def shortestPath(gr, root):
    distance = {}
    parent = {}

    # TODO

    return (distance, parent)


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
    bridges.set_description(
        "Shows residential paths in Gainesville!")

    # TODO: Get Data
    osm_data = data_source.get_osm_data("Gainesville, Florida", "residential")

    gr = osm_data.get_graph()
    gr.force_large_visualization(True)

    # TODO: Uncomment for part 2
    # #find and style the root of the Shortest Path
    # root = getClosest(gr,
    #                      (osm_data.latitude_range[0]+osm_data.latitude_range[1])/2,
    #                      (osm_data.longitude_range[0]+osm_data.longitude_range[1])/2)  # sets origin to center of graph
    # FIXME: getClosest doesn't work, uncomment for error message
    # root = getClosest(gr, TURLINGTON_HALL[0], TURLINGTON_HALL[1])  # sets origin to turlington

    # style_root(gr, root)
    bridges.set_data_structure(gr)
    bridges.visualize()

    # TODO: Uncomment for part 3
    # #run Shortest Path
    # Shouldn't we give an option between Dijkstra's algorithm and another shortest path algorithm so that we can compare the two? - Andres
    # (distance,parent) = shortestPath(gr,root)

    # #style vertices based on distances
    # style_distance(gr, distance)
    # bridges.set_data_structure(gr)
    # bridges.visualize()

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
