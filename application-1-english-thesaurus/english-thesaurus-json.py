import json
import difflib

with open('./application-1-english-thesaurus/data.json') as definitions_file:
  definitions = json.load(definitions_file) 

def get_definition(word):
  word = word.strip()
  if word in definitions:
    return format_response(word)
  elif word.upper() in definitions:
    return format_response(word.upper())
  elif word.lower() in definitions:
    return format_response(word.lower())
  elif word.title() in definitions:
    return format_response(word.title())
  else:    
    print("The word \"" + word + "\" doesn't exist.")
    
    closest_matching_words = difflib.get_close_matches(word, definitions.keys())
    for close_matching_word in closest_matching_words:
      print("Did you mean " + close_matching_word + "? ")
      confirmation = ""
      while confirmation not in {"Y", "N"}:
        confirmation = input("Please type Y or N to confirm: ")      
      
      if confirmation == "Y":
        return format_response(close_matching_word)
    
    return "The word doesn't exist. Please double check it."

def format_response(word):
  formatted_response = ""
  for definition_index, definition in enumerate(definitions[word]):
    formatted_response += str(definition_index + 1) + ". " + definition + "\n"
  return formatted_response

word = input("Enter word: ")

definition = get_definition(word)

print(definition)