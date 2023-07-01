import os

with open('countries.txt','r') as file:
    for line in file:
        if line.startswith('Answer') is True:
            with open('cities.txt','a') as f:
                f.write(line)