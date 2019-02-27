# Description
This script was created to have a numerical support to work on a phpmyadmin database structure (table and columns). As the phpmyadmin export in yaml extract all the data, I need to remove all data and only keep the key name (representing the columns name of a table)
# How to
usage: extractyamlstruct.py [-h] [--output OUTPUT] input databasename

positional arguments:
  input            the yaml input file
  databasename     the database name

optional arguments:
  -h, --help       show this help message and exit
  --output OUTPUT  the directory where csv will be exported
