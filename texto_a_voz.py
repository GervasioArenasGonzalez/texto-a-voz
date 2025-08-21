from newspaper import Article
import nltk
import gtts 

#nltk.download('punkt')
#nltk.download('punkt_tab')

url='https://ve.scielo.org/scielo.php?pid=S0378-18442005001000004&script=sci_arttext'
article=Article(url)

article.download()
article.parse()
texto=article.text

oraciones= nltk.sent_tokenize(texto, language='spanish')
oraciones_copia=oraciones[:]
fragmentos=[]

while oraciones_copia:
    fragmento=''
    for oracion in oraciones_copia:
        fragmento=fragmento+oracion
        oraciones_copia.remove(oracion)
        if len(fragmento)>200:
            break
    fragmentos.append(fragmento)

print('aura')

