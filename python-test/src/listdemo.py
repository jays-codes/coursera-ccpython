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