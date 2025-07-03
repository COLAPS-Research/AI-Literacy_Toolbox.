"""Handles the flow of views."""

import tkinter as tk

from src.settings import SETTINGS
from src.pages.quiz_page import QuizPage
from src.pages.result_page import ResultPage
from src.score import Score
from src.pages.start_page import StartPage
from src.loggers_home.decorators import info_logger
from src.pages.learning_material_page import LearningMaterialPage


class MainApplication(tk.Tk):
    """
    Main Application welche das Main-Window von tk.Tk erbt. Initialisiert also die UI der App
    """

    def __init__(self):
        """
        Initialisiert den Rahmen der Anwendung(Titel, Größe).
        """
        super().__init__()
        self.title(SETTINGS.get("general").get("title"))
        self.geometry(SETTINGS.get("general").get("image_size"))
        self.frames = {}
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.score = Score()
        self.resizable(False, False)

        # Initialize all pages
        for F in (StartPage, LearningMaterialPage, QuizPage, ResultPage):
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.selected_topic = None
        self.show_frame("StartPage")
        self.frames["StartPage"].display_start_page()

    @info_logger
    def show_frame(self, page_name) -> str:
        """
        Show a frame for the given page name.
        Dadurch wird die Seite angezeigt
        """
        frame = self.frames[page_name]
        frame.tkraise()
        return f"Showing frame {page_name}"
