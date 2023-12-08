from flask import Flask, render_template, request, send_file
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from io import BytesIO
import os
import argparse
from flask import jsonify

app = Flask(__name__)

def get_video_memory():
    try:
        import GPUtil
        gpu = GPUtil.getGPUs()[0]
        return f"{gpu.memoryFree} MB free out of {gpu.memoryTotal} MB total"
    except ImportError:
        return "GPUtil module not found. Please install it to get GPU information."

def get_last_count():
    try:
        with open('count.txt', 'r') as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return 0

def update_last_count(count):
    with open('count.txt', 'w') as file:
        file.write(str(count))

def preload_bark_models():
    print("Preloading Bark models...")
    preload_models()
    print("Bark models preloaded.")

def parse_command_line_args():
    parser = argparse.ArgumentParser(description="Flask Text-to-Speech Web Application")
    parser.add_argument('--debug', action='store_true', help='Run in debug mode without preloading Bark models')
    return parser.parse_args()

# Parse command-line arguments
args = parse_command_line_args()

# download and load all models if not in debug mode
if not args.debug:
    preload_bark_models()

last_count = get_last_count()
print(f"Last count: {last_count}")

@app.route('/')
def index():
    print(get_video_memory())
    video_memory = get_video_memory()
    return render_template('index.html', video_memory=video_memory)

@app.route('/get_video_memory')
def get_video_memory_endpoint():
    video_memory = get_video_memory()
    return jsonify({'video_memory': video_memory})

@app.route('/generate_audio', methods=['POST'])
def generate_audio_endpoint():
    text_prompt = request.form['text_prompt']

    # Debugging video memory before generating audio
    print(get_video_memory())

    # generate audio from text
    audio_array = generate_audio(text_prompt, history_prompt="v2/en_speaker_9")

    # Debugging video memory after generating audio
    print(get_video_memory())

    # Increment the count
    last_count = get_last_count()
    current_count = last_count + 1

    # save audio to memory buffer with incremented count
    audio_buffer = BytesIO()
    write_wav(audio_buffer, SAMPLE_RATE, audio_array)
    audio_buffer.seek(0)

    # Save the audio file with an incremented count
    audio_filename = f"audio_{current_count}.wav"
    with open(audio_filename, 'wb') as audio_file:
        audio_file.write(audio_buffer.read())

    # Update the last count
    update_last_count(current_count)

    return send_file(audio_filename, mimetype="audio/wav", as_attachment=True, download_name=audio_filename)

if __name__ == '__main__':
    app.run(debug=True)
