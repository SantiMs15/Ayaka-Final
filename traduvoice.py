from google_trans_new import google_translator
import speech_recognition as sr
import pyttsx3

a=pyttsx3.init()
r=sr.Recognizer()

with sr.Microphone() as source:
    print('Señor/a la escucho :v')
    r.adjust_for_ambient_noise(source,duration=1)
    print('No le entiendo nada... :d')
    sonido=r.listen(source,timeout=1)
    print('Creo que ya entendí :D')
try:
    print('Estoy pensando ...')
    idio_entrada=r.recognize_google(audio,language='es')
except Exception as xd:
    print(xd)


def traduccion():
    idio_salida=input('de')
    t=google_translator()
    o=t.translate(str(result),d=str(idio_salida))
    print(o)
    a.say(str(o))
    a.runAndWait()
traduccion()    
