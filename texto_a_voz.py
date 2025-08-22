import nltk , os
from newspaper import Article
from gtts import gTTS 
from pydub import AudioSegment

#nltk.download('punkt')
#nltk.download('punkt_tab')
os.makedirs("audios", exist_ok=True)
os.chdir(r'C:\Users\Pc\Desktop\proyectos\texto_a_voz')
url='https://ve.scielo.org/scielo.php?pid=S0378-18442005001000004&script=sci_arttext'
article=Article(url)

#obtengo el texto de la url
article.download()
article.parse()
texto=article.text

#creo dos listas, una con las oraciones del texto separadas
#la otra vacia para llenarla con fragmentos de texto
oraciones= nltk.sent_tokenize(texto, language='spanish')
oraciones_copia=oraciones[:]
fragmentos=[]

#me creo cada fragmento (conjunto de varias oraciones,que no supere 200 caracteres)
while oraciones_copia:
    fragmento=''
    for oracion in oraciones_copia:
        fragmento=fragmento+oracion
        oraciones_copia.remove(oracion)
        if len(fragmento)>200:
            break
    fragmentos.append(fragmento)

#creo un archivo mp3 por cada fragmento
i=0
for fragmento in fragmentos:
    i+=1
    gtts1=gTTS(text=fragmento,lang='es')
    gtts1.save(f'audios/archivo{i}.mp3')

#mezclo todos los audios en uno solo llamado final.mp3
combinado=AudioSegment.empty()
for i in range(1,len(fragmentos)+1):
    ruta=rf'C:\Users\Pc\Desktop\proyectos\texto_a_voz\audios\archivo{i}.mp3'
    audio=AudioSegment.from_mp3(ruta)
    combinado=combinado+audio
combinado.export('audios/final.mp3', format='mp3')

#elimino todos los audios temporales
for i in range(1,len(fragmentos)+1):
    os.remove(f'audios/archivo{i}.mp3')

print('Ya esta listo el archivo final con todo el texto convertido a mp3.')