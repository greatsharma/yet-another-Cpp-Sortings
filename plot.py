import argparse
import pandas as pd
import matplotlib.pyplot as plt


ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input', required=True,
                help='path to input csv file')
ap.add_argument('-o', '--output', required=True,
                help='path to output image')
args = vars(ap.parse_args())


df = pd.read_csv(args["input"], names=["size", "comp"])

plt.scatter(df["size"], df["comp"])
plt.xlabel("size of array")
plt.ylabel("no. of comparisons")

sort_type = args["output"].split("_")[2].title()
fig_title = f"size v/s comparison, {sort_type}-Sort"
plt.title(fig_title)
plt.savefig(args["output"])
