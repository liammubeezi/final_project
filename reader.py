
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