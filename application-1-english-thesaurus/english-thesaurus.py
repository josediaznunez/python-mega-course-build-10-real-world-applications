import json
import difflib

with open('./application-1-english-thesaurus/data.json') as definitions_file:
  definitions = json.load(definitions_file) 

def get_definition(word):
  word_formatted = word.strip().lower()
  if word_formatted in definitions:
    return definitions[word_formatted]
  else:
    closest_matching_word = difflib.get_close_matches(word_formatted, definitions.keys())[0]
    confirmation = "CONFIRMATION_DEFAULT"
    while confirmation not in ["N", "Y"]:
      if confirmation != "CONFIRMATION_DEFAULT":
        confirmation = input("Please type Y or N to confirm: ")
      else:
        confirmation = input(
          "The word \"" + word + "\" doesn't exist. " +
          "Did you mean " + closest_matching_word + "? " + 
          "Please type Y or N to confirm: "
        )
    
    if confirmation == "Y":
      return definitions[closest_matching_word]
    else:
      return "The word doesn't exist. Please double check it."

word = input("Enter word: ")

definition = get_definition(word)

print(definition)