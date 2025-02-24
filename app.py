from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)

# Load the trained model
nlp = spacy.load('activity_extractor_model')

def extract_person_activities(text):
    doc = nlp(text)
    person_activities = []
    people = []
    activity_queue = []

    # Collect all entities first
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            people.append(ent.text)
        elif ent.label_ == 'ACTIVITY':
            activity_queue.append(ent.text.lower().replace('reads', 'reading').replace('does', 'doing'))

    # Use context tracking to link people and activities
    for sent in doc.sents:
        current_person = None
        for token in sent:
            if token.ent_type_ == 'PERSON':
                current_person = token.text
            elif token.ent_type_ == 'ACTIVITY' and current_person:
                activity = token.text.lower().replace('reads', 'reading').replace('does', 'doing')
                person_activities.append({'Person': current_person, 'Activity': activity})
                current_person = None

    # Fallback pairing for unmatched activities
    if not person_activities and people and activity_queue:
        person_activities = [{'Person': p, 'Activity': a} for p, a in zip(people, activity_queue)]

    return person_activities

@app.route('/extract', methods=['POST'])
def extract():
    text = request.json.get('text')
    result = extract_person_activities(text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
