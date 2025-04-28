from flask import Flask, request, jsonify
from inference import summarize_and_extract
from mcq import generate_mcqs
from flask_cors import CORS  # important to allow frontend to call backend

app = Flask(__name__)
CORS(app)  # Allow CORS

@app.route('/process-text', methods=['POST'])
def process_text():
    data = request.get_json()
    input_text = data.get('text', '')

    if not input_text.strip():
        return jsonify({'error': 'No text provided.'}), 400

    try:
        summary, keywords, keyword_sentences = summarize_and_extract(input_text)
        mcqs = generate_mcqs(input_text)

        return jsonify({
            'summary': summary,
            'keywords': keywords,
            'mcqs': mcqs
        })
    except Exception as e:
        print(e)
        return jsonify({'error': 'Error processing the text.'}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
