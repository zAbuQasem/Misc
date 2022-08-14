#!/usr/bin/env python3

#/**
# SecretsConverter is a tiny tool used to convert data in secrets file from plain
# text into base64 encoded data.
# Codedby: zeyad abulaban
#
# Options:
#           python3 SecretsConverter.py -f <SecretsFile.yml> -o secrets.yml
#    -f : input filename
#    -o: output filename (default name is secrets.yml) 
#**/


import yaml
from sys import stdout
import argparse
from base64 import b64encode, b64decode


class SecretsConverter:
    def __init__(self, args):
        self.file = args.file
        self.output = args.output

    def loadfile(self):
        try:
            file = open(self.file, "r")
            loaded_file = yaml.load(file, Loader=yaml.Loader)
            file.close()
            return loaded_file
        except yaml.YAMLError as err:
            print(f"[!] Error Malformed Yaml file: {err}")
            exit(1)

    def converter(self):
        try:
            file = self.loadfile()
            for key, value in file['data'].items():
                file['data'][key] = b64encode(value.encode()).decode()
            return file
        except Exception as e:
            print(e)


    def main(self):
        try:
            output = self.converter()
            with open(self.output, "w") as outputfile:
                yaml.dump(output, outputfile, sort_keys=False)
                outputfile.close()
            # Priting the Output to console
            yaml.safe_dump(output, stdout,sort_keys=False)
        except Exception as err:
            print(err)

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        options = parser.add_argument_group("Options")
        options.add_argument('-f', '--file', help='Input yaml file', required=True)
        options.add_argument('-o', '--output', help='Output file name',default="secrets.yml") 
        args = parser.parse_args()
        Runner = SecretsConverter(args)
        Runner.main()
    except KeyboardInterrupt:
        exit(1)
