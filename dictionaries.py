##allow us to store infos in pairs
#we can create a dictionary with curly brackers
# and store the months of the year#
monthsOfTheYear= {
    "Jan" :"January",
    "Feb" : "Febrauary",
    "Mar" : "March",
    "Apr" : "April",
     "May" :"May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
     "Sept" :"September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
}
#to access a specific value, you refer to the key
print(monthsOfTheYear["Dec"])
#or print(monthsOfTheYear.get("Dec"))
#when the key isn't there, it prints none
#or you can tell it to print a default value
print(monthsOfTheYear.get("Sept", "NOT A KEY"))
print(monthsOfTheYear.get("Set", "NOT A KEY"))
##exercise
# Create a new dictionary, where
# "John", "Jane" and "Gerard" are keys and numbers are values.
phone_book = {"John": 123, "Jane": 234, "Gerard": 345}
print(phone_book)

# Add a new item to the dictionary.
phone_book["Jill"] = 345
print(phone_book)

# Remove a key-value pair from phone_book.
del phone_book["John"]

# Add Jared's number to the phone book

# Remove Gerard's number from the phone book

print(phone_book)
print(???)
