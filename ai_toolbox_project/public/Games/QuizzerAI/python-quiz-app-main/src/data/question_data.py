"""Question data for the application."""

question_data = {
    "Deepfakes": [
        {
            "id": 0,
            "question_text": "What are deepfakes?",
            "options": [
                {
                    "answer_text": "Realistic fake videos, images or audios created with AI",
                    "explanation": "True: Deepfakes are generated using AI to create convincing fake media.",
                },
                {
                    "answer_text": "A tool to fix blurry photos and videos",
                    "explanation": "False: Deepfakes are about creating fake content, not enhancing image quality.",
                },
                {
                    "answer_text": "Real images and videos that look fake",
                    "explanation": "False: Deepfakes are fake media that appear real, not real media that appear fake.",
                },
            ],
            "answer": 0,
            "learning_material_id": 0,
        },
        {
            "id": 1,
            "question_text": "How does deepfake work?",
            "options": [
                {
                    "answer_text": "It uses green screen to replace the background",
                    "explanation": "False: Green screen technology is unrelated to deepfake creation.",
                },
                {
                    "answer_text": "It uses AI to learn and copy someone’s face and voice",
                    "explanation": "True: AI learns and replicates facial and vocal characteristics for deepfake "
                    "creation.",
                },
                {
                    "answer_text": "It copies someone‘s voice by recording their thoughts",
                    "explanation": "False: AI can mimic voices but cannot read or record thoughts.",
                },
            ],
            "answer": 1,
            "learning_material_id": 1,
        },
        {
            "id": 2,
            "question_text": "What are signs to recognize deepfakes?",
            "options": [
                {
                    "answer_text": "Videos always having a bad audio quality",
                    "explanation": "False: Not all deepfakes have bad audio; quality depends on the creator.",
                },
                {
                    "answer_text": "Weird facial movements or unnatural audio",
                    "explanation": "True: Deepfakes often have subtle flaws like odd facial expressions or "
                    "mismatched audio.",
                },
                {
                    "answer_text": "Perfectly smooth skin without any shadows",
                    "explanation": "False: While some deepfakes are highly detailed, smooth skin alone isn’t a reliable"
                    "indicator.",
                },
            ],
            "answer": 1,
            "learning_material_id": 2,
        },
        {
            "id": 3,
            "question_text": "Is it always possible to recognize a deepfake?",
            "options": [
                {
                    "answer_text": "It depends on how old the video or image is",
                    "explanation": "False: The age of the content does not determine the ease of recognizing a "
                    "deepfake.",
                },
                {
                    "answer_text": "Yes, deepfakes are very obvious",
                    "explanation": "False: Many deepfakes are sophisticated and not easily recognizable.",
                },
                {
                    "answer_text": "No, sometimes they are really hard to tell apart",
                    "explanation": "True: Advanced deepfakes can be indistinguishable from real content.",
                },
            ],
            "answer": 2,
            "learning_material_id": 2,
        },
        {
            "id": 4,
            "question_text": "Why can deepfakes be dangerous?",
            "options": [
                {
                    "answer_text": "Because it’s not allowed to post deepfakes on social media",
                    "explanation": "False: The danger lies especially in their misuse, not just posting restrictions.",
                },
                {
                    "answer_text": "Because mostly they spread faster on the internet and are difficult to recognize",
                    "explanation": "True: Deepfakes can quickly disseminate misinformation and are hard to detect.",
                },
                {
                    "answer_text": "Because you never recognize them",
                    "explanation": "False: Some deepfakes are detectable, though not always.",
                },
            ],
            "answer": 1,
            "learning_material_id": 3,
        },
        {
            "id": 5,
            "question_text": "What possibilities bring deepfakes?",
            "options": [
                {
                    "answer_text": "They could help for a better communication in different languages",
                    "explanation": "True: Deepfakes can be used for language translation and communication "
                    "improvement.",
                },
                {
                    "answer_text": "They don’t have any benefits",
                    "explanation": "False: Deepfakes have potential for positive uses in communication and "
                    "entertainment.",
                },
                {
                    "answer_text": "They create better special effects in movies without using actors",
                    "explanation": "False: While deepfakes may enhance effects, this is not their primary benefit.",
                },
            ],
            "answer": 0,
            "learning_material_id": 4,
        },
        {
            "id": 6,
            "question_text": "Is it allowed to post deepfakes on social media?",
            "options": [
                {
                    "answer_text": "No, social media doesn’t allow to post deepfakes",
                    "explanation": "False: Policies vary by platform, and not all ban deepfakes outright.",
                },
                {
                    "answer_text": "Yes, but only if it is clearly labeled as fake",
                    "explanation": "False: Some platforms may require labeling, but this is not universally true.",
                },
                {
                    "answer_text": "It depends on the platform, because each one has different rules and rights",
                    "explanation": "True: Posting policies for deepfakes differ across social media platforms.",
                },
            ],
            "answer": 2,
            "learning_material_id": 5,
        },
    ],
    "Myths and Facts": [
        {
            "id": 0,
            "question_text": "Can AI solve every problem in the world all at once?",
            "options": [
                {
                    "answer_text": "Yes, because AI can do anything, like magic",
                    "explanation": "False: AI is powerful but is not magical and has limitations.",
                },
                {
                    "answer_text": "No, AI is designed for specific tasks and needs programming for each job",
                    "explanation": "True: AI requires training and specific programming for tasks.",
                },
                {
                    "answer_text": "Yes, AI is smarter than humans and knows how to do everything",
                    "explanation": "False: AI is not inherently smarter than humans; "
                    "it depends on data and programming.",
                },
                {
                    "answer_text": "No because AI is overstrained to work on many things at once",
                    "explanation": "False: AI’s limitations are due to task specificity, not overstrain.",
                },
            ],
            "answer": 1,
            "learning_material_id": 0,
        },
        {
            "id": 1,
            "question_text": "Does AI always figure things out all by itself without any help from humans?",
            "options": [
                {
                    "answer_text": "Yes, AI is completely independent and doesn’t need humans at all.",
                    "explanation": "False: I doesn't work completely independently. It needs humans to program it, "
                    "provide data, and guide its learning process. Without human input, AI can't operate"
                    "effectively. ",
                },
                {
                    "answer_text": "Sometimes, AI figures things out but often cheats by copying from humans.",
                    "explanation": "False: While AI can learn from data provided by humans, it doesn't cheat. It "
                    "processes data and recognizes patterns. The role of humans is to provide quality "
                    "data and proper guidance, not to be copied.",
                },
                {
                    "answer_text": "No, AI needs humans to give it information and teach it how to work.",
                    "explanation": "True: AI requires human input, especially when it comes to training, programming, "
                    "and providing feedback. Humans are essential for guiding AI's learning process and "
                    "ensuring it operates correctly",
                },
                {
                    "answer_text": "AI can sometimes guess things, but it mostly relies on humans to guide it.",
                    "explanation": "False: While AI might make predictions or estimates based on data, it doesn't "
                    "guess in the way humans do. AI’s decisions are data-driven, and it still heavily "
                    "relies on humans to supply the right data, algorithms, and training.",
                },
            ],
            "answer": 2,
            "learning_material_id": 1,
        },
        {
            "id": 2,
            "question_text": "Do AI know everything, so humans don’t need to help them at all?",
            "options": [
                {
                    "answer_text": "Yes, AI already knows more than any human ever will.",
                    "explanation": "False: AI does not know more than humans. It can process vast amounts of data "
                    "quickly, but it still relies on human input and doesn't possess human-like "
                    "understanding or knowledge.",
                },
                {
                    "answer_text": "No, but AI can guess answers without needing any real information.",
                    "explanation": "False: AI doesn't simply guess. It relies on data to make informed decisions or "
                    "predictions. It needs real, structured information to learn and generate responses."
                    "Guessing without data is not how AI works.",
                },
                {
                    "answer_text": "Yes, AI is programmed with every fact in the world.",
                    "explanation": "False: AI is not programmed with every fact. It learns from data, but it doesn't "
                    "have access to all the information in the world, nor is it programmed with all "
                    "facts. Its knowledge is limited by the data it's trained on.",
                },
                {
                    "answer_text": "No, AI can only use the data it’s been given and doesn’t know everything.",
                    "explanation": "True: AI can only work with the data it's provided and doesn't have innate "
                    "knowledge. It relies on humans to supply data and guidance, and it doesn't know "
                    "everything outside of what it has been trained on.",
                },
            ],
            "answer": 3,
            "learning_material_id": 1,
        },
        {
            "id": 3,
            "question_text": "Will AI take over the world like in movies and make humans disappear?",
            "options": [
                {
                    "answer_text": "Yes, AI is already building secret armies to take over.",
                    "explanation": "False: This is purely fictional and based on movies. AI does not build secret "
                    "armies or have any desire for power. It is a tool created and controlled by "
                    "humans.",
                },
                {
                    "answer_text": "No, AI will stop working if it gets too powerful.",
                    "explanation": "False: AI does not stop working if it becomes too powerful. It depends on human "
                    "oversight and control. AI needs to be carefully monitored, but it doesn’t "
                    "automatically shut down because it’s powerful.",
                },
                {
                    "answer_text": "No, AI follows rules and can’t do things it’s not programmed to do.",
                    "explanation": "True: AI operates based on the rules and algorithms it's programmed with. It cannot"
                    "make decisions beyond what it's designed to do, and it requires human input for "
                    "tasks beyond its programming.",
                },
                {
                    "answer_text": "Yes, AI will become so powerful that humans won’t be needed anymore.",
                    "explanation": "False: AI is a tool meant to assist humans, not replace them entirely. Humans "
                    "provide the creativity, judgment, and oversight needed to ensure AI functions "
                    "responsibly and effectively. AI cannot fully replace human skills and "
                    "intelligence.",
                },
            ],
            "answer": 2,
            "learning_material_id": 2,
        },
        {
            "id": 4,
            "question_text": "Is AI like a super-genius that's way smarter than any person in the world?",
            "options": [
                {
                    "answer_text": "Yes, AI is the smartest thing ever created.",
                    "explanation": "False: While AI can be very efficient at specific tasks, it is not universally "
                    "smarter than humans. It lacks human-like reasoning, creativity, and emotional "
                    "intelligence. AI excels in data processing, but it is not an all-knowing entity.",
                },
                {
                    "answer_text": "No, AI is good at specific tasks but not as smart as humans overall.",
                    "explanation": "True: AI excels at certain tasks like pattern recognition or data analysis, but it "
                    "doesn't have the general intelligence or adaptability of humans. Humans can think "
                    "creatively, solve complex problems, and apply knowledge in diverse ways, something "
                    "AI cannot do on its own.",
                },
                {
                    "answer_text": "Yes, AI is so smart it can predict the future.",
                    "explanation": "False: AI can make predictions based on patterns in data, but it cannot predict the"
                    "future with certainty. Its predictions are based on past data, and it cannot "
                    "foresee future events in the way humans might expect.",
                },
                {
                    "answer_text": "No, AI is just a robot with no brain power at all.",
                    "explanation": "False: AI is not a robot in the traditional sense, but it does have computational"
                    "power and can process data, learn from it, and make decisions. While it doesn't "
                    "have a brain like humans, it operates on algorithms and data to perform tasks, "
                    "which shows a form of artificial intelligence.",
                },
            ],
            "answer": 1,
            "learning_material_id": 3,
        },
        {
            "id": 5,
            "question_text": "Can AI turn evil, like a villain in a story, or become alive like a person?",
            "options": [
                {
                    "answer_text": "Yes, AI is alive and can make its own choices, good or bad.",
                    "explanation": "False: AI is not alive. It does not have consciousness or free will. It operates"
                    "based on algorithms and data, following instructions set by humans. "
                    "It cannot independently make good or bad choices like a living being.",
                },
                {
                    "answer_text": "No, AI can turn evil only if it’s given the wrong instructions.",
                    "explanation": "False: While AI can make mistakes or be misused due to incorrect instructions or "
                    "flawed data, it doesn't inherently turn evil. "
                    "AI is a tool that follows its programming; it can't act with malicious intent "
                    "unless specifically designed or misused in harmful ways.",
                },
                {
                    "answer_text": "No, AI isn’t alive and can’t turn evil because it follows programming.",
                    "explanation": "True: AI is not alive and doesn't have emotions or intentions. It works by "
                    "following rules and algorithms programmed by humans. Any harmful actions from AI "
                    "would be the result of human decisions or flaws in its programming, not the AI "
                    "acting evil on its own.",
                },
                {
                    "answer_text": "Yes, AI can turn evil if it gets hacked by another AI.",
                    "explanation": "False: While hacking can cause AI systems to behave unpredictably or maliciously, "
                    "AI does not have the ability to turn evil on its own. It's a tool that requires "
                    "human oversight and guidance.",
                },
            ],
            "answer": 2,
            "learning_material_id": 4,
        },
        {
            "id": 6,
            "question_text": "Is it impossible to make rules and laws to control AI and how it’s used?",
            "options": [
                {
                    "answer_text": "Yes, AI is so advanced that no rules or laws can control it.",
                    "explanation": "False: AI is a tool created and controlled by humans. While it’s complex, rules "
                    "and laws can be established to regulate its development and usage to ensure it is "
                    "used ethically and safely.",
                },
                {
                    "answer_text": "Yes because AI always finds ways to break rules like a sneaky trickster.",
                    "explanation": "False: AI does not have an independent will or intent to break rules. It follows "
                    "the instructions given by humans. Any issues with AI breaking rules would result "
                    "from improper programming, not AI actively trying to trick anyone.",
                },
                {
                    "answer_text": "No, humans can create rules and laws to guide how AI is developed and used.",
                    "explanation": "True: It is possible for humans to create regulations, guidelines, and laws to "
                    "ensure that AI is developed and used responsibly. Governments and organizations can"
                    "set ethical standards, safety measures, and frameworks for AI deployment.",
                },
                {
                    "answer_text": "No, but only if the AI agrees to follow the rules by itself.",
                    "explanation": "False: AI cannot agree to follow rules on its own. It is not autonomous in that "
                    "way. AI operates based on the rules and instructions it is programmed with, and any"
                    "compliance with laws depends on human oversight and enforcement, not the AI's own "
                    "decisions.",
                },
            ],
            "answer": 2,
            "learning_material_id": 5,
        },
        {
            "id": 7,
            "question_text": "Can AI be used to help doctors and nurses take better care of patients?",
            "options": [
                {
                    "answer_text": "Yes, AI can assist by analyzing data, helping  with diagnoses, and suggesting "
                    "treatments.",
                    "explanation": "True: AI can significantly support healthcare professionals by analyzing medical "
                    "data, assisting with diagnoses, and recommending treatments. It helps doctors make "
                    "more accurate decisions and improves patient care by identifying patterns in data "
                    "that might be missed by humans.",
                },
                {
                    "answer_text": "No, AI doesn’t work well in hospitals because it’s too slow.",
                    "explanation": "False: AI is not slow. In fact, it can process large amounts of data very quickly, "
                    "which is crucial in healthcare settings. AI can assist doctors by providing rapid "
                    "insights, especially in situations requiring quick decision-making.",
                },
                {
                    "answer_text": "Yes, but AI can only help doctors with simple tasks like making appointments.",
                    "explanation": "False: AI is capable of much more than just simple tasks. It can assist with "
                    "complex medical tasks such as diagnosing conditions, analyzing medical images, "
                    "predicting outcomes, and recommending treatment plans, not just administrative "
                    "tasks like appointments.",
                },
                {
                    "answer_text": "No, doctors and nurses don’t need AI to do their jobs better.",
                    "explanation": "False: While doctors and nurses have expertise, AI can enhance their ability to "
                    "provide better care. It can analyze large volumes of data, identify trends, and "
                    "assist in decision-making, ultimately improving patient outcomes and reducing "
                    "errors.",
                },
            ],
            "answer": 0,
            "learning_material_id": 5,
        },
    ],
}
