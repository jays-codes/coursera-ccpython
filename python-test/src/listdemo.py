#list demo

x = [1, 2, 3, 4, 5]
print(x)

#print the type of x
print("type is:", type(x))

#tuple demo. function to convert seconds to 
#Hours, Minutes and Seconds
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return hours, minutes, seconds

# Example usage
total_seconds = 3661
toops = convert_seconds(total_seconds)
print(f"{total_seconds} seconds is equal to {toops[0]} hours, {toops[1]} minutes, and {toops[2]} seconds")
print("type is:", type(toops))


def skip_elements(elements):
    # Initialize variables
    new_list = []
    i = 0

    # Iterate through the list
    for element in elements:
        # Does this element belong in the resulting list?
        if i % 2 == 0:
            # Add this element to the resulting list
            new_list.append(element)
        # Increment i
        i += 1

    return new_list



#The format of the input variable “address_string” is: numeric house number, 
#followed by the street name which may contain numbers and could be several 
# words long (e.g., "123 Main Street", "1001 1st Ave", 
# or "55 North Center Drive"). 

#Complete the string methods needed in this function so that input like 
# "123 Main Street" will produce the output "House number 123 on a street 
# named Main Street". This function should: accept a string through the 
# parameters of the function;
# separate the address string into new strings: house_number and street_name; 
# return the variables in the string 
# format: "House number X on a street named Y". 
def format_address(address_string):


    house_number = ""
    street_name = ""


    # Separate the house number from the street name.
    address_parts = address_string.split()
    
    for address_part in address_parts:
       # Complete the if-statement with a string method.  
       if address_part.isnumeric():
         house_number = address_part
       else:
         street_name += address_part + " "
    # Remove the extra space at the end of the last "street_name".
    street_name = street_name.strip()
 
    # Use a string method to return the required formatted string.
    return "House number {} on a street named {}".format(house_number, street_name)


print(format_address("123 Main Street"))
# Should print: "House number 123 on a street named Main Street"


print(format_address("1001 1st Ave"))
# Should print: "House number 1001 on a street named 1st Ave"


print(format_address("55 North Center Drive"))
# Should print "House number 55 on a street named North Center Drive"



def string_words(string):
    # Complete the return statement using both a string operation and 
    # a string method in a single line.
    return len(string.split())


print(string_words("Hello, World")) # Should print 2
print(string_words("Python is awesome")) # Should print 3
print(string_words("Keep going")) # Should print 2
print(string_words("Have a nice day")) # Should print 4


def alphabetize_lists(list1, list2):

    # Initialize a new list.
    new_list = [] 
    # Combine the lists.
    list1.extend(list2)
    
    # Sort the combined lists.
    new_list = sorted(list1) 
    # Assign the combined lists to the "new_list".
    return new_list

Aniyahs_list = ["Jacomo", "Emma", "Uli", "Nia", "Imani"]
Imanis_list = ["Loik", "Gabriel", "Ahmed", "Soraya"]


print(alphabetize_lists(Aniyahs_list, Imanis_list))
# Should print: ['Ahmed', 'Emma', 'Gabriel', 'Imani', 'Jacomo', 'Loik', 'Nia', 'Soraya', 'Uli']


def squares(start, end):
    # Create the required list comprehension.
    return [ x**2 for x in range(start, end+1) ]

print(squares(2, 3)) # Should print [4, 9]
print(squares(1, 5)) # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


def countries(countries_dict):
    result=""
    for continent,countries in countries_dict.items():
        # for each countries list, convert the list to a string and assign to result
        #when result is printed, the value should be in its own line, 
        # each line enclosed in a pair of square brackets, 
        # and the countries enclosed in single quotes and separated by a comma and a space.
        result += "[" + ", ".join(["'"+country+"'" for country in countries]) + "]\n"
    return result

# Example usage
print(countries({"Africa": ["Kenya", "Egypt", "Nigeria"], "Asia":["China", "India", "Thailand"], "South America": ["Ecuador", "Bolivia", "Brazil"]}))



def combine_guests(guests1, guests2):
  # Use a dictionary method to combine the dictionaries.
  guests2.update(guests1)
  return guests2

Ricks_guests = { "Adam":2, "Camila":3, "David":1, "Jamal":3, "Charley":2, "Titus":1, "Raj":4}
Tessas_guests = { "David":4, "Noemi":1, "Raj":2, "Adam":1, "Sakira":3, "Chidi":5}

print(combine_guests(Ricks_guests, Tessas_guests))
# Should print:
# {'David': 1, 'Noemi': 1, 'Raj': 4, 'Adam': 2, 'Sakira': 3, 'Chidi': 5, 'Camila': 3, 'Jamal': 3, 'Charley': 2, 'Titus': 1}


def setup_gradebook(old_gradebook):
    # Use a dictionary method to create a new copy of the "old_gradebook".
    new_gradebook = old_gradebook.copy()
    # Complete the for loop to iterate over the new gradebook. 
    for student in new_gradebook:
        # Use a dictionary operation to reset the grade values to 0.
        new_gradebook[student] = 0
    return new_gradebook

fall_gradebook = {"James": 93, "Felicity": 98, "Barakaa": 80}
print(setup_gradebook(fall_gradebook))
# Should output {'James': 0, 'Felicity': 0, 'Barakaa': 0}

car_make = "Lamborghini"
print(car_make[3:-5])
print(car_make[-4:])
print(car_make[:7])

music_genres = ["rock", "pop", "country"]
music_genres.append("blues")
print(music_genres)

host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
host_addresses.keys()
print(host_addresses.keys())