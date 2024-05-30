from pydub import AudioSegment
from io import BytesIO



def process_mp3(r):
    # from_mp3 expect a file-like object, so we provide a way to treat the audio content as a readable sequence of bytes
    audio_content = BytesIO(r.content)

    # Load mp3 content into AudioSegment
    mp3_audio = AudioSegment.from_mp3(audio_content)

    # Process it 
    duration = len(mp3_audio)
    print("duration as proof of processing :", duration)
