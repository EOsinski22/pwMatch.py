import argparse
import os

#EOsinski22
#Description
#Simple script to compare the results of a secretsdump.py outputfile to a hashtopolis output file, writes the matching values to a results file
#TODO perform password analysis after results are obtained

parser = argparse.ArgumentParser(description="Process secretsdump and hashtopolis results")
parser.add_argument("secretsdump_results_file", help="Path to the secretsdump results file")
parser.add_argument("hashtopolis_results_file", help="Path to the hashtopolis results file")
parser.add_argument("-o", "--output_file", default="results.txt", help="Name of the output file (Default=results.txt)")
parser.add_argument("-f", "--id_field", type=int, default=3, help="Field number containing the ID in secretsdump results file (Default=3) -- NOTE: Default should work if you're using standard secretsdump output format")
args = parser.parse_args()

# Check if both files exist
if not os.path.exists(args.secretsdump_results_file):
    print(f"Error: Secretsdump Results File ({args.secretsdump_results_file}) does not exist.")
    print("Please make sure the file is created and in the current directory.")
    exit(1)

if not os.path.exists(args.hashtopolis_results_file):
	print(f"Error: Hashtopolis Results File ({args.hashtopolis_results_file}) does not exist.")
    print("Please make sure the file is created and in the current directory.")
    exit(1)

# Count lines in hashtopolis_results_file
with open(args.hashtopolis_results_file, "r") as file:
    line_count = len(file.readlines())
print(f"Checking {line_count} lines in Hashtopolis Results against each line in Secretsdump Results File.")

# Initialize match counter
match_count = 0

# Process secretsdump_results_file
with open(args.secretsdump_results_file, "r") as file1, open(args.output_file, "w") as temp:
    for line1 in file1:
        id = line1.split(":")[args.id_field]

        # Reset file pointer for hashtopolis_results_file
        file2 = open(args.hashtopolis_results_file, "r")

        match_found = False
        for line2 in file2:
            if line2.startswith(id + ":"):
                line1 = f"{line1[:-1]} > {line2.split(':')[1]}"
                match_found = True
                match_count += 1
                break

        file2.close()

        if match_found:
            temp.write(line1)  # Write the modified line1 without adding a newline

print(f"Found {match_count} matches. Results written to {args.output_file}")
