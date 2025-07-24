import os
import pytest
from reader import FileReader, AdvancedReader


@pytest.fixture(scope="module", autouse=True)
def setup_teardown():
    with open("file1.txt", "w") as f:
         f.write("THIS WILL MAKE")
    with open("file2.txt", "w") as f:
        f.write("A FULL SENTENCE! ")    
    with open("two_files.txt", "w") as f:
        f.write("THIS WILL MAKE")
    with open("combination.txt", "w") as f:
        f.write("THIS WILL MAKE")

    yield
    test_files = [ "combination.txt","empty.txt", "file1.txt", "file2.txt", "two_files.txt"]
    for file in test_files:
        if os.path.exists(file):
            os.remove(file)


class TestFileReader:
    
    def test_path_property(self):
        """Test path getter and setter."""
        reader = FileReader("file1.txt")
        assert reader.path == "file1.txt"
        
        reader.path = "file2.txt"
        assert reader.path == "file2.txt"
    
    
    def test_read_lines_generator(self):
        reader = FileReader("file1.txt")
        lines = list(reader.read_lines())
        assert lines == ["THIS WILL MAKE"]

    def test_add_operator(self):
        
        r1 = FileReader('file1.txt')
        r2 = FileReader('file2.txt')
        combined = r1 + r2

        assert isinstance(combined, FileReader)
        assert os.path.exists(combined.path)

        with open("two_files.txt") as f:
            content = f.read()
        assert "THIS" in content and "MAKE" in content
    
    def test_static_method(self):
        
        assert FileReader.file_type() == ".txt"
    
    def test_class_method(self):
        reader = FileReader.empty_file("empty.txt")
        assert os.path.exists("empty.txt")
        assert isinstance(reader, FileReader)
    
    def test_info_decorator(self):
        
        reader = FileReader("file1.txt")
        output = reader.info()
        assert "\033[" in output  
        assert "file1.txt" in output


class TestAdvancedReader:

    def test_combiner(self):
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
    
   # def test_str_override(self):
       # reader = AdvancedReader("file1.txt")
       # assert str(reader).startswith("[Advanced]")
