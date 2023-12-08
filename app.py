from flask import Flask, render_template, request, send_file
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from io import BytesIO

app = Flask(__name__)


def get_video_memory():
    try:
        import GPUtil
        gpu = GPUtil.getGPUs()[0]
        return f"{gpu.memoryFree} MB free out of {gpu.memoryTotal} MB total"
    except ImportError:
        return "GPUtil module not found. Please install it to get GPU information."


# download and load all models
print(get_video_memory());
preload_models()
print(get_video_memory());
@app.route('/')
def index():
    print(get_video_memory());
    return render_template('index.html')

@app.route('/generate_audio', methods=['POST'])
def generate_audio_endpoint():
    text_prompt = request.form['text_prompt']

    # generate audio from text
    audio_array = generate_audio(text_prompt, history_prompt="v2/en_speaker_9")

    # save audio to memory buffer
    audio_buffer = BytesIO()
    write_wav(audio_buffer, SAMPLE_RATE, audio_array)
    audio_buffer.seek(0)

    return send_file(audio_buffer, mimetype="audio/wav", as_attachment=True, download_name="generated_audio.wav")

if __name__ == '__main__':
    app.run(debug=True)
