from gensim.summarization.summarizer import summarize #only a 4 sentence summary
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.stemmers import Stemmer
from sumy.nlp.tokenizers import Tokenizer
from sumy.utils import get_stop_words
import nltk

LANGUAGE = "english"
SENTENCES = 2
#nltk.download('punkt') Do not download again

def summary(str=''):
   #return summarize(str)
   parser = PlaintextParser.from_file('transcript.txt', Tokenizer(LANGUAGE))
   stemmer = Stemmer(LANGUAGE)
   summarizer = Summarizer(stemmer)
   summarizer.stop_words = get_stop_words(LANGUAGE)

   for sentence in summarizer(parser.document, SENTENCES):
      print(sentence)