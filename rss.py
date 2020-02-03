import io, os, sys, types, shutil, json
from datetime import datetime

# Servers can sometimes get upset if you don't tell them
# where to look for feedparser and Goose, considre adding
# sys.path.inser(0,//PATH TO PACKAGES//)

import feedparser, operator
from goose3 import Goose

import spacy
from spacy.lang.en import English
from spacy.parts_of_speech import NOUN


## take the url of a webpage that should be an article
## return the article and its metadata
def extractArticle(url):
    from goose3.configuration import Configuration
    config = Configuration()
    # config.local_storage_path = tmp_dir
    return Goose(config).extract(url=url)

## bump up count of word in wordict
def addCount(wordict,word):
    if word not in wordict:
        wordict[word] = 1
    else:
        wordict[word] += 1


def build(rss):
    # analyze the feed
    feed = feedparser.parse(rss)
    if (feed['feed'] == {}): #could not parse properly
        print("Error: input does not yield a viable rss feed")
        sys.exit(0);
    # prepare spacy and entity metadata
    nlp = English()
    is_noun = lambda dok: tok.pos == NOUN
    entities = ['People','Nationalities, Organizations, Religions, and Political Parties','Facilities','Organizations','Geo-Political Entities','Locations','Products','Events','Works of Art','Laws','Languages','Dates','Times','Percents','Money','Quantities','Ordinal Numbers','Cardinal Numbers']
    entity_nums = [28061,1499631,164860,202115,85248,87482,86554,81537,1499633,39247,83611,55719,8206,112430,17764,341856,1499632,354826]
    # loop through items in feed
    # write a file for each analysis
    for item in feed["items"]:
        # initalize the dictionaries
        #   1 for words, 1 for entities
        wordcount = {}
        value_dicts = dict((x,{}) for x in entity_nums)
        # extract article from url and process with spacy
        body = extractArticle(item["link"]).cleaned_text
        tokens = nlp(body)
        # add words to dictionary
        for tok in tokens:
            if is_noun(tok):
                addCount(wordcount, tok.orth_)
        # format data for printing to comply with html file
        articleTitle = item["title"].replace(u"\"", "'")
        articleLink = item["link"]
        articleInfo = {'title': articleTitle, 'link': articleLink}
        data = [{'name': 'Articles', 'children': [articleInfo]}]
        nounInfo = [{'name': k, 'size': v} for k,v in wordcount.items()]
        data.append({'name': 'Nouns', 'children': nounInfo})
        data += [{'name': entities[entity_nums.index(d)], 'children' : [{'name': k, 'size': v} for k,v in c.items()]} for d,c in value_dicts.items()]
            # f.write(json.dumps(data))
        print(data)
        print("------------------------")



def main(argv):
    if len(argv) != 2:
        print("Error: impropert input length")
        return
    else:
        build(sys.argv[1])

if __name__ == "__main__":
    main(sys.argv)
