import customtkinter as ctk
from random import randint

from frames.home import HomeFrame
from frames.live import LiveFrame
from frames.questions import QuestionsFrame
from frames.participants import ParticipantsFrame
from frames.settings import SettingsFrame

class SidePanel(ctk.CTkFrame):
    panelItems = list()
    activeItemColor = "#2345ac"

    activeB = None
    b_home = None
    b_live = None
    b_questions = None
    b_participants = None
    b_settings = None
    
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        commons = {
            "master": self,
            "anchor":"w",
            "height":40, 
            "corner_radius":0,
            "fg_color":"transparent"
        }
        self.b_home = ctk.CTkButton(text="HOME", width=150,command=self.click_home,**commons)
        self.b_live = ctk.CTkButton(text="LIVE", command=self.click_live,**commons)
        self.b_questions = ctk.CTkButton(text="QUESTIONS", command=self.click_questions,**commons)
        self.b_participants = ctk.CTkButton(text="PARTICIPANTS", command=self.click_participants,**commons)
        self.b_settings = ctk.CTkButton(text="SETTINGS", command=self.click_settings,**commons)

        self.b_home.configure(fg_color=self.activeItemColor)
        self.activeB = self.b_home

    def show(self):
        self.b_home.grid(row=0, column=0, sticky="we", pady=(10,0))
        self.b_live.grid(row=1, column=0, sticky="we")
        self.b_questions.grid(row=2, column=0, sticky="we")
        self.b_participants.grid(row=3, column=0, sticky="we")
        self.b_settings.grid(row=4, column=0, sticky="we")

        self.grid(row=1, column=0, stick='nsw')

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

    def setActiveItem(self,item):
        self.activeB.configure(fg_color="transparent")
        self.activeB = item
        self.activeB.configure(fg_color=self.activeItemColor)


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
        self.grid(row=1, column=1, stick='nswe')

class TopBar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, height=50, **kwargs)

        self.l_title = ctk.CTkLabel(self, text="IT QUIZ APP", font=("monospace", 40))

    def show(self):
        self.l_title.pack(fill="x")
        self.grid(row=0, column=0, stick='we', columnspan=2)

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