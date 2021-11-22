import sys
import yaml
import pprint

yaml_filename = sys.argv[1]

with open(yaml_filename, "r") as open_file:
	file_contents = yaml.safe_load(open_file)

pprint.pprint(file_contents)