## Created the 26/02/2019
## By Quentin BEDENEAU
## Requirements : PYYAML, argpase, sys, re
##
## This script was created to have a numerical support to work on
## a phpmyadmin database structure (table and columns).
## As the phpmyadmin export in yaml extract all the data, I need to remove all
## data and only keep the key name (representing the columns name of a table)

try:
    import yaml
except Exception as e:
    print("The library Yaml is not available. please download it before running this script")
import argparse, sys, re, os

# Argument creation
parser = argparse.ArgumentParser()
parser.add_argument("input", help="the yaml input file")
parser.add_argument("databasename", help="the database name")
parser.add_argument("--output", help="the directory where csv will be exported")
args = parser.parse_args()

## First step is to modify the extract because the table name is a YAML comment
with open(args.input,'r') as stream:
    with open("text.txt",'w') as temp:
        for line in stream:
            match = re.compile("# "+args.databasename+"(.)*").search(line)
            if match:
                string = match[0]+":"
                # if we have a match we keep the string except the 2 first character
                temp.write(string[2:]+"\n")
            else:
                temp.write(line)

## Second step is to transform the YAML file to a csv
with open("text.txt",'r') as stream:
    data = yaml.load(stream)
    for x in data:
        with open(x+".csv",'w') as file:
            print(list(data[x][0].keys()),file=file)

## Clean the temporary file
os.remove("text.txt")
