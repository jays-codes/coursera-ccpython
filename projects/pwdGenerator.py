    # read a csv file, users_in.csv and generate a password for each user
    # and write to users_out.csv. Password should be 16 characters long. Each
    # record in users_in.csv has the following format: username, password, real_name. 
    # password is blank in users_in.csv. Use csv, secrets, subprocess
    # from pathlib import Path. 
    
import csv
import secrets
import subprocess
from pathlib import Path

# Define the path to the input and output files
cwd = Path.cwd()
input_file = Path("projects/users_in.csv")
output_file = Path("projects/users_out.csv")

try:
    # Open the input file in read mode
    with open(cwd / input_file, "r") as file:
        # Create a csv reader object
        reader = csv.reader(file)
        # Read the header row
        header = next(reader)
        # Create a list to store the updated records
        updated_records = [header]
        # Iterate over each row in the input file
        for row in reader:
            # Generate a random password using secrets module
            password = secrets.token_hex(8)
            # Append the generated password to the row
            row[1] = password
            # Append the updated row to the list
            updated_records.append(row)

    # Open the output file in write mode
    with open(cwd / output_file, "w", newline="") as file:
        # Create a csv writer object
        writer = csv.writer(file)
        # Write the updated records to the output file
        writer.writerows(updated_records)

    # Print a message to indicate the process is complete
    print("Passwords generated and written to users_out.csv")

    # Open the output file using the default application (Windows specific)
    subprocess.Popen(["start", str((cwd / output_file).resolve())], shell=True)

except Exception as e:
    print(f"An error occurred: {e}")

# End of script
print("End of script")