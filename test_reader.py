import os
import pytest
from reader import FileReader, AdvancedReader


@pytest.fixture(scope="module", autouse=True)
def setup_teardown():
    """Setup test files before tests, cleanup after."""
    # Setup
    with open("sample1.txt", "w") as f:
        f.write("A\nB\n")
    with open("sample2.txt", "w") as f:
        f.write("C\nD\n")
    
    yield  # Run tests
    
    # Cleanup
    test_files = ["sample1.txt", "sample2.txt", "combined.txt", 
                  "multi_combined.txt", "empty.txt"]
    for file in test_files:
        if os.path.exists(file):
            os.remove(file)


class TestFileReader:
    """Test cases for FileReader class."""
    
    def test_path_property(self):
        """Test path getter and setter."""
        reader = FileReader("file1.txt")
        assert reader.path == "file1.txt"
        
        reader.path = "file2.txt"
        assert reader.path == "file2.txt"
    
    def test_invalid_extension(self):
        """Test that non-.txt files raise ValueError."""
        reader = FileReader("file1.txt")
        with pytest.raises(ValueError):
            reader.path = "invalid.pdf"
    
    def test_read_lines_generator(self):
        """Test line reading generator."""
        reader = FileReader("file1.txt")
        lines = list(reader.read_lines())
        assert lines == ["THIS WILL MAKE"]

    def test_add_operator(self):
        """Test file concatenation with + operator."""
        r1 = FileReader('file1.txt')
        r2 = FileReader('file2.txt')
        combined = r1 + r2

        assert isinstance(combined, FileReader)
        assert os.path.exists(combined.path)

        with open("two_files.txt") as f:
            content = f.read()
        assert "THIS" in content and "MAKE" in content
    
    def test_static_method(self):
        """Test static method."""
        assert FileReader.file_type() == ".txt"
    
    def test_class_method(self):
        """Test class method for empty file creation."""
        reader = FileReader.empty_file("empty.txt")
        assert os.path.exists("empty.txt")
        assert isinstance(reader, FileReader)
    
    def test_info_decorator(self):
        """Test that info method uses color decorator."""
        reader = FileReader("sample1.txt")
        output = reader.info()
        assert "\033[" in output  # ANSI color code
        assert "sample1.txt" in output


class TestAdvancedReader:
    """Test cases for AdvancedReader class."""
    
    def test_concat_many(self):
        """Test multi-file concatenation."""
        r1 = AdvancedReader("file1.txt")
        r2 = FileReader("file2.txt")
        multi = r1.combiner(r2, FileReader("file1.txt"))
        
        assert isinstance(multi, AdvancedReader)
        assert os.path.exists(multi.path)
        
        with open("combination.txt") as f:
            data = f.read()
        assert data.count("THIS") == 2  # THIS appears twice
        assert "THIS" in data
    
    def test_str_override(self):
        """Test overridden __str__ method."""
        reader = AdvancedReader("file1.txt")
        assert str(reader).startswith("[Advanced]")
