import os
import logging
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.font import Font

from src.settings import SETTINGS
from src.loggers_home.decorators import info_logger
from src.data.learning_material_data import learning_material


class LearningMaterialPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.material_index = 0
        self.topic_spec_learning_mat = []
        self.style = ttk.Style()
        self.style.theme_use(SETTINGS.get("general").get("theme"))

        # Hintergrundbild:
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

        # Configure button styles
        self.style.configure(
            "TopicButton.TButton",
            background="white",
            foreground="black",
            relief="flat",
            font=(SETTINGS.get("font").get("primary"), 12),
        )
        self.style.configure(
            "Hover.TButton",
            background="red",
            foreground="dark green",
            relief="raised",
            font=(SETTINGS.get("font").get("primary"), 12),
        )
        self.style.configure(
            "HoverNext.TButton",
            background="red",
            foreground="dark green",
            relief="raised",
            font=(SETTINGS.get("font").get("primary"), 12),
        )
        self.style.configure(
            "Hover.TButton", background="red", foreground="dark green", relief="raised"
        )

        self.text = tk.Text(
            self,
            wrap=tk.WORD,
            font=("Comic Sans MS", 14),
            fg="darkblue",
            relief="raised",
            background="#e4f3ff",
        )
        self.text.pack(pady=40, padx=80)
        self.text.configure(highlightthickness=0, borderwidth=0)

        self.next_button = ttk.Button(
            self,
            text=f"{SETTINGS.get("translations").get("next_en")}",
            command=self.go_to_quiz,
            style="NextButton.TButton",
        )
        self.next_button.bind(
            "<Enter>", lambda e: self.next_button.configure(style="HoverNext.TButton")
        )
        self.next_button.bind(
            "<Leave>", lambda e: self.next_button.configure(style="NextButton.TButton")
        )
        self.next_button.pack(pady=10)

        self.photo = None

    def load_material(self, topic):
        """Load and display learning materials for the selected topic."""
        self.material_index = 0
        self.topic_spec_learning_mat = self.get_learning_material(topic)
        self.display_material()

    @info_logger
    def display_material(self) -> bool:
        """Display the current learning material or transition to the result page if complete."""
        if self.material_index < len(self.topic_spec_learning_mat):
            self.text.config(state="normal")
            content = self.topic_spec_learning_mat[self.material_index].get("content")
            self.text.delete("1.0", tk.END)  # Clear previous content
            self.text.insert(tk.END, content)
            self.adjust_text_size(content)  # Adjust text widget size
            self.text.config(state="disabled")
            score_label = ttk.Label(
                self,
                text=f"Score: {self.controller.score.get_score()}",
                font=(SETTINGS.get("font").get("primary"), 14),
                background="purple",
                foreground="white",
                padding=(10, 5),
            )
            score_label.place(relx=1.0, rely=0.0, anchor="ne")
            return False
        else:
            self.controller.show_frame("ResultPage")
            self.reset_learning_page()
            self.controller.frames["ResultPage"].display_result_page()
            return True

    def adjust_text_size(self, content):
        """Adjust the size of the text widget based on the content."""
        font = Font(font=self.text["font"])
        char_width = font.measure("0")
        char_height = font.metrics("linespace")

        text_widget_width = self.text.winfo_width() or 400
        max_chars_per_line = text_widget_width // char_width

        wrapped_lines = 0
        for line in content.split("\n"):
            wrapped_lines += max(
                1,
                (len(line) // max_chars_per_line)
                + (1 if len(line) % max_chars_per_line > 0 else 0),
            )

        total_lines = max(wrapped_lines, 5)
        total_width = max(len(max(content.split("\n"), key=len, default="")), 40)

        self.text.config(width=total_width, height=total_lines)

    @info_logger
    def go_to_quiz(self):
        """Navigate to the quiz page with the current material's questions."""
        if self.material_index < len(self.topic_spec_learning_mat):
            material = self.topic_spec_learning_mat[self.material_index]
            self.controller.frames["QuizPage"].load_questions(
                self.controller.selected_topic, material.get("question_ids")
            )
            self.controller.show_frame("QuizPage")
            self.material_index += 1
        else:
            self.reset_learning_page()
            self.controller.show_frame("ResultPage")
            self.controller.frames["ResultPage"].display_result_page()

    @staticmethod
    def get_learning_material(topic):
        """Retrieve learning materials for the specified topic."""
        return [
            material for material in learning_material if material.get("topic") == topic
        ]

    def reset_learning_page(self):
        """Reset the learning page to its default state."""
        self.photo = None
        self.material_index = 0

    def set_next_button_image(self, image_path):
        """Set an image for the next button if the path is valid."""
        if os.path.exists(image_path):
            original_image = Image.open(image_path)
            rotated_image = original_image.rotate(180, expand=True).resize((24, 24))
            self.photo = ImageTk.PhotoImage(rotated_image)
            self.next_button.config(image=self.photo, compound="right")
        else:
            logging.error(f"Image not found: {image_path}")
