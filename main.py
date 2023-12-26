from flask import Flask, render_template, request, jsonify
from threading import Timer

app = Flask(__name__)

# Variable to store the text
current_text = ""

# Timeout duration in seconds
timeout_duration = 5  # Adjust as needed

# Timer object for tracking inactivity
timeout_timer = None

def clear_text():
    global current_text
    current_text = ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_text', methods=['POST'])
def update_text():
    global current_text, timeout_timer

    text = request.form['text']
    current_text = text

    # Cancel previous timer (if any)
    if timeout_timer:
        timeout_timer.cancel()

    # Start a new timer
    timeout_timer = Timer(timeout_duration, clear_text)
    timeout_timer.start()

    return 'Text updated successfully'

@app.route('/get_text')
def get_text():
    global current_text
    return jsonify({'text': current_text})

if __name__ == '__main__':
    app.run(debug=True)
