from gtts import gTTS
a = input("Type Text Here ")
l = "en"
out = gTTS(text=a,lang=l,slow=False)
out.save("voice.mp3")
