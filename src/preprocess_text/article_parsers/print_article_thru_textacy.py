# coding: utf-8
import textacy
myjson = textacy.fileio.read_json("/opt/nlp_shared/data/news_articles/webhose_english_dataset/news_0000124.json")
content, metadata = textacy.fileio.utils.split_record_fields(myjson, "text")
for line in content:
    print(line)
    
