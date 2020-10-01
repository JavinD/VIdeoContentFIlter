import os
import speech_recognition as sr
import youtube_dl
import pydub

parameter = {
    'format': 'bestaudio/best',
    'outtmpl':'\\%(input)s.%(ext)s',
    'postprocessors':[{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192', 
    }],
}

youtube = youtube_dl.YoutubeDL(parameter)
youtube.download(['https://www.youtube.com/watch?v=BiQiq1xxx44'])

sound = pydub.AudioSegment.from_mp3("NA.mp3")
sound.export("output.wav", format="wav")

r = sr.Recognizer()

PATH = 'output.wav'

with sr.AudioFile(PATH) as source:
    audio = r.record(source)
    
    data = r.recognize_google(audio) 
    print(data)

# This Base Bad Words List is provided free by: Free Web Headers – www.freewebheaders.com
# URL: https://www.freewebheaders.com/full-list-of-bad-words-banned-by-google/
    
forbidden_words = ['anal ','anus ','arse ','ass ','ass fuck ','ass hole ','assfucker ','asshole ','assshole ','bastard ','bitch ','black cock ',                     'bloody hell ','boong ','cock ','cockfucker ','cocksuck ','cocksucker ','coon ','coonnass ','crap ','cunt ','cyberfuck ',                     'damn ','darn ','dick ','dirty ','douche ','dummy ','erect ','erection ','erotic ','escort ','fag ','faggot ','fuck','Fuck off ',                     'fuck you ','fuckass ','fuckhole ','god damn ','gook ','hard core ','hardcore ','homoerotic ','hore ','lesbian ','lesbians ',                     'mother fucker ','motherfuck ','motherfucker ','negro ','nigger ','orgasim ','orgasm ','penis ','penisfucker ','piss ','piss off ',                     'porn ','porno ','pornography ','pussy ','retard ','sadist ','sex ','sexy ','shit ','slut ','son of a bitch ','suck ','tits ','viagra ',                     'whore ','xxx ']

for i in range (len(forbidden_words)) :
    if(data.find(forbidden_words[i])) != -1 :
        print('ur video contains "{}" word'.format(forbidden_words[i]))