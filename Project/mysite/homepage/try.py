import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=1)
    playsound('speak.mp3')
    audio = r.listen(source, phrase_time_limit=20)
    playsound(audio)