from customtkinter import *
from PIL import Image
from location_coords import LOCATION_NAMES
from main_functions import *

BLUE = "#6e78ff"
LIGHT_BLUE = "#6C8DFA"
ORANGE = "#F89246"
LIGHT_ORANGE = "#FFB449"
GREEN = "#447241"
LIGHT_GREEN = "#60a05b"
GRAY = "#262626"
LIGHT_GRAY = "#333333"


class MainScreen(CTk):
    def __init__(self):
        super().__init__()

        set_appearance_mode("dark")
        set_default_color_theme("dark-blue")

        self.geometry("1080x600")
        self.minsize(1080, 600)
        self.maxsize(1080, 600)
        self.title("COP3530 Project 3, Group 76, Spring 2024")

        # CTk variables for interactive text and menus

        self.map_caption = StringVar(value="Map of Gainesville using Bridges Open Street Map Data")
        self.sorted_array_results_text = StringVar(value="")
        self.fibonacci_results_text = StringVar(value="")
        self.distance_results_text = StringVar(value="")

        # left side!
        self.left_frame = CTkFrame(master=self, fg_color=GRAY, bg_color=GRAY)
        self.title_text = CTkTextbox(master=self.left_frame, fg_color="transparent", wrap=WORD, font=(None, 32),
                                     activate_scrollbars=False)
        self.title_text.insert("0.0", "Getting Gators Around Gainesville")
        self.title_text.configure(state="disabled")
        self.group_label = CTkLabel(master=self.left_frame, text="Group 76: Hogtown Wayfinders")
        self.names_label = CTkLabel(master=self.left_frame, text="Connor Verra")
        self.description_text = CTkTextbox(master=self.left_frame, fg_color="transparent", wrap=WORD)
        self.description_text.insert("0.0",
                                     "Welcome to Getting Gators Around Gainesville! This application uses Dijkstra's "
                                     "shortest path algorithm to figure out how long the shortest path is from your "
                                     "starting location to your destination! Select a starting point and destination using "
                                     "the option menus, then hit calculate, and distance of the optimal path will be shown! \n \n"
                                     "After you've calculated your optimal path, you can compare the calculation"
                                     " times of this path between using an array versus "
                                     "a heap! If you'd like to calculate a new path, simply choose new"
                                     " starting and ending locations and hit the button again!")
        self.description_text.configure(state="disabled")

        # middle frame!

        self.middle_frame = CTkFrame(master=self, fg_color=LIGHT_GRAY, bg_color=LIGHT_GRAY)
        self.map_label = CTkLabel(master=self.middle_frame, textvariable=self.map_caption)
        self.map_image = CTkImage(light_image=Image.open("DSAp3startimg.png"),
                                  dark_image=Image.open("DSAp3startimg.png"), size=(600, 300))
        self.map_image_label = CTkLabel(master=self.middle_frame, image=self.map_image, text="")

        self.middle_grid_frame = CTkFrame(master=self.middle_frame, fg_color="transparent")
        self.start_combobox_label = CTkLabel(master=self.middle_grid_frame, text="Starting Location")
        self.start_combobox = CTkComboBox(master=self.middle_grid_frame, values=LOCATION_NAMES,
                                          border_color=BLUE, button_color=BLUE, button_hover_color=LIGHT_BLUE)
        self.destination_combobox_label = CTkLabel(master=self.middle_grid_frame, text="Destination")
        self.destination_combobox = CTkComboBox(master=self.middle_grid_frame, values=LOCATION_NAMES,
                                                border_color=ORANGE, button_color=ORANGE,
                                                button_hover_color=LIGHT_ORANGE)
        self.calculate_button = CTkButton(master=self.middle_frame,
                                          command=lambda: self.calculate_path(self.start_combobox.get(),
                                                                              self.destination_combobox.get()),
                                          text="Calculate Path", fg_color=GREEN, hover_color=LIGHT_GREEN)

        # right side!

        self.right_frame = CTkFrame(master=self, fg_color=GRAY, bg_color=GRAY)
        self.results_label = CTkLabel(master=self.right_frame, text="Results", font=(None, 25))
        self.results_text = CTkTextbox(master=self.right_frame, fg_color="transparent", wrap=WORD)
        self.results_text.insert("0.0", "Below are the times it took to calculate the "
                                        "optimal path using the two graph representations, as well as the "
                                        "calculated distance.")
        self.results_text.configure(state="disabled")
        self.sorted_array_label = CTkLabel(master=self.right_frame, text="Array Calculation Time:")
        self.sorted_array_results_label = CTkLabel(master=self.right_frame,
                                                     textvariable=self.sorted_array_results_text)
        self.fibonacci_label = CTkLabel(master=self.right_frame,
                                               text="Heap Calculation Time:")
        self.fibonacci_results_label = CTkLabel(master=self.right_frame,
                                                       textvariable=self.fibonacci_results_text)
        # self.results_additional_text = CTkTextbox(master=self.right_frame, fg_color="transparent", wrap=WORD)
        # self.results_additional_text.insert("0.0", "Some text to explain the results and time complexities "
        #                                            "of our chosen data structures, blah blah blah filling space to show"
        #                                            " how this will end up looking like.")
        # self.results_additional_text.configure(state="disabled")
        self.distance_label = CTkLabel(master=self.right_frame,
                                        text="Calculated Distance:")
        self.distance_results_label = CTkLabel(master=self.right_frame,
                                                textvariable=self.distance_results_text)

        # PLACING WIDGETS

        # left frame

        self.left_frame.place(relx=0, rely=0, relwidth=0.25, relheight=1.00)

        self.title_text.place(relx=0.1, rely=0.035, relwidth=0.8, relheight=0.23)
        self.group_label.place(relx=0.1, rely=0.27, relwidth=0.8, relheight=0.05)
        self.names_label.place(relx=0.1, rely=0.31, relwidth=0.8, relheight=0.05)

        self.description_text.place(relx=0.05, rely=0.4, relwidth=0.9, relheight=0.54)

        # middle frame

        self.middle_frame.place(relx=0.25, rely=0, relwidth=0.5, relheight=1.00)
        self.map_label.place(relx=0.1, rely=0.03, relwidth=0.8, relheight=0.05)
        self.map_image_label.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.5)

        self.middle_grid_frame.place(relx=0.1, rely=0.65, relwidth=0.8, relheight=0.15)
        self.middle_grid_frame.columnconfigure(0, weight=1)
        self.middle_grid_frame.columnconfigure(1, weight=1)
        self.middle_grid_frame.rowconfigure(0, weight=1)
        self.middle_grid_frame.rowconfigure(1, weight=1)
        self.start_combobox_label.grid(row=0, column=0)
        self.start_combobox.grid(row=1, column=0)
        self.destination_combobox_label.grid(row=0, column=1)
        self.destination_combobox.grid(row=1, column=1)
        self.calculate_button.pack(side="bottom", pady=50)

        # right frame

        self.right_frame.place(relx=0.75, rely=0, relwidth=0.25, relheight=1.00)
        self.results_label.pack(pady=30, side="top")
        self.results_text.place(relx=0.10, rely=0.20)
        self.sorted_array_label.place(relx=0.20, rely=0.40)
        self.sorted_array_results_label.place(relx=0.30, rely=0.45)
        self.fibonacci_label.place(relx=0.20, rely=0.55)
        self.fibonacci_results_label.place(relx=0.30, rely=0.60)
        # self.results_additional_text.place(relx=0.10, rely=0.7)
        self.distance_label.place(relx=0.20, rely=0.70)
        self.distance_results_label.place(relx=0.30, rely=0.75)

    # methods!

    def calculate_path(self, start, destination):
        # get values from combo boxes
        # check if either are null, if so display error message
        # if not, pass to backend for path calculation
        bridges = Bridges(209, "CoNnOrBOSS03", "996702144742")
        bridges.set_title("Graph : Gainesville Map Graph Test")
        bridges.set_description("Shows residential paths in Gainesville!")

        osm_data = data_source.get_osm_data("Gainesville, Florida", "residential")

        gr = osm_data.get_graph()
        gr.force_large_visualization(True)

        root = getClosest(gr, LocationDictionary[start][0], LocationDictionary[start][1])
        destination = getClosest(gr, LocationDictionary[destination][0], LocationDictionary[destination][1])

        for key in gr.vertices:
            gr.get_vertex(key).opacity = 0.5

        gr.get_vertex(root).color = "blue"
        gr.get_vertex(root).color = "orange"

        distance, time1 = shortestPathArray(gr, root, destination)
        self.distance_results_text.set(f"{str(round((distance / 1609), 2))} miles")
        self.sorted_array_results_text.set(f"{str(time1)} ms")

        time2 = ShortestPathHeap(gr, root, destination)

        self.fibonacci_results_text.set(f"{str(time2)} ms")


