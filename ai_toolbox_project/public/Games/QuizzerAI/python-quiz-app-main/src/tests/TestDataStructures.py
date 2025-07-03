import unittest
from src.data.question_data import question_data
from src.data.learning_material_data import learning_material
from src.data.topic_data import topic_data


class TestDataStructures(unittest.TestCase):

    def test_question_data_structure(self):
        # Verify question_data is a dictionary
        self.assertIsInstance(
            question_data, dict, "question_data should be a dictionary"
        )

        for category, questions in question_data.items():
            # Verify category is a string
            self.assertIsInstance(category, str, "Category keys should be strings")

            # Verify questions is a list
            self.assertIsInstance(questions, list, "Questions should be a list")

            for question in questions:
                # Verify each question is a dictionary
                self.assertIsInstance(
                    question, dict, "Each question should be a dictionary"
                )

                # Check required keys
                self.assertIn("id", question, "Missing 'id' key in question")
                self.assertIn(
                    "question_text", question, "Missing 'question_text' key in question"
                )
                self.assertIn("options", question, "Missing 'options' key in question")
                self.assertIn("answer", question, "Missing 'answer' key in question")
                self.assertIn(
                    "learning_material_id",
                    question,
                    "Missing 'learning_material_id' key in question",
                )

                # Verify types of values
                self.assertIsInstance(question["id"], int, "'id' should be an integer")
                self.assertIsInstance(
                    question["question_text"], str, "'question_text' should be a string"
                )
                self.assertIsInstance(
                    question["options"], list, "'options' should be a list"
                )
                self.assertIsInstance(
                    question["answer"], int, "'answer' should be an integer"
                )
                self.assertIsInstance(
                    question["learning_material_id"],
                    int,
                    "'learning_material_id' should be an integer",
                )

                for option in question["options"]:
                    # Verify each option is a dictionary
                    self.assertIsInstance(
                        option, dict, "Each option should be a dictionary"
                    )

                    # Check required keys in options
                    self.assertIn(
                        "answer_text", option, "Missing 'answer_text' key in option"
                    )
                    self.assertIn(
                        "explanation", option, "Missing 'explanation' key in option"
                    )

                    # Verify types of option values
                    self.assertIsInstance(
                        option["answer_text"], str, "'answer_text' should be a string"
                    )
                    self.assertIsInstance(
                        option["explanation"], str, "'explanation' should be a string"
                    )

    def test_learning_material_structure(self):
        # Verify learning_material is a list
        self.assertIsInstance(
            learning_material, list, "learning_material should be a list"
        )

        for material in learning_material:
            # Verify each material is a dictionary
            self.assertIsInstance(
                material, dict, "Each material should be a dictionary"
            )

            # Check required keys
            self.assertIn("topic", material, "Missing 'topic' key in material")
            self.assertIn("subtopic", material, "Missing 'subtopic' key in material")
            self.assertIn("content", material, "Missing 'content' key in material")
            self.assertIn(
                "question_ids", material, "Missing 'question_ids' key in material"
            )
            self.assertIn(
                "learning_material_index",
                material,
                "Missing 'learning_material_index' key in material",
            )

            # Verify types of values
            self.assertIsInstance(material["topic"], str, "'topic' should be a string")
            self.assertIsInstance(
                material["subtopic"], str, "'subtopic' should be a string"
            )
            self.assertIsInstance(
                material["content"], str, "'content' should be a string"
            )
            self.assertIsInstance(
                material["question_ids"], list, "'question_ids' should be a list"
            )
            self.assertIsInstance(
                material["learning_material_index"],
                int,
                "'learning_material_index' should be an integer",
            )

            for question_id in material["question_ids"]:
                # Verify each question_id is an integer
                self.assertIsInstance(
                    question_id, int, "Each 'question_id' should be an integer"
                )

    def test_topic_data_structure(self):
        # Verify topic_data is a list
        self.assertIsInstance(topic_data, list, "topic_data should be a list")

        for topic in topic_data:
            # Verify each topic is a string
            self.assertIsInstance(topic, str, "Each topic should be a string")

    def test_question_id_mapping(self):
        # Verify that question_ids in learning_material map to valid questions in question_data
        question_ids = set()
        for category_questions in question_data.values():
            for question in category_questions:
                question_ids.add(question["id"])

        for material in learning_material:
            for question_id in material["question_ids"]:
                self.assertIn(
                    question_id,
                    question_ids,
                    f"Question ID {question_id} in learning_material does not exist in question_data",
                )

    def test_learning_material_id_consistency(self):
        # Verify that each question's learning_material_id maps to a valid learning material
        learning_material_ids = {
            material["learning_material_index"] for material in learning_material
        }

        for category_questions in question_data.values():
            for question in category_questions:
                self.assertIn(
                    question["learning_material_id"],
                    learning_material_ids,
                    f"Learning Material ID {question['learning_material_id']} in question_data does not exist in learning_material",
                )


if __name__ == "__main__":
    unittest.main()
