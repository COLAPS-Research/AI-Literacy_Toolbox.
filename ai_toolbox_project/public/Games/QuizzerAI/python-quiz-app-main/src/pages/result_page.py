""" Here is the page, which will show the results after the quiz """

import os
import tkinter as tk
from tkinter import ttk
from src.settings import SETTINGS
from PIL import Image, ImageTk


class ResultPage(tk.Frame):
    """Shows the final result page."""

    def __init__(self, parent, controller):
        """Initialize the result-page."""
        super().__init__(parent)
        self.controller = controller

        self.style = ttk.Style()
        self.style.theme_use(SETTINGS.get("general").get("theme"))

        bg_image = Image.open(
            os.path.join(
                os.getcwd(), SETTINGS.get("images_and_icons").get("background_image")
            )
        )

        resize_values = tuple(
            map(int, SETTINGS.get("general").get("image_size").split("x"))
        )
        bg_image = bg_image.resize(resize_values)

        self.bg_photo = ImageTk.PhotoImage(bg_image)

        self.canvas = tk.Canvas(self, width=bg_image.width, height=bg_image.height)
        self.canvas.place(
            x=0,
            y=0,
        )
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
        self.style.configure(
            "HoverNext.TButton",
            background="red",
            foreground="dark green",
            relief="raised",
            font=(SETTINGS.get("font").get("primary"), 12),
        )

        self.style.configure(
            "NextButton.TButton",
            font=(
                SETTINGS.get("font").get("primary"),
                12,
            ),  # Replace with your font name and size
        )

    def display_result_page(self):
        """Display the result page."""
        # Titel/Überschrift/Hinweis:
        self.label = ttk.Label(
            self,
            text=f"{SETTINGS.get("translations").get("results_en")}",
            font=(f"{SETTINGS.get("font").get("primary")}", 16),
            wraplength=600,
        )
        self.label.pack(pady=20)

        # Label zum Anzeigen der Ergebnisse:
        self.result_label = ttk.Label(
            self,
            text=f"{self.controller.score.get_score()}",
            font=(SETTINGS.get("font").get("primary"), 16),
            wraplength=600,
        )
        self.result_label.pack(pady=20)

        # Button zurück zur Startseite:
        self.restart_button = ttk.Button(
            self, text=f"{SETTINGS.get("translations").get("restart_en")}", command=self.restart_quiz,
            style="NextButton.TButton"
        )
        self.restart_button.bind(
            "<Enter>", lambda e: self.restart_button.configure(style="HoverNext.TButton")
        )
        self.restart_button.bind(
            "<Leave>", lambda e: self.restart_button.configure(style="NextButton.TButton")
        )
        self.restart_button.pack(pady=20)

    def restart_quiz(self):
        """Restart the quiz."""
        # Quiz-Daten zurücksetzen & zurück zur StartPage:
        self.controller.frames["StartPage"].get_available_topics()
        self.controller.show_frame("StartPage")
        self.clear_buttons()
        self.controller.frames["StartPage"].display_start_page()

    def clear_buttons(self):
        """Clear all labels and buttons"""
        self.label.destroy()
        self.result_label.destroy()
        self.restart_button.destroy()
