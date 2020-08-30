import json
import difflib

with open('./application-1-english-thesaurus/data.json') as definitions_file:
  definitions = json.load(definitions_file) 

def get_definition(word):
  word_formatted = word.strip().lower()
  if word_formatted in definitions:
    return definitions[word_formatted]
  else:    
    print("The word \"" + word + "\" doesn't exist.")
    
    closest_matching_words = difflib.get_close_matches(word_formatted, definitions.keys())
    for close_matching_word in closest_matching_words:
      print("Did you mean " + close_matching_word + "? ")
      confirmation = ""
      while confirmation not in {"Y", "N"}:
        confirmation = input("Please type Y or N to confirm: ")      
      
      if confirmation == "Y":
        return definitions[close_matching_word]
    
    return "The word doesn't exist. Please double check it."

word = input("Enter word: ")

definition = get_definition(word)

print(definition)