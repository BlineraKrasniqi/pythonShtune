import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv('avgIQpercountry.csv')
#
# avg_iq_continent = df.groupby('Continent') ['Avarage IQ'].mean()
#
# plt.figure(figsize=(10.6))
#
# avg_iq_continent(kind='line', marker='o', color='skyblue')
#
# plt.title('Average IQ per Continent')
# plt.xlabel('Continent')
# plt.ylabel('Average IQ')
#
# plt.grid(axis='both', linestyle='--', alpha= '0.7')
# plt.show()



# df = pd.read_csv('avgIQpercountry.csv')
#
# filtered_df = df[df['Avarage IQ'] >=100]
# filtered_df = filtered_df.sort_values(by="Average IQ", ascending=False)
#
# print(filtered_df)
#
# plt.figure(figsize=(14,8))
#
# bars = plt.bar(filtered_df['Country'], filtered_df['Average IQ'], color= "skyblue")
#
# plt.title("Average IQ by Country (IQ >= 100)", fontsize=16)
#
# plt.xlabel('Country', fontsize=14)
# plt.ylabel('Average IQ', fontsize=14)
#
#
#
#
# plt.xticks(rotation=90, fontsize=10)
# plt.yticks(fontsize=14)
#
# plt.grid(axis= 'y', linestyle='--', alpha= 0.8)
# plt.bar_label(bars, fmt='%.2f', fontsize=10, color="black")
#
# plt.tight_layout
#
# plt.show()