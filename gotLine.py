import pandas as pd

# File path
file_path = "tokopdi266775.csv"

# Read the data from the CSV file
parsed_data = []
skipped_lines = []
with open(file_path, "r") as file:
    for line in file:
        try:
            line_data = line.strip().split(",")
            if len(line_data) >= 5:
                entry = {
                    "EMAIL": line_data[0].strip(),
                    "NAME": line_data[1].strip(),
                    "Phone": line_data[2].strip() if len(line_data) > 2 else "",
                    "DOB": line_data[3].strip() if len(line_data) > 3 else "",
                    "SHA384": line_data[4].strip() if len(line_data) > 4 else "",
                }
                parsed_data.append(entry)
            else:
                skipped_lines.append(line.strip())
        except Exception:
            skipped_lines.append(line.strip())

# Create a DataFrame from the parsed data
df = pd.DataFrame(parsed_data)

# Sort the DataFrame based on the presence of the email field
df_sorted = df[df["EMAIL"].str.contains("@")]

# Export the DataFrame to an Excel file
df_sorted.to_excel("tokopedia1.xlsx", index=False)

# Export the skipped lines to a separate Excel file
df_skipped = pd.DataFrame({"Skipped Lines": skipped_lines})
df_skipped.to_excel("tokopedia_skipped.xlsx", index=False)