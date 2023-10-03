import pandas as pd

# File path
file_path = "your_file.xlsx"

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
                "Phone": line_data[2].strip() if len(line_data) > 2 else "",
                "DOB": line_data[3].strip() if len(line_data) > 3 else "",
                "SHA384": line_data[4].strip() if len(line_data) > 4 else "",
            }
            parsed_data.append(entry)
    except Exception:
        continue

# Create a DataFrame from the parsed data
df_processed = pd.DataFrame(parsed_data)

# Sort the DataFrame based on the presence of the email field
df_sorted = df_processed[df_processed["EMAIL"].str.contains("@")]

# Export the processed DataFrame to an Excel file
df_sorted.to_excel("output.xlsx", index=False)
