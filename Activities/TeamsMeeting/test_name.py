""" Week 03 team-activity -- members :
test the following functions in the names.py file. make_full_name, extract_family_name, and extract_given_name
    set up reminders # 1. use: from names import make_full_name,  extract_family_name, extract_given_name
                     # 2. import
 
  Core Requirements
1. Write test_make_full_name so that it tests make_full_name with various names, including long names, short names, and hyphenated names. Fix the mistake in the make_full_name function.
 
2. Write test_extract_family_name so that it tests extract_family_name with various names, including long names, short names, and hyphenated names.
 
3. Write test_extract_given_name so that it tests extract_given_name with various names, including long names, short names, and hyphenated names. Fix the mistake in the extract_given_name function.                  
"""
from names import make_full_name, \
    extract_family_name, extract_given_name
 
import pytest
 
""" How to test a function steps:
 
1. Open previously written functions file by name.
2. create test_file.py
"""
 
def test_make_full_name():
    """ parameters: None
    test make_full_name function here: write assert statements to test the value returned
    """
    # full_name = make_full_name ("Tina", "Brown")
    assert make_full_name(' Tina', 'Brown') == "Brown; Tina"
   
def test_extract_family_name():
    """ parameters: None
    test extract_family_name function here: write assert statements to test the value returned
    """  
   
def test_extract_given_name():
    """ parameters: None
    test extract_given_name function here: write assert statements to test the value returned
    """  
   
   
""" bottom of test_names.py file, write a call the the py.main function use this example: pytest.main(["-v", "--tb=line", "-rN", __file__]) """
# call the main function that is part of pytest so that the computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])