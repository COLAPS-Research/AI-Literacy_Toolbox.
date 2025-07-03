import unittest

from src.settings import SETTINGS


class TestSettings(unittest.TestCase):
    """
    Check basic structure of settings.py.
    """

    def test_general_settings(self):
        """Verify general settings exist and have required keys"""
        self.assertIn("general", SETTINGS, "Missing 'general' key in SETTINGS")
        general = SETTINGS["general"]
        required_keys = [
            "title",
            "version",
            "authors",
            "description",
            "image_size",
            "theme",
        ]
        for key in required_keys:
            self.assertIn(key, general, f"Missing '{key}' in general settings")

    def test_font_settings(self):
        """Verify font settings exist and have required keys"""
        self.assertIn("font", SETTINGS, "Missing 'font' key in SETTINGS")
        font = SETTINGS["font"]
        required_keys = [
            "primary",
            "secondary",
            "monospace",
            "default_size",
            "heading_size",
            "subheading_size",
        ]
        for key in required_keys:
            self.assertIn(key, font, f"Missing '{key}' in font settings")

        # Verify font sizes are integers
        self.assertIsInstance(
            font["default_size"], int, "'default_size' should be an integer"
        )
        self.assertIsInstance(
            font["heading_size"], int, "'heading_size' should be an integer"
        )
        self.assertIsInstance(
            font["subheading_size"], int, "'subheading_size' should be an integer"
        )

    def test_color_settings(self):
        """Verify color settings exist and have required keys"""
        self.assertIn("colors", SETTINGS, "Missing 'colors' key in SETTINGS")
        colors = SETTINGS["colors"]
        required_keys = [
            "background",
            "text_primary",
            "text_secondary",
            "button_background",
            "button_text",
            "error",
            "success",
        ]
        for key in required_keys:
            self.assertIn(key, colors, f"Missing '{key}' in color settings")

        # Verify colors are valid hex codes
        for key, value in colors.items():
            self.assertRegex(
                value,
                r"^#(?:[0-9a-fA-F]{3}){1,2}$",
                f"'{key}' does not have a valid hex color code",
            )

    def test_images_and_icons(self):
        """Verify images_and_icons settings exist and have required keys"""
        self.assertIn(
            "images_and_icons", SETTINGS, "Missing 'images_and_icons' key in SETTINGS"
        )
        images_and_icons = SETTINGS["images_and_icons"]
        required_keys = [
            "icon_deepfakes",
            "icon_myth",
            "icon_llm",
            "icon_arrow",
            "background_image",
        ]
        for key in required_keys:
            self.assertIn(
                key, images_and_icons, f"Missing '{key}' in images_and_icons settings"
            )

    def test_labels(self):
        """Verify labels settings exist and have required keys"""
        self.assertIn("labels", SETTINGS, "Missing 'labels' key in SETTINGS")
        labels = SETTINGS["labels"]
        required_keys = [
            "welcome",
            "submit_button",
            "cancel_button",
            "error_message",
            "success_message",
        ]
        for key in required_keys:
            self.assertIn(key, labels, f"Missing '{key}' in labels settings")

    def test_misc_settings(self):
        """Verify misc settings exist and have required keys"""
        self.assertIn("misc", SETTINGS, "Missing 'misc' key in SETTINGS")
        misc = SETTINGS["misc"]
        required_keys = [
            "default_language",
            "date_format",
            "time_format",
            "items_per_page",
        ]
        for key in required_keys:
            self.assertIn(key, misc, f"Missing '{key}' in misc settings")

        # Verify items_per_page is an integer
        self.assertIsInstance(
            misc["items_per_page"], int, "'items_per_page' should be an integer"
        )

        # Verify default_language is a string
        self.assertIsInstance(
            misc["default_language"], str, "'default_language' should be a string"
        )


if __name__ == "__main__":
    unittest.main()
