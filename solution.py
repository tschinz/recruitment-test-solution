import pandas as pd
from plotly.offline import plot
import plotly.io as pio
import plotly.figure_factory as ff

# Load data into a dataframe
filename = "Sample Data.csv"
df = pd.read_csv(filename, delimiter=";", decimal=",")

# Sample_ID 13 missing

# Ignore Sample_ID 42 with wrong value
df.drop(df.index[41], inplace=True)

# Find NaN Values and drop them (found in Sample_ID 50)
df.dropna(inplace=True)

# Find duplicated Rows and drop them (none found)
df.drop_duplicates(inplace=True)

# Calculate multiplication and sum
df["VAL_A * VAL_B"] = df["VAL_A"] * df["VAL_B"]
df["VAL_C + VAL_D"] = df["VAL_C"] + df["VAL_D"]

# Create distribution plots
hist_data = [df["VAL_A * VAL_B"], df["VAL_C + VAL_D"]]
group_labels = ["VAL_A * VAL_B", "VAL_C + VAL_D"]
fig = ff.create_distplot(hist_data, group_labels)
fig['layout'].update(title="Histogram of " + filename)

# Save as html and png
plot(fig, filename="histogram_of_sample_data.html")
pio.write_image(fig, "histogram_of_sample_data.png")