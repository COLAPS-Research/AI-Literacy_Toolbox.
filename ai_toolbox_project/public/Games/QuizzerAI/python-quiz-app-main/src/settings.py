"""Stores all the customizable settings for the application"""

# Dictionary to store customizable settings for the application
SETTINGS = {
    "general": {
        "title": "QuizzerAI",
        "version": "0.0.1",
        "authors": "Lara, Cate, Linda & Yannick",
        "description": "A quizzer application for AI learning",
        "image_size": "960x540",
        "theme": "clam",
    },
    # Fonts and Font Sizes
    "font": {
        "primary": "Comic Sans MS",
        "secondary": "Helvetica",
        "monospace": "Courier New",
        "default_size": 12,
        "heading_size": 18,
        "subheading_size": 16,
    },
    # Colors
    "colors": {
        "background": "#ffffff",
        "text_primary": "#000000",
        "text_secondary": "#555555",
        "button_background": "#007bff",
        "button_text": "#ffffff",
        "error": "#ff0000",
        "success": "#28a745",
    },
    # Images and Icons used to style the application
    "images_and_icons": {
        "icon_deepfakes": "images/deepfakes1.png",
        "icon_myth": "images/myths_and_facts.png",
        "icon_arrow": "images/arrow-next.png",
        "background_image": "images/Stars5.jpg",
    },
    # Label Texts
    "labels": {
        "welcome": "Welcome to the Application!",
        "submit_button": "Submit",
        "cancel_button": "Cancel",
        "error_message": "An error occurred. Please try again.",
        "success_message": "Operation completed successfully!",
    },
    # Other Customizable Settings
    "misc": {
        "default_language": "en",
        "date_format": "%Y-%m-%d",
        "time_format": "%H:%M:%S",
        "items_per_page": 10,
    },
    "translations": {
        "correct_en": "Correct",
        "incorrect_en": "Incorrect",
        "next_en": "Next",
        "choose_en": "Choose a topic...",
        "results_en": "Your Results:",
        "restart_en": "Restart"
    },
}
