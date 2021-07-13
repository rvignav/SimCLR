import pandas as pd
import csv

csv_file = open('trainLabels.csv', mode='r')
d = csv.DictReader(csv_file)

fname = []
label = []
one_hot = []

for row in d:
    fname.append('data/train/' + row['image'] + '.jpeg')
    l = int(row['level'])
    label.append(l)
    arr = [0, 0, 0, 0, 0]
    arr[l] = 1
    one_hot.append(arr)

df = pd.DataFrame({"filename": fname, "class_label": label, "class_one_hot": one_hot})
df.to_pickle("df.pickle")

# Check pickle file
import pandas as pd
df = pd.read_pickle("df.pickle")
print(df.head())