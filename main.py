import os
from google.cloud import texttospeech
from google.cloud import texttospeech_v1
import PyPDF2

os.environ['GOOGLE_APPLICATION_CREDENTIALS']="text_speech.json"

# creating a pdf file object
pdfFileObj = open('Kvitto.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
# print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
print(pageObj.extractText())

# closing the pdf file object
pdfFileObj.close()

client=texttospeech_v1.TextToSpeechClient()

text='''this is the first time iam trying out this google api'''

synthensis_input=texttospeech_v1.SynthesisInput(text=text)



"""
Method #1
"""
voice1=texttospeech_v1.VoiceSelectionParams(
    language_code='en-US',
    ssml_gender=texttospeech_v1.SsmlVoiceGender.MALE
)
"""
Method #2
"""
voice2=texttospeech_v1.VoiceSelectionParams(
name="es-ES-Standard-B",
language_code="es-ES"
)
# print(client.list_voices())

"""
Output
"""
audio_config=texttospeech_v1.AudioConfig(
    audio_encoding=texttospeech_v1.AudioEncoding.MP3
)

response=client.synthesize_speech(
    input=synthensis_input,
    voice=voice1,
    audio_config=audio_config
)
response2=client.synthesize_speech(
    input=synthensis_input,
    voice=voice2,
    audio_config=audio_config
)

with open('audio file1.mp3','wb')as output1:
    output1.write(response.audio_content)

with open('audio file1.mp3','wb')as output2:
    output2.write(response2.audio_content)