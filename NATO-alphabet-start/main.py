student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}
#
# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
#
# # read a file with python use open()
# with open("nato_phonetic_alphabet.csv") as datapy:
#     py = datapy.read()

# read a csv with pandas use .read_csv
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)

nato_dict = {row.letter:row.code for index, row in data.iterrows()}
print(nato_dict)

word = input("Enter a word:\n").upper()
output = [nato_dict[letter] for letter in word]
print(output)








# nato_list = {key:value for letter, code in pandas.DataFrame(contents).iterrows()}
# print(nato_list)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

