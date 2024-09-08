#Formatting strings

#string.format()

#positional formatting
print("{0} is the first {1}".format("Jay", "name"))

#keyword formatting
print("{name} is the first {thing}".format(name="Jay", thing="name"))

#formatting expressions

#2 decimal places
result = 2/3
print("{:.2f}".format(result))

#comma separator
num = 1000000
print("{:,}".format(num))

#binary, octal, hexadecimal
print("{0:b} {0:o} {0:x}".format(10))

#padding
print("{:10}".format("test"))

#left, right, center alignment
print("{:<10}".format("test"))
print("{:>10}".format("test"))
print("{:^10}".format("test"))

#fill with *
print("{:*^10}".format("test"))


# Here are the items in the customer's basket. Each item is a tuple
# of (item name, weight, price per pound).
#
basket = [
("Peaches", 3.0, 2.99),
("Pears", 5.0, 1.66),
("Plums", 2.5, 3.99)
]


# Calculate the total price for each item (weight times price per pound)
# and add them up to get a subtotal.
#
subtotal = 0.00
for item in basket:
    fruit, weight, unit_price = item
    subtotal += (weight * unit_price)


# Now calculate the sales tax and total bill.
#
tax_rate = 0.06625# 6.625% sales tax in New Jersey
tax_amt = subtotal * tax_rate
total = subtotal + tax_amt


# Print the receipt for the customer.
#
print("Subtotal:    {:>11}".format("${:.2f}".format(subtotal)))
print("Sales Tax:   {:>11}".format("${:.2f}".format(tax_amt)))
print("Total:       {:>11}".format("${:.2f}".format(total)))


def replace_date(schedule, old_date, new_date):
    new_schedule = schedule.replace(old_date, new_date)
    return new_schedule

print(replace_date("Last year’s annual report will be released in March 2023", "2023", "2024")) 
# Should display "Last year’s annual report will be released in March 2024"
print(replace_date("In April, the CEO will hold a conference", "April", "May")) 
# Should display "In April, the CEO will hold a conference"
print(replace_date("The convention is scheduled for October", "October", "June")) 
# Should display "The convention is scheduled for June"


def replace_ending(sentence, old, new):
    # Check if the old substring is at the end of the sentence 
    if sentence.endswith(old):
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the 
        # end with the new string
        i = len(sentence) - len(old)
        new_sentence = sentence[:i] + new
        return new_sentence

    # Return the original sentence if there is no match
    return sentence

print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"

