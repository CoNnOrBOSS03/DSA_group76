from customtkinter import *
from PIL import Image

BLUE = "#6e78ff"
LIGHT_BLUE = "#6C8DFA"
ORANGE = "#F89246"
LIGHT_ORANGE = "#FFB449"

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

        # left side!
        self.left_frame = CTkFrame(master=self)
        self.title_text = CTkTextbox(master=self.left_frame, fg_color="transparent", wrap=WORD, font=(None, 32),
                                     activate_scrollbars=False)
        self.title_text.insert("0.0", "Getting Gators Around Gainesville")
        self.title_text.configure(state="disabled")
        self.group_label = CTkLabel(master=self.left_frame, text="Group 76: Hogtown Wayfinders")
        self.names_label = CTkLabel(master=self.left_frame, text="Connor Verra, Andres Cortes")
        self.description_text = CTkTextbox(master=self.left_frame, fg_color="transparent", wrap=WORD)
        self.description_text.insert("0.0",
                                      "Welcome to Getting Gators Around Gainesville! This application uses Dijkstra's "
                                      "shortest path algorithm to figure out how to get you to where you want to go"
                                      " in the shortest path possible! Select a starting point and destination using "
                                      "the option menus, then hit calculate, and the optimal path will be shown! \n \n"
                                      "After you've calculated your optimal path, you can compare the calculation"
                                      " times of this path between graph representations of an adjacency list versus"
                                      " an adjacency matrix! If you'd like to calculate a new path, simply choose new"
                                      " starting and ending locations and hit the button again!")
        self.description_text.configure(state="disabled")

        # middle frame!

        self.middle_frame = CTkFrame(master=self, fg_color="transparent")
        self.map_label = CTkLabel(master=self.middle_frame, textvariable=self.map_caption)
        self.map_image = CTkImage(light_image=Image.open("DSAp3startimg.png"), dark_image=Image.open("DSAp3startimg.png"), size=(600, 300))
        self.map_image_label = CTkLabel(master=self.middle_frame, image=self.map_image, text="")

        self.middle_grid_frame = CTkFrame(master=self.middle_frame, fg_color="transparent")
        self.start_combobox_label = CTkLabel(master=self.middle_grid_frame, text="Starting Location")
        self.start_combobox = CTkComboBox(master=self.middle_grid_frame, border_color=BLUE, button_color=BLUE, button_hover_color=LIGHT_BLUE)
        self.destination_combobox_label = CTkLabel(master=self.middle_grid_frame, text="Destination")
        self.destination_combobox = CTkComboBox(master=self.middle_grid_frame, border_color=ORANGE, button_color=ORANGE, button_hover_color=LIGHT_ORANGE)

        # right side!

        self.right_frame = CTkFrame(master=self)

        # PLACING WIDGETS

        # left frame

        self.left_frame.place(relx=0, rely=0, relwidth=0.25, relheight=1.00)

        self.title_text.place(relx=0.1, rely=0.035, relwidth=0.8, relheight=0.23)
        self.group_label.place(relx=0.1, rely=0.27, relwidth=0.8, relheight=0.05)
        self.names_label.place(relx=0.1, rely=0.31, relwidth=0.8, relheight=0.05)

        self.description_text.place(relx=0.05, rely=0.4, relwidth=0.9, relheight=0.54)

        # middle frame

        self.map_label.place(relx=0.1, rely=0.03, relwidth=0.8, relheight=0.05)
        self.middle_frame.place(relx=0.25, rely=0, relwidth=0.5, relheight=1.00)
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

        # right frame

        self.right_frame.place(relx=0.75, rely=0, relwidth=0.25, relheight=1.00)

    # methods!

    def calculate_path(self):
        # get values from combo boxes
        # check if either are null, if so display error message
        # if not, pass to backend for path calculation
        pass

main_screen = MainScreen()

main_screen.mainloop()
