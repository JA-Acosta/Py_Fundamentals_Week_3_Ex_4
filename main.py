'''
>>> JAAR
>>> 8/9/2023
>>> Practicing Fundamentals Program 16
>>> Version 1
'''

'''
>>> Generates a program that takes a csv file containing a list of users and their emails and creates a copy of the csv file that is sorted based on last name.
'''

import csv

def main() :
    data = []
    with open('names.csv', 'r') as csv_file :
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader :
            data.append(row)
    data.sort(key = lambda x : (x["last_name"], x["first_name"] ))
    with open('copy.csv', 'w', newline= '') as csv_copy :
        field_names = ['last_name', 'first_name', 'email']
        csv_writer = csv.DictWriter(csv_copy, fieldnames = field_names)
        csv_writer.writeheader()
        for row in data :
            csv_writer.writerow(row)
if __name__ == "__main__" :
    main()