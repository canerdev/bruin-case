import argparse
import json
import sys
import re

# TODO order check
# TODO null check
# TODO type validation


def extract_arguments(columns):
  """
  Extracts arguments from the 'args' object and converts them into a JSON file.
  
  Returns:
    json_list (list): The list of extracted arguments in JSON format.
  """

  json_list = []

  for col in columns:
    col = re.sub('[^0-9a-zA-Z]+', ':', col)
    properties = col.split(':')

    # check the format
    if len(properties) == 1 or len(properties) > 3:
      raise ValueError("Argument format is incorrect. Expected format: <column name>:<column type>:<nullable or not>")

    # check if the column is nullable
    if (len(properties) == 3):
      if (properties[2] == 'nullable'):
        properties[2] = True
      else:
        properties[2] = False
    else:
      properties.append(False)
    
    # create the dictionary
    col_dict = {
      "column": properties[0],
      "type": properties[1],
      "nullable": properties[2]
    }

    # append the dictionary to the json list
    json_list.append(col_dict)

  return json_list

def list_to_json(json_list):
  """
  Converts a list to JSON format and writes it to a file.
  
  Parameters:
  json_list (list): The list to be converted to JSON format.
  
  Returns:
  None
  """

  if json_list:
    with open('results.json', 'w') as fout:
      json.dump(json_list , fout)

def main():
  # set arguments
  parser = argparse.ArgumentParser()
  parser.add_argument("-col", "--columns", help="Column details", action='append', nargs='+')
  args = parser.parse_args()

  if args.columns:
    columns = [item[0] for item in args.columns]
    json_list = extract_arguments(columns)
    list_to_json(json_list)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    main()
  else:
    raise ValueError("Argument format is incorrect. Expected format: <column name>:<column type>:<nullable or not>")
