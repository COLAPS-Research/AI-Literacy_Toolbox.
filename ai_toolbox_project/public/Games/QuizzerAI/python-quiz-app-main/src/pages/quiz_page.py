import os
import tkinter as tk
from idlelib.configdialog import font_sample_text
from tkinter import ttk

from src.settings import SETTINGS
from src.utils.utils import get_question_data
from src.loggers_home.decorators import timer_logger, info_logger
from PIL import Image, ImageTk


class QuizPage(tk.Frame):
    """Implements the logic and visuals seen on the quiz page."""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.init_widgets()

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
        self.canvas.place(x=0, y=0)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Move the canvas to the background
        self.canvas.tag_lower("all")

        self.init_widgets()

    def init_widgets(self):
        """Initialize and configure widgets for the quiz page."""
        self.style = ttk.Style()
        self.style.theme_use(SETTINGS.get("general").get("theme"))
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
            "NextButton.TButton",
            font=(
                SETTINGS.get("font").get("primary"),
                12,
            ),  # Replace with your font name and size
        )

        self.grid_rowconfigure(0, weight=0)
        self.grid_columnconfigure(0, weight=1)

        self.question_label = ttk.Label(
            self,
            text="",
            font=(SETTINGS.get("font").get("primary"), 16),
            wraplength=600,
        )
        self.question_label.grid(row=0, column=0, pady=10)

        self.answer_buttons_frame = tk.Frame(self)
        self.answer_buttons_frame.grid(row=1, column=0, pady=5, sticky="n")

    def reset_quiz(self):
        """Reset quiz attributes and clear widgets."""
        self.questions_all = []
        self.questions_loaded = []
        self.question_index = 0
        self.clear_widgets()

    def clear_widgets(self):
        """Remove all widgets from the answer buttons frame."""
        for widget in self.answer_buttons_frame.winfo_children():
            widget.destroy()

    @timer_logger
    def load_questions(self, topic, questions_to_load):
        """Load questions for the given topic and indices."""
        self.reset_quiz()
        self.questions_all = get_question_data().get(topic, [])
        self.questions_loaded = [
            q for q in self.questions_all if q.get("id") in questions_to_load
        ]
        self.display_question()

    @timer_logger
    def display_question(self):
        """Display the current question and its options."""
        self.clear_widgets()

        if self.question_index < len(self.questions_loaded):
            score_label = ttk.Label(
                self,
                text=f"Score: {self.controller.score.get_score()}",
                font=(SETTINGS.get("font").get("primary"), 14),
                background="purple",
                foreground="white",
                padding=(10, 5),
            )
            score_label.place(relx=1.0, rely=0.0, anchor="ne")
            current_q = self.questions_loaded[self.question_index]
            self.question_label.config(text=current_q["question_text"])

            for i, option in enumerate(current_q["options"]):
                button = ttk.Button(
                    self.answer_buttons_frame,
                    text=option.get("answer_text"),
                    command=lambda i=i: self.check_answer(i, current_q["options"]),
                    style="TopicButton.TButton",
                )
                button.grid(row=i, column=0, pady=5, sticky="ew")
                button.bind(
                    "<Enter>", lambda e, b=button: b.configure(style="Hover.TButton")
                )
                button.bind(
                    "<Leave>",
                    lambda e, b=button: b.configure(style="TopicButton.TButton"),
                )
        else:
            self.transition_to_next_material()

    @info_logger
    def check_answer(self, selected_option, explanations):
        """Check if the selected answer is correct and provide feedback."""
        current_q = self.questions_loaded[self.question_index]
        is_correct = selected_option == current_q["answer"]
        self.controller.score.increase_score() if is_correct else None

        self.show_feedback(is_correct, explanations[selected_option]["explanation"])

    def show_feedback(self, is_correct, explanation):
        """Display feedback popup for the current question."""
        # Destroy the previous popup if it exists
        if hasattr(self, "feedback_popup") and self.feedback_popup.winfo_exists():
            self.feedback_popup.destroy()

        # Create a new feedback popup
        self.feedback_popup = tk.Toplevel(self)
        self.feedback_popup.title("Feedback")

        # Get the position of the parent window and center the popup
        x = self.winfo_rootx() + 100
        y = self.winfo_rooty() + 100
        self.feedback_popup.geometry(f"400x300+{x}+{y}")

        self.feedback_popup.configure(background="#e4f3ff")

        feedback_text = (
            SETTINGS.get("translations").get("correct_en") + "!"
            if is_correct
            else SETTINGS.get("translations").get("incorrect_en") + "!"
        )
        ttk.Label(
            self.feedback_popup,
            text=feedback_text,
            font=(SETTINGS.get("font").get("primary"), 14),
            foreground="darkblue",
            background="#e4f3ff",
        ).pack(pady=10)

        ttk.Label(
            self.feedback_popup,
            text=explanation,
            font=(SETTINGS.get("font").get("primary"), 12),
            wraplength=280,
            foreground="darkblue",
            background="#e4f3ff",
        ).pack(pady=10)

        # Next button
        next_button = ttk.Button(
            self.feedback_popup,
            text=f"{SETTINGS.get("translations").get("next_en")}",
            command=lambda: self.next_question(self.feedback_popup),
            style="NextButton.TButton",
        )
        next_button.pack(pady=10)

        next_button.bind(
            "<Enter>", lambda e: next_button.configure(style="HoverNext.TButton")
        )
        next_button.bind(
            "<Leave>", lambda e: next_button.configure(style="NextButton.TButton")
        )

    def next_question(self, popup):
        """Move to the next question and close feedback popup."""
        popup.destroy()
        self.question_index += 1
        self.display_question()

    def transition_to_next_material(self):
        """Transition to the next learning material if available."""
        material_page = self.controller.frames["LearningMaterialPage"]

        if not material_page.display_material():
            self.questions_loaded = []
            self.controller.show_frame("LearningMaterialPage")
