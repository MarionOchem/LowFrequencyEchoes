from transformers import pipeline

pipe = pipeline("emotion-recognition", model="Lajavaness/wav2vec2-lg-xlsr-fr-speech-emotion-recognition") 