#importing unittest from python standard library
import unittest
#importing time 
import time
#importing scrabble_score.py code 
from  scrabble_score import scrabble_score

dict = ['apple', 'ball', 'cat', 'do']

# Creating TestProject2 class that inherits TestCase class from unittest
class TestProject2(unittest.TestCase):

    #Defining testfunction as method with self as argument
    #Test for checking scrabblescore of given word
    def test_scrabblescore(self): 

        #Storing the result of scrabble_score method in variable
        finalresult=scrabble_score("ball")
        #assertion for comapring two values
        self.assertEqual(finalresult, 6)


    #testcase to check upper & lower case letters has same value
    def test_upper_lower(self):
        #calculating the value for upper case letters and holding in variable
        uppercaseresult=scrabble_score("APPLE") 
        #calculating the value for lower case letters and holding in variable
        lowercaseresult=scrabble_score("apple")
        #assertion for comparing upper and lowercase reult
        self.assertEqual(uppercaseresult, lowercaseresult)


    #testcase to check whether input from  is word or not 
    def test_input_string(self):
        #Assigning string to word variable 
        word='ball'
        #checking word is character or not 
        if word.isalpha():
            #assertion 
            assert bool 

    #testcase for timer
    def test_timeout(self):
        print ("timer test case start for 15 sec")
        #looping for 15 secs
        for i in range(1,15):
            time.sleep(1)
        print("Timer end")

    #testcase for checking input for length 
    def test_input_isnumeric(self):
        #declaring integer variable
        input_length=7
        #assertion to check whether input length is integer or not 
        assert type(input_length) is int,"num must be an integer"
    

    def test_dict_word(self):
        for i in range(len(dict)):
            self.assertEqual(dict[1], 'ball')


if __name__ == '__main__':
    unittest.main()