"""Start page of the application."""

import os
import tkinter as tk
from tkinter import ttk

from src.settings import SETTINGS
from src.loggers_home.decorators import info_logger
from src.data.topic_data import topic_data
from PIL import Image, ImageTk


class StartPage(tk.Frame):
    """Start page of the application. Allows users to choose a topic."""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.photo_images = []

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

        # Set theme and styles
        self.style = ttk.Style()
        self.style.theme_use(SETTINGS.get("general").get("theme"))
        self.style.configure(
            "TopicButton.TButton", background="white", foreground="black", relief="flat"
        )
        self.style.configure(
            "Hover.TButton", background="red", foreground="dark green", relief="raised"
        )

        # Grid configuration
        self.grid_rowconfigure((0, 1, 2, 3), weight=0)
        self.grid_columnconfigure(0, weight=1)

    def display_start_page(self):
        """Display the start page with topic buttons."""

        self.controller.score.reset_score()
        ttk.Label(
            self,
            text=SETTINGS.get("translations").get("choose_en"),
            style="WB.TLabel",
            font=(f"{SETTINGS.get("font").get("primary")}", 20),
        ).grid(row=0, column=0, pady=10)

        # Determine button dimensions
        button_width = self.winfo_screenwidth() // 4 // 8

        for idx, topic in enumerate(self.get_available_topics()):
            button = self.create_topic_button(topic, button_width)
            button.grid(row=idx + 1, column=0, pady=5, sticky="n")

    def create_topic_button(self, topic, button_width):
        """Create a button for a specific topic with an optional image."""
        image_path = os.path.join(os.getcwd(), "images", f"{topic.lower()}.png")
        image = self.load_image(image_path) if os.path.exists(image_path) else None

        button = ttk.Button(
            self,
            text=topic,
            image=image,
            compound="left" if image else None,
            command=lambda t=topic: self.select_topic(t),
            style="TopicButton.TButton",
            width=button_width,
        )
        self.add_hover_effect(button)
        return button

    def load_image(self, path):
        """Load and resize an image for a button."""
        photo = tk.PhotoImage(file=path).subsample(24, 24)
        self.photo_images.append(photo)  # Prevent garbage collection
        return photo

    def add_hover_effect(self, button):
        """Add hover effects to a button."""
        button.bind("<Enter>", lambda e: button.configure(style="Hover.TButton"))
        button.bind("<Leave>", lambda e: button.configure(style="TopicButton.TButton"))

    @info_logger
    def select_topic(self, topic):
        """Handle topic selection and navigate to the learning material page."""
        self.controller.selected_topic = topic
        learning_page = self.controller.frames["LearningMaterialPage"]
        learning_page.load_material(topic)
        self.controller.show_frame("LearningMaterialPage")

    @staticmethod
    def get_available_topics():
        """Return the list of available topics."""
        return topic_data
