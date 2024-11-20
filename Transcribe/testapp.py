from openai import OpenAI
client = OpenAI()

audio_file= open("audio.mp3", "rb")
transcription = client.audio.translations.create(
  model="whisper-1",
  response_format="text",
  file=audio_file
)
#print(transcription)
f = open("myfile.txt", "w")
f.write(transcription)
f.close()

