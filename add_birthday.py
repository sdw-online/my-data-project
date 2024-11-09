import pandas as pd

# 1. Load the CSV file
birthdays_df = pd.read_csv('birthdays.csv')


# 2. Print the contents of the CSV file
print("Current Birthdays in the calendar:")
print(birthdays_df)


# 3. Add a new birthday to the calendar
new_birthday = {'Name': 'Matthew', 'Date': '2024-12-25'}
birthdays_df = birthdays_df.append(new_birthday, ignore_index=True)


# 4. Save the updated file back to the CSV
birthdays_df.to_csv('birthdays.csv', index=False)
print("Successfully added Matthew's birthday to birthdays.csv and saved the updated file.")
