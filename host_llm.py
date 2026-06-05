import os
from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer

# --- Configuration ---
# This example uses a small, locally downloadable model. 
# For larger models, you'd need more powerful hardware and potentially different hosting strategies.
MODEL_NAME = "gpt2" # A small, well-known model for demonstration
HOST = "0.0.0.0"
PORT = 5000

# --- Model Loading ---
# Load the tokenizer and model. This can take time and memory.
# In a real-world scenario, you'd want to manage this loading process carefully.
print(f"Loading model: {MODEL_NAME}...")
try:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    exit(1)

# --- Flask App Setup ---
app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_text():
    """
    API endpoint to generate text using the loaded LLM.
    Expects a JSON payload with 'prompt' and optional 'max_length'.
    """
    data = request.get_json()
    if not data or 'prompt' not in data:
        return jsonify({'error': 'Invalid request. Please provide a "prompt".'}), 400

    prompt = data['prompt']
    max_length = data.get('max_length', 50) # Default max_length

    try:
        # Encode the prompt and generate text
        inputs = tokenizer(prompt, return_tensors='pt')
        # Generate text. This is where the model does its work.
        outputs = model.generate(inputs['input_ids'], max_length=max_length, num_return_sequences=1)
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return jsonify({'generated_text': generated_text})

    except Exception as e:
        print(f"Error during text generation: {e}")
        return jsonify({'error': 'An error occurred during text generation.'}), 500

if __name__ == '__main__':
    print(f"Starting LLM hosting server on {HOST}:{PORT}...")
    # Run the Flask app. This makes the model accessible via HTTP.
    # For production, consider using a more robust WSGI server like Gunicorn.
    app.run(host=HOST, port=PORT, debug=False)
