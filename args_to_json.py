import argparse
import json
import sys

# TODO order check
# TODO null check
# TODO type validation

# set arguments
parser = argparse.ArgumentParser()
parser.add_argument("-col", "--columns", help="Column details", action='append', nargs='+')
args = parser.parse_args()

def extract_arguments():
  """
  Extracts arguments from the 'args' object and converts them into a JSON file.
  
  Returns:
    json_list (list): The list of extracted arguments in JSON format.
  """

  cols = args.columns
  json_list = []

  for col in cols:    
    properties = str(col[0]).split(':')

    # check if the column is nullable
    if (len(properties) == 3):
      if (properties[2] == 'nullable'):
        properties[2] = True
      else:
        properties[2] = False
    else:
      properties.append(False)
    
    col_dict = {
      "column": properties[0],
      "type": properties[1],
      "nullable": properties[2]
    }

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
  
  with open('results.json', 'w') as fout:
    json.dump(json_list , fout)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    json_list = extract_arguments()
    list_to_json(json_list)
  else:
    print("No arguments are passed!")