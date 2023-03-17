from gtts import gTTS

voz = gTTS(text = 'texto de ejemplo', lang = 'es', slow = False)
voz.save('audio.mp3')
