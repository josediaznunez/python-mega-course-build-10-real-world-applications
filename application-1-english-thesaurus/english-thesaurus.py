
import json

def get_definition(word):
  with open('./application-1-english-thesaurus/data.json') as definitions_file:
    definitions = json.load(definitions_file)
  return definitions[word]

print(get_definition("rain"))