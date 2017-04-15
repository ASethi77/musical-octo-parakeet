import spacy
nlp = spacy.load('en')

doc = nlp.tokenizer(u'Hello, world. Natural Language Processing in 10 lines of code.')
nlp.tagger(doc)
nlp.parser(doc)
nlp.entity(doc)