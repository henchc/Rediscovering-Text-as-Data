import os
import pandas as pd

repo_df = pd.read_csv('repos.csv')

for i in range(len(repo_df)):

    folder = repo_df["Last Name"][i] + "-" + repo_df["First Name"][i]
    os.system("cd " + folder + " &&" + " git pull")
    print(i + 1, folder)
    print()
