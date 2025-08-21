from newspaper import Article
import nltk

#nltk.download('punkt')
#nltk.download('punkt_tab')

url='https://ve.scielo.org/scielo.php?pid=S0378-18442005001000004&script=sci_arttext'
article=Article(url)

article.download()
article.parse()
texto=article.text

oraciones= nltk.sent_tokenize(texto, language='spanish')
