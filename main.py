import os
import socket

# Variables
read_directory = "/home/data"
write_directory = "/home/output/result.txt"
files = []
words_per_file = {}
word_count = {}
total_words = 0

# Iterate through files in directory
for file in os.listdir(read_directory):
    files.append(file) 

    file_path = os.path.join(read_directory, file)

    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            
            # Count words in file
            contents = f.read()
            words = contents.split()
            count = len(words)
            total_words += count

            words_per_file[file] = count

            # Calculate max word count for 3 highest words
            if file == "IF.txt":
                for word in words:
                    word = word.lower()

                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1

                max_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:3]

# Retrieve Internal IP Address
try:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
except Exception as e :
        ip_address = "ERROR"

# Format and store outputs
output_string = f"1. List of Text Files in {read_directory}:\n"
output_string += "\n".join(files) + "\n\n"

output_string += "2. Word Count in Each File:\n"
for file, count in words_per_file.items():
    output_string += f"- {file}: {count} words\n"  

output_string += "\n\n3. Grand Total of Words in Both Files:\n"
output_string += f"- Total: {total_words} words\n\n"

output_string += "4. Top 3 Words in IF.txt:\n"
for word, count in max_words:
    output_string += f"- {word}: {count} times\n"

output_string += "\n\n5. IP Address of the Machine:\n"
output_string += f"- IP Address: {ip_address}"

# Write to output file
with open(write_directory, 'w') as f:
    f.write(output_string)

# Print output file
with open(write_directory, 'r') as f:
    print(f.read())