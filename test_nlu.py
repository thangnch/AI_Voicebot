from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter


from pyvi import ViTokenizer, ViPosTagger

print(ViTokenizer.tokenize("Trường đại học bách khoa hà nội"))
print(ViPosTagger.postagging(ViTokenizer.tokenize("Tôi muốn đi chơi công viên")))

import feedparser

NewsFeed = feedparser.parse("https://www.shb.com.vn/feed/")
entry = NewsFeed.entries[1]

print(entry.title)