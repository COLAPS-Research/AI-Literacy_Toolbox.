from flask import Flask, render_template, jsonify, request
from src.data.question_data import question_data  # Importiere die Frage-Daten
from src.data.learning_material_data import learning_material  # Importiere das Lernmaterial

app = Flask(__name__)

# Route für die Startseite
@app.route('/')
def home():
    return render_template('index.html')  # Lädt die Startseite

# Route für die Quiz-Seite
@app.route('/quiz')
def quiz():
    return render_template('quiz.html')  # Lädt die Quiz-Seite

# API-Endpunkt für Fragen
@app.route('/questions', methods=['GET'])
def get_questions():
    return jsonify(question_data)  # Gibt die Frage-Daten als JSON zurück

# API-Endpunkt für die Antwort des Nutzers
@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    answer = request.json['answer']  # Holen der Antwort vom Frontend
    score = 0

    # Beispiel: Antwort 1 ist korrekt
    if answer == 0:
        score += 1

    return jsonify({'score': score})  # Gibt den Punktestand zurück

@app.route('/learning_material', methods=['GET'])
def get_learning_material():
    learning_material_with_questions = []

    # Lernmaterial mit den Fragen verknüpfen
    for material in learning_material:
        questions_for_material = []

        # Frage-IDs aus dem Lernmaterial holen und die dazugehörigen Fragen aus `question_data` extrahieren
        for q_id in material['question_ids']:
            for topic, questions in question_data.items():
                for question in questions:
                    if question['id'] == q_id:
                        questions_for_material.append(question)

        # Füge das Lernmaterial mit den zugehörigen Fragen zusammen
        learning_material_with_questions.append({
            "topic": material['topic'],
            "subtopic": material['subtopic'],
            "content": material['content'],
            "questions": questions_for_material
        })

    return jsonify(learning_material_with_questions)  # Gibt das Lernmaterial mit den Fragen als JSON zurück

# Route für Lernmaterial-Seite
@app.route('/learning_material')
def learning_material_page():
    return render_template('learning_material.html')  # Lädt die Lernmaterial-Seite

@app.route('/topics')
def topics():
    return jsonify(list(question_data.keys()))

if __name__ == '__main__':
    app.run(debug=True)
