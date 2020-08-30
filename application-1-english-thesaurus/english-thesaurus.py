
import json

with open('./application-1-english-thesaurus/data.json') as definitions_file:
  definitions = json.load(definitions_file) 

def get_definition(word):
  if word in definitions:
    return definitions[word]
  else:
    return "The word doesn't exist. Please double check it."

word = input("Enter word: ")

definition = get_definition(word)

print(definition)