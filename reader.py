# file_processor.py
'''
def deco(color: str):
    colors = {"red": "\033[91m", "green": "\033[92m", "blue": "\033[94m", "reset": "\033[0m"}
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{colors.get(color, '')}{result}{colors['reset']}"
        return wrapper
    return decorator

class FileReader:
    def __init__(self, path):
        self._path = path

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        if not value.endswith(".txt"):
            raise ValueError("Only .txt files allowed.")
        self._path = value

    def read_lines(self):
        with open(self.path, "r") as f:
            for line in f:
                yield line

    def __str__(self):
        return f"Reading from: {self.path}"

    def __add__(self, other):
        new_path = "combined.txt"
        with open(new_path, "w") as f:
            f.writelines(self.read_lines())
            f.writelines(other.read_lines())
        return FileReader(new_path)

    @staticmethod
    def file_type():
        return ".txt"

    @classmethod
    def empty_file(cls, name):
        open(name, "w").close()
        return cls(name)

    @deco("green")
    def info(self):
        return f"File path: {self.path}"

class AdvancedReader(FileReader):
    def concat_many(self, *others):
        new_path = "multi_combined.txt"
        with open(new_path, "w") as f:
            f.writelines(self.read_lines())
            for other in others:
                f.writelines(other.read_lines())
        return AdvancedReader(new_path)

    def __str__(self):
        return f"[Advanced] {self.path}"
    
'''
'''
if __name__ == "__main__":
    # Create a test file
    with open("sample1.txt", "w") as f:
        f.write("Hello from sample1\n")

    with open("sample2.txt", "w") as f:
        f.write("Hello from sample2\n")

    # Create FileReader objects
    file1 = FileReader("sample1.txt")
    file2 = FileReader("sample2.txt")

    # Print info with colored decorator
    print(file1.info())

    # Combine files using +
    combined = file1 + file2
    print(f"Combined file created: {combined.path}")

    # Use AdvancedReader to combine many files
    adv = AdvancedReader("sample1.txt")
    multi = adv.concat_many(file2, FileReader("sample1.txt"))
    print(f"Multi file created: {multi.path}")

'''
'''


if __name__ == "__main__":
    # Step 1: Create a test file
    print("[1] Creating file: sample1.txt")
    with open("sample1.txt", "w") as f:
        f.write("Line 1\nLine 2\nLine 3\n")

    # Step 2: Create a FileReader object
    print("[2] Creating FileReader for sample1.txt")
    reader = FileReader("sample1.txt")

    # Step 3: Use the generator to read lines
    print("[3] Reading lines using generator:")
    for line in reader.read_lines():
        print(f"  Yielded line: {line.strip()}")


''' 



'''
if __name__ == "__main__":
    # Step 1: Create test files
    print("[1] Creating files...")
    with open("sample1.txt", "w") as f:
        f.write("Line 1 from file 1\nLine 2 from file 1\n")
    with open("sample2.txt", "w") as f:
        f.write("Line 1 from file 2\nLine 2 from file 2\n")

    # Step 2: Initialize readers
    print("[2] Initializing readers...")
    reader1 = FileReader("sample1.txt")
    reader2 = FileReader("sample2.txt")

    # Step 3: Show info using decorator
    print("[3] Displaying file info:")
    print(reader1.info())

    # Step 4: Combine two files using +
    print("[4] Combining two files...")
    combined = reader1 + reader2
    print(f"Combined file created: {combined.path}")

    # Step 5: Combine multiple files using AdvancedReader
    print("[5] Combining multiple files...")
    adv = AdvancedReader("sample1.txt")
    multi = adv.concat_many(reader2, FileReader("sample1.txt"))
    print(f"Multi file created: {multi.path}")


#print(repr(reader1.info()))


'''
def decor(color: str):
    """Decorator that adds ANSI color to function output."""
    colors = {
            "red": "\033[91m", 
            "green": "\033[92m", 
            "blue": "\033[94m", 
            "reset": "\033[0m",
            "HEADER": '\033[95m',
            "OKCYAN": '\033[96m',
            "WARNING": '\033[93m',

            "BOLD": '\033[1m',
            "UNDERLINE": '\033[4m',
            "BLINK": '\033[5m',
            "BLUE": "\033[0;34m",
            "COLOR_BLINK": "\033[5m",
            "COLOR_NEGATIVE": "\033[7m"
    }
    
    def foo(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{colors.get(color, '')}{result}{colors['reset']}"
        return wrapper
    return foo


class FileReader:
    """File reader class with generator-based line reading."""
    
    def __init__(self, path: str):
        """Initialize with file path."""
        self.path = path
    
    @property
    def path(self) :
        """Get file path."""
        return self._path
    
    @path.setter
    def path(self, value: str):
        """Set file path, only .txt files allowed."""
        if not value.endswith(".txt"):
            raise ValueError("Only .txt files allowed.")
        self._path = value
    
    def read_lines(self):
        """Generator that yields lines from file."""
        with open(self.path, "r") as f:
            for line in f:
                yield line
    
    def __str__(self) :
        """String representation."""
        return f"Reading from: {self.path}"
    
    def __add__(self, other):
        """Concatenate two files using + operator."""
        new_path = "two_files.txt"
        with open(new_path, "w") as f:
            f.writelines(self.read_lines())
            f.writelines(other.read_lines())
        return FileReader(new_path)
    
    @staticmethod
    def file_type() :
        """Return supported file type."""
        return ".txt"
    
    @classmethod
    def empty_file(cls, name: str):
        """Create empty file and return FileReader instance."""
        open(name, "w").close()
        return cls(name)
    
    @decor("green")
    def info(self) :
        """Return file info with green color."""
        return f"File path: {self.path}"
    @decor("blue")
    def info2(self) :
        """Return file info with blue color."""
        return f"File path: {self.path}"


class AdvancedReader(FileReader):
    """Enhanced file reader with multi-file concatenation."""
    
    def concat_many(self, *others):
        """Concatenate multiple files."""
        new_path = "big_sentence.txt"
        with open(new_path, "w") as f:
            f.writelines(self.read_lines())
            for other in others:
                f.writelines(other.read_lines())
        return AdvancedReader(new_path)
    
    def __str__(self) :
        """Enhanced string representation."""
        return f"[Advanced] {self.path}"


if __name__ == "__main__":
    # Demo usage
    print("Creating test files...")
    print("part 1")
    
    with open("file1.txt", "w") as f:
        f.write("THIS WILL MAKE")
    print("part 2")
    with open("file2.txt", "w") as f:
        f.write(" A FULL SENTENCE! ")
    
    # Initialize readers
    file1 = FileReader("file1.txt")
    file2 = FileReader("file2.txt")
    
    # Show colored info
    print(file1.info())
    print(file2.info2())
    
    # Combine files
    combined = file1 + file2
    print(f"Full sentence: {combined.path}")

    # Multi-file combination
    adv = AdvancedReader("file1.txt")
   # multi = adv.concat_many(file2,  FileReader("file1.txt"), FileReader("file2.txt"), combined)
    multi = adv.concat_many(
    file2,
    FileReader('file1.txt'),
    FileReader('file2.txt'),
    combined  # assuming combined is a FileReader or similar object
)
    print(f"all_three: {multi.path}")