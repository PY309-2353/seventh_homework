import pandas as pd
import matplotlib.pyplot as plt

otzyv = pd.read_table('train.txt', delim_whitespace=True, names=['id', 'label', '3', '4', '5', '6', '7'])

id_and_label = otzyv.loc[:, ['id', 'label']]

min_id = id_and_label['id'].min()
max_id = id_and_label['id'].max()

labels_counter = id_and_label['label'].value_counts(ascending=True)

OBSCENITY = labels_counter[0]
THREAT =  labels_counter[1]
INSULT = labels_counter[2]
NORMAL = labels_counter[3]
total_labels = OBSCENITY + THREAT + INSULT + NORMAL

labels = 'OBSCENITY', 'THREAT', 'INSULT', 'NORMAL'
sizes = [OBSCENITY/100 * total_labels, THREAT/100 * total_labels, INSULT/100 * total_labels, NORMAL/100 * total_labels]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')
plt.show()


print(min_id)
print(max_id)
