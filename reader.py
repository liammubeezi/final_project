
def decor(color: str):
    
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
    
    
    def __init__(self, path: str):
        """Initialize with file path."""
        self.path = path
    
    @property
    def path(self) :
        """Get file path."""
        return self._path
    
    @path.setter
    def path(self, value: str):
        
        if not value.endswith(".txt"):
            raise ValueError("Only .txt files allowed.")
        self._path = value
    
    def read_lines(self):
        
        with open(self.path, "r") as f:
            for line in f:
                yield line
    
    def __str__(self) :
        
        return f"Reading from: {self.path}"
    
    def __add__(self, other):
       
        new_path = "two_files.txt"
        with open(new_path, "w") as f:
            f.writelines(self.read_lines())
            f.writelines(other.read_lines())
        return FileReader(new_path)
    
    @staticmethod
    def file_type() :
        
        return ".txt"
    
    @classmethod
    def empty_file(cls, name: str):
        
        open(name, "w").close()
        return cls(name)
    
    @decor("green")
    def info(self) :
       
        return f"File path: {self.path}"
    @decor("blue")
    def info2(self) :
        
        return f"File path: {self.path}"


class AdvancedReader(FileReader):
    
    
    def combiner(self, *others):
        """Concatenate multiple files."""
        new_path = "combination.txt"
        with open(new_path, "w") as f:
            f.writelines(self.read_lines())
            for other in others:
                f.writelines(other.read_lines())
        return AdvancedReader(new_path)
    
    def __str__(self) :
        """Enhanced string representation."""
        return f"[Advanced] {self.path}"


if __name__ == "__main__":
    
    print("Creating test files...")
    print("part 1 created")
    
    with open("file1.txt", "w") as f:
        f.write("THIS WILL MAKE")
    file1 = FileReader("file1.txt")
    print(file1.info())

    print("part 2 created:")
    with open("file2.txt", "w") as f:
        f.write(" A FULL SENTENCE! ")
    file2 = FileReader("file2.txt")
    print(file2.info2())
    
    
    combined = file1 + file2
    print(f"Full sentence: {combined.path}")

    
    adv = AdvancedReader("file1.txt")
   # multi = adv.concat_many(file2,  FileReader("file1.txt"), FileReader("file2.txt"), combined)
    multi = adv.combiner(
    file2,
    FileReader('file1.txt'),
    FileReader('file2.txt'),
    combined  
)
   
    print(f"combined: {multi.path}")