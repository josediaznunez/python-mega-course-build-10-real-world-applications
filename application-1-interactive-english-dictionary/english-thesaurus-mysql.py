import mysql.connector
import difflib

connection = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)
cursor = connection.cursor()

def get_all_words():
  all_words_list = []
  cursor.execute("SELECT DISTINCT Expression FROM Dictionary")
  all_words_tuples = cursor.fetchall()
  for word_tuple in all_words_tuples:
    all_words_list.append(word_tuple[0])
  return all_words_list

all_words = get_all_words()

def get_definition(word):
  word = word.strip()

  definitions = get_results(word)
  if definitions:
    return format_response(definitions)

  definitions = get_results(word.upper())
  if definitions:
    return format_response(definitions)
  
  definitions = get_results(word.lower())
  if definitions:
    return format_response(definitions)
  
  definitions = get_results(word.title())
  if definitions:
    return format_response(definitions)
  
  print("The word \"" + word + "\" doesn't exist.")

  closest_matching_words = difflib.get_close_matches(word, all_words)
  for close_matching_word in closest_matching_words:
    print("Did you mean " + close_matching_word + "? ")
    confirmation = ""
    while confirmation not in {"Y", "N"}:
      confirmation = input("Please type Y or N to confirm: ")      
    
    if confirmation == "Y":
      definitions = get_results(close_matching_word)
      return format_response(definitions)

  return "The word doesn't exist. Please double check it."

def get_results(word):
  cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
  return cursor.fetchall()

def format_response(definitions):
  formatted_response = ""
  for definition_index, definition in enumerate(definitions):
    formatted_response += str(definition_index + 1) + ". " + definition[1] + "\n"
  return formatted_response

word = input("Enter word: ")

definition = get_definition(word)

print(definition)