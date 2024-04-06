import customtkinter as ctk
from random import randint

from frames.home import HomeFrame
from frames.live import LiveFrame
from frames.questions import QuestionsFrame
from frames.participants import ParticipantsFrame
from frames.settings import SettingsFrame
from PIL import Image
import os

from tktooltip import ToolTip
from CTkToolTip import *
class SidePanel(ctk.CTkFrame):
    panelItems = list()
    activeItemColor = ("#bbb", "#111")

    activeB = None
    b_home = None
    b_live = None
    b_questions = None
    b_participants = None
    b_settings = None
    commons = {
        "anchor": "w",
        "height": 30,
        "width":0,
        "corner_radius": 5,
        "fg_color": "transparent",
        "hover_color": ("gray70", "#333"),
        "border_spacing":10,
        "text_color":("gray10", "gray90"),
    }
    icons = dict()
    images = dict()

    def load_icon(self, name):
        self.images[name] = Image.open(os.path.join("ui","admin", "icons", name))
        return ctk.CTkImage(    
            self.images[name],
            size=(20, 20)
        )

    def button(self, text, cmd,icons:tuple):
        light, dark = icons
        img = ctk.CTkImage(
            light_image=Image.open(os.path.join("ui","admin", "icons", light)),
            dark_image=Image.open(os.path.join("ui","admin", "icons", dark)),
            size=(20,20)
        )
        btn =  ctk.CTkButton(
            self,
            # text="   "+text, 
            text="",
            image=img,
            command=cmd,
            **self.commons
        )
        CTkToolTip(btn, message=text, delay=0.1, corner_radius=5)    
        return btn

    def init_icons(self):
        dir = os.path.join("ui", 'admin', 'icons')
        icons = os.listdir(dir)
        self.icons = dict()
        for icon in icons:
            self.icons[icon] = self.load_icon(icon)

    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        # self.init_icons() # load icon images into memory

        self.b_home = self.button("HOME",self.click_home, ("home_dark.png", "home_light.png"))
        self.b_live = self.button("LIVE",self.click_live, ("live_dark.png", "live_light.png"))
        self.b_questions = self.button("QUESTIONS",self.click_questions, ("database_dark.png", "database_light.png"))
        self.b_participants = self.button("PARTICIPANTS",self.click_participants, ("users_dark.png", "users_light.png"))
        self.b_settings = self.button("SETTINGS",self.click_settings, ("settings_dark.png", "settings_light.png"))

        # self.b_home.configure(fg_color=self.activeItemColor)
        # self.activeB = self.b_home
        self.setActiveItem(self.b_home)

    def show(self):
        commons = {
            "padx":5,
            "pady":2
        }
        self.b_home.grid(row=0, column=0, sticky="we", **commons)
        self.b_live.grid(row=1, column=0, sticky="we", **commons)
        self.b_questions.grid(row=2, column=0, sticky="we", **commons)
        self.b_participants.grid(row=3, column=0, sticky="we", **commons)
        self.b_settings.grid(row=4, column=0, sticky="we", **commons)

        self.grid(row=1, column=0, stick="nsw")

    def click_home(self):
        app.mainPanel.setActiveFrame(app.mainPanel.homeFrame)
        self.setActiveItem(self.b_home)

    def click_live(self):
        app.mainPanel.setActiveFrame(app.mainPanel.liveFrame)
        self.setActiveItem(self.b_live)

    def click_questions(self):
        app.mainPanel.setActiveFrame(app.mainPanel.questionsFrame)
        self.setActiveItem(self.b_questions)

    def click_participants(self):
        app.mainPanel.setActiveFrame(app.mainPanel.participantsFrame)
        self.setActiveItem(self.b_participants)

    def click_settings(self):
        app.mainPanel.setActiveFrame(app.mainPanel.settingsFrame)
        self.setActiveItem(self.b_settings)

    def setActiveItem(self, item):
        if self.activeB is not None:
            self.activeB.configure(fg_color="transparent")
            self.activeB.configure(hover_color=self.commons["hover_color"])
        self.activeB = item
        self.activeB.configure(fg_color=self.activeItemColor)
        self.activeB.configure(hover_color=self.activeItemColor)


class MainPanel(ctk.CTkFrame):
    homeFrame = None
    liveFrame = None
    questionsFrame = None
    participantsFrame = None
    settingsFrame = None

    def setActiveFrame(self, frame):
        app.mainPanel.activeFrame.grid_forget()
        app.mainPanel.activeFrame = frame
        app.mainPanel.activeFrame.show()

    def __init__(self, master, **kwargs):
        super().__init__(master=master, fg_color="green", **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.homeFrame = HomeFrame(self)
        self.liveFrame = LiveFrame(self)
        self.questionsFrame = QuestionsFrame(self)
        self.participantsFrame = ParticipantsFrame(self)
        self.settingsFrame = SettingsFrame(self)

        self.activeFrame = self.homeFrame

    def show(self):
        self.activeFrame.show()
        self.grid(row=1, column=1, stick="nswe")


class TopBar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, height=50, **kwargs)

        self.l_title = ctk.CTkLabel(self, text="IT QUIZ APP", font=("monospace", 40))

    def show(self):
        self.l_title.pack(fill="x")
        self.grid(row=0, column=0, stick="we", columnspan=2)


class App(ctk.CTk):
    HEIGHT = 400
    WIDTH = 800
    side_panel_width = 300

    def __init__(self):
        super().__init__()
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.topBar = TopBar(self)
        self.sidePanel = SidePanel(self, width=self.side_panel_width)
        self.mainPanel = MainPanel(self)

    def show(self):
        self.topBar.show()
        self.sidePanel.show()
        self.mainPanel.show()
        self.mainloop()


app = None
if __name__ == "__main__":
    app = App()
    app.show()
