def read_file(filename):
    with open(filename, 'r') as file:
        contents = file.read()
    return contents

def write_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)
    return "File written successfully."

if __name__ == "__main__":
    # Example usage
    filename = input("Enter file name to read: ")
    file_contents = read_file(filename)
    print("File contents:")
    print(file_contents)

    filename_to_write = input("Enter file name to write: ")
    data_to_write = input("Enter data to write to file: ")
    write_file(filename_to_write, data_to_write)
    print("Data written to file.")
