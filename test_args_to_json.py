import unittest
from args_to_json import extract_arguments, list_to_json
import os
import json

class TestArgsToJson(unittest.TestCase):
  def test_extract_arguments_basic(self):
    columns = ["col1:int", "col2;string%nullable"]
    expected_output = [
      {"column": "col1", "type": "int", "nullable": False},
      {"column": "col2", "type": "string", "nullable": True}
    ]
    self.assertEqual(extract_arguments(columns), expected_output)
  
  def test_extract_arguments_invalid_format(self):
    columns = ["col1:string:nullable:extra", "col2", ""]
    with self.assertRaises(ValueError):
      extract_arguments(columns)

  def test_extract_arguments_default_nullable(self):
    columns = ["col1:int"]
    expected_output = [{"column": "col1", "type": "int", "nullable": False}]
    self.assertEqual(extract_arguments(columns), expected_output)

  def test_list_to_json(self):
    json_list = [{"column": "col1", "type": "int", "nullable": False}]
    list_to_json(json_list)
    
    with open('results.json', 'r') as f:
      data = json.load(f)
      self.assertEqual(data, json_list)
    
    os.remove('results.json')

if __name__ == "__main__":
  unittest.main()