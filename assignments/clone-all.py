import os
import pandas as pd

repo_df = pd.read_csv('repos.csv')

for i, url in enumerate(repo_df["Repository URL"]):
    folder = url.split("/")[-1].replace(".git", "")

    os.system("git clone " + url)
    os.system(
        "mv " + folder + " " +
        repo_df["Last Name"][i] +
        "-" +
        repo_df["First Name"][i])
