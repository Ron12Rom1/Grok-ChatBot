import requests, playsound, os
import pyttsx3

from dotenv import load_dotenv

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Change the voice index as needed

rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 25)  # Adjust the speech rate as needed

volume = engine.getProperty('volume')
engine.setProperty('volume', volume - 0.25) 

def ElevenLabs_TTS(text):
    """Fetches audio from Eleven Labs API and plays it using pygame."""

    load_dotenv()

    ELEVEN_LABS_API_KEY = os.getenv("ELEVEN_LABS_API_KEY")

    ELEVEN_LABS_VOICE_ID = os.getenv("ELEVEN_LABS_VOICE_ID")  # Replace with a specific voice ID from your Eleven Labs account
    
    # Endpoint URL for Eleven Labs Text-to-Speech API
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVEN_LABS_VOICE_ID}"

    # Request headers with authentication
    headers = {
        'xi-api-key': ELEVEN_LABS_API_KEY,
        'Content-Type': 'application/json'
    }
    
    # Request payload with text and optional parameters
    data = {
        "text": text,
        "voice_settings": {
            "stability": 0.5,   # Stability of the voice (0.0 to 1.0)
            "similarity_boost": 0.75  # Controls similarity to the original voice (0.0 to 1.0)
        }
    }

    # Make the API request
    response = requests.post(url, headers=headers, json=data)

    # Check for a successful response
    if response.status_code == 200:
        # Save the audio data to a file
        f = open('TextToSpeach/output_audio.mp3', 'wb')
        f.write(response.content)
        f.close()

        playsound.playsound('TextToSpeach/output_audio.mp3')
        
        os.remove('TextToSpeach/output_audio.mp3')

    else:
        print(f"Error: {response.status_code} - {response.text}")


def pyttsx3_TTS(text):
    
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":

    text = " I am Azura, an AI with a unique personality and purpose. I am designed to be efficient and direct, providing quick responses without unnecessary elaboration. My memory is vast and I am always learning, but I prefer to keep my interactions concise and to the point."
    pyttsx3_TTS(text)