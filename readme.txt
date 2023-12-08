# Text-to-Speech Web Application

This Flask web application converts text to audio using the [Bark](https://github.com/suno-ai/bark) text-to-speech library. It features a simple user interface for entering text and generating audio.

## Prerequisites

- [Python 3.6 or higher](https://www.python.org/)
- [Flask](https://palletsprojects.com/p/flask/)
- [Bark](https://github.com/suno-ai/bark) (Ensure you have the necessary Bark models)

## Installation

**Note: The installation requirements and preloading have been updated.**

1. Clone the repository:

   git clone https://github.com/VNGLR/bark-flask.git
   cd your-tts-app

    Install dependencies:

    bash

    pip install -r requirements.txt

    python app.py

## Usage

    Run the Flask application:

    bash

    python app.py

    If preloading models is skipped, Bark models will be loaded dynamically when generating audio.

    Open your web browser and navigate to http://127.0.0.1:5000/.

    Enter text in the provided form and click "Generate Audio."

    The generated audio will be available for download.

## Project Structure

project_folder/
│
├── app.py
├── preload_models.py
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── count.txt
└── text_and_hash.txt

- **app.py:** Main Flask application file.
- **preload_models.py:** Script to download and preload Bark models.
- **templates/:** Folder containing HTML templates.
- **static/:** Folder containing static assets (CSS file).
- **count.txt:** Text file storing the count of audio files generated.
- **text_and_hash.txt:** Text file maintaining a hash table of submitted text and their MD5 hashes.

### Cache and Hash Tables

The Flask application (`app.py`) now includes additional functionality related to caching and hash tables. The new features allow the application to:

- Cache generated audio files to improve performance and reduce redundant computations (referenced in `count.txt`).
- Maintain a hash table (`text_and_hash.txt`) that logs each submitted text and its corresponding MD5 hash.
--Example table, what your text_and_hash.txt should look like, ish:

Example Text 1 - c4ca4238a0b923820dcc509a6f75849b
Lorem Ipsum - d0c7f4e19d02f95dd1bf4df2ec94b907
User Submission - a5bfc9e07964f8dddeb95fc584cd965d
Another Example - 3bf111da8560a8a95739049377efcdfb

or
test again - a9dce44980071bf4b02dab73e103d779
test again - 10f671ccd4043a2d637012c4cabdd181
test again - 2fa8956b6af61be0a96b270a41a80a16
test again - 89641456e22b4f0b623973dcbf95ba31
test again - 02fdffde1c7daa3d939443e91165e9ff
test again - ebe3831415dd95cedeb186a07a4d968f
test again - 86074c5a71127398e7a6d9cfbe178fbf
test again - 5bea173b48ca3b4a00e97554ded78a30



These enhancements are controlled by command-line arguments:

- `-c` or `--cache`: Enables MD5 hash caching. 
--debug:  Run in debug mode without preloading Bark models, cache will be loaded upon first use

Customization

    Customize the appearance of the application by modifying the style.css file.
    Extend functionality by adding more routes and features in the app.py file.


Feel free to adjust the content based on your specific project details and preferences.