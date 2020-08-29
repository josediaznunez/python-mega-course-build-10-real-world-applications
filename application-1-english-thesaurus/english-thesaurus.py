
import json

with open('./application-1-english-thesaurus/data.json') as definitions_file:
  definitions = json.load(definitions_file)

def get_definition(word):
  return definitions[word]

word = input("Enter word: ")

definition = get_definition(word)

print(definition)