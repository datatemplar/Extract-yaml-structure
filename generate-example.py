## script to generate the example.yml
##
import os, sys
with open('file.yml','w') as file:
    file.write("%YAML 1.1\n---\n")
    for i in range (1,11):
        file.write("database.tablenumb"+str(i)+":\n")
        for j in range(1,101):
            file.write("-\n")
            file.write("  tag1: tagvalue"+str(j)+"\n")
            file.write("  tag2: "+str(j)+"\n")
