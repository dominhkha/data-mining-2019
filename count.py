
# f=open("clean_data.txt")
import pandas as pd 
contents = pd.read_csv("clean_data.csv")
contents=contents['label'].values
print(len(contents))
# f= open("agedetector_team14_solution.result.txt")
# contents=f.readlines()
cate_dict={'__label__18-24':0,'__label__45-54':0, '__label__25-34':0,'__label__35-44':0,'__label__55+':0}

for i in contents:
    cate_dict[i.strip()]+=1

print(cate_dict)