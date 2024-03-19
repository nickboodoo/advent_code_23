class TextFileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        # Open file from filename
        try:
            with open(self.file_path, 'r') as file:
                data = file.read()
            return data
        
        # Handle misinput
        except FileNotFoundError:
            print(f"Error: File '{self.file_path}' not found.")
            return None
        
        # Catch-all exception handling
        except Exception as e:
            print(f"Error: {e}")
            return None

    def read_lines(self):
        # Open file from filename and store the data as variable 'lines'
        try:
            with open(self.file_path, 'r') as file:
                lines = file.readlines()
            return lines
        
        except FileNotFoundError:
            print(f"Error: File '{self.file_path}' not found.")
            return None
        
        except Exception as e:
            print(f"Error: {e}")
            return None

    def first_and_last_digit(self):
        lines = self.read_lines()
        if lines:
            results = []
            for line in lines:
                digits = []
                for char in line:
                    if char.isdigit():
                        digits.append(char)
                if digits:
                    first_digit = digits[0]
                    last_digit = digits[-1]
                    results.append((first_digit, last_digit))
            return results
        else:
            return None


