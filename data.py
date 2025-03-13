import pandas as pd

# Creating the DataFrame with example ASU academic calendar data
data = {
    "Event": [
        "Classes Begin",
        "Last Day to Register",
        "Drop Deadline",
        "Tuition fee payment deadline",        
    ],
    "Session A": [
        "Jan 13, 2025",
        "Jan 14, 2025",
        "Jan 19, 2025",
        "Feb 25, 2025"
    ],
    "Session B": [
        "March 17, 2025",
        "March 18, 2025",
        "March 23, 2025",
        "Feb 25, 2025"
    ],
    "Session C": [
        "Jan 13, 2025",
        "Jan 18, 2025",
        "Jan 19, 2025",
        "Feb 25, 2025"
    ]
}

# Convert dictionary to Pandas DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)