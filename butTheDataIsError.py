import pandas as pd

# File path
file_path = "tokopdi266775.csv"

# Read the skipped lines from the Excel file
df_skipped = pd.read_excel(file_path)

# Process the skipped lines and create a list of dictionaries
parsed_data = []
for _, row in df_skipped.iterrows():
    try:
        line_data = row["Skipped Lines"].strip().split(",")
        if len(line_data) >= 3:  # Adjust the number of expected fields here
            entry = {
                "EMAIL": line_data[0].strip(),
                "NAME": line_data[1].strip(),
                "Phone": "",
                "DOB": "",
                "SHA384": "",
            }
            if line_data[2].strip().isnumeric():
                entry["Phone"] = line_data[2].strip()
            else:
                entry["DOB"] = line_data[2].strip()
            if len(line_data) > 3:
                if line_data[3].strip().isnumeric():
                    entry["Phone"] = line_data[3].strip()
                else:
                    entry["DOB"] = line_data[3].strip()
            if len(line_data) > 4:
                entry["SHA384"] = line_data[4].strip()
            parsed_data.append(entry)
    except Exception:
        continue

# Create a DataFrame from the parsed data
df_processed = pd.DataFrame(parsed_data)

# Sort the DataFrame based on the presence of the email field
df_sorted = df_processed[df_processed["EMAIL"].str.contains("@")]

# Export the processed DataFrame to an Excel file
df_sorted.to_excel("tokopedia_processedagain.xlsx", index=False)
