# Read the CSV file
with open('wappalyzer_leetcode-com.csv', 'r') as csv_file:
    lines = csv_file.readlines()

if len(lines) < 2:
    print("Invalid input file format. The file should contain at least 2 lines.")
else:
    keys = lines[0].strip().split(',')
    values = lines[1].strip().split(',')

    if len(keys) != len(values):
        print("Mismatch between the number of keys and values.")
    else:
        # Create a dictionary from the keys and values
        data_dict = {key: value for key, value in zip(keys, values)}

        # Write processed data to a new TXT file
        with open('processed_data_Leetcode.txt', 'w') as txt_file:
            for key, value in data_dict.items():
                txt_file.write(f"{key}: {value}\n")

        print("Processed data has been written to 'processed_data.txt'")