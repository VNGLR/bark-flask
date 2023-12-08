# Text-to-Speech Web Application

This Flask web application converts text to audio using the [Bark](https://github.com/suno-ai/bark) text-to-speech library. It features a simple user interface for entering text and generating audio.

## Prerequisites

- [Python 3.6 or higher](https://www.python.org/)
- [Flask](https://palletsprojects.com/p/flask/)
- [Bark](https://github.com/suno-ai/bark) (Ensure you have the necessary Bark models)

## Installation

NOTE

iNSTALLATION REQUIREMENTS AND PRELOAD NOT DONE... MAYBE DONE SOMEDAY
Install flash and bark and it should work
recommend installing cuda for GPU use, CPU use is very slow, GPU is almost realtime.
Note will have issues on sentences longer then ~ 14 seconds, will impliment later
NOTE

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-tts-app.git
   cd your-tts-app

    Install dependencies:

    bash

pip install -r requirements.txt

Download and preload Bark models:

bash

    python preload_models.py

Usage

    Run the Flask application:

    bash

    python app.py

    Open your web browser and navigate to http://127.0.0.1:5000/.

    Enter text in the provided form and click "Generate Audio."

    The generated audio will be available for download.

Project Structure

arduino

project_folder/
│
├── app.py
├── preload_models.py
├── templates/
│   └── index.html
│
└── static/
    └── style.css

    app.py: Main Flask application file.
    preload_models.py: Script to download and preload Bark models.
    templates/: Folder containing HTML templates.
    static/: Folder containing static assets (CSS file).

Customization

    Customize the appearance of the application by modifying the style.css file.
    Extend functionality by adding more routes and features in the app.py file.





This version provides links for installing Bark and Flask, making it more straightforward for users to access the necessary resources.
