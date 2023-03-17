from gtts import gTTS

voz = gTTS(text = 'Las lágrimas que curan son también las que queman y mortifican', lang = 'es', slow = False)
voz.save('audio.mp3')