# read a csv file, users_in.csv and generate a password for each user
# and write to users_out.csv. Password should be 16 characters long. Each
# record in users_in.csv has the following format: username, password, real_name. 
# password is blank in users_in.csv. Use csv, secrets, subprocess
# from pathlib import Path. Use DictReader and DictWriter.

import csv
import secrets
import subprocess
from pathlib import Path
import bcrypt

# Define the path to the input and output files
cwd = Path.cwd()
input_file = Path("projects/users_in.csv")
output_file = Path("projects/users_out.csv")

try:
    # Open the input file in read mode
    with open(cwd / input_file, "r") as infile, open(cwd / output_file, "w", newline="") as outfile:
        # Create a csv reader and writer object
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        
        # Iterate over each row in the input file
        for row in reader:
            # Generate a random password using secrets module
            password = secrets.token_urlsafe(16)
            # Encrypt the password using bcrypt
            encrypted_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            # Append the generated password to the row
            row["password"] = password
            
            # Comment out the useradd command for Windows compatibility
            # useradd_cmd = [
            #     "/sbin/useradd", 
            #     "-c", row["real_name"], 
            #     "-m",
            #     "-G", "users",
            #     "-p", encrypted_password,
            #     row["username"]
            # ]
            # subprocess.run(useradd_cmd, check=True)
            
            # Write the updated row to the output file
            writer.writerow(row)
        
    # Print a message to indicate the process is complete
    print("Passwords generated and written to users_out.csv")

except Exception as e:
    print(f"An error occurred: {e}")

# End of script
print("End of script")