#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        # Constructor to initialize the object with a default value
        self._value = value

    def get_value(self):
        # Getter method to retrieve the value of the string
        return self._value

    def set_value(self, stringVal):
        # Setter method to set the value of the string
        if type(stringVal) == str:
            # Check if the input is a string
            self._value = stringVal
        else:
            # If the input is not a string, print an error message
            print("The value must be a string.")

    # Property to access the value attribute using property decorators
    value = property(get_value, set_value)

    def is_sentence(self):
        # Method to check if the string ends with a period (.)
        return self._value.endswith(".")

    def is_question(self):
        # Method to check if the string ends with a question mark (?)
        return self._value.endswith("?")

    def is_exclamation(self):
        # Method to check if the string ends with an exclamation mark (!)
        return self._value.endswith("!")

    def count_sentences(self):
        # Method to count the number of sentences in the string
        value = self.value
        for punc in ['!', '?']:
            # Replace other punctuation marks with periods for accurate sentence counting
            value = value.replace(punc, '.')

        # Split the string into sentences based on periods and filter out empty strings
        sentences = [s for s in value.split('.') if s]

        # Return the number of sentences
        return len(sentences)
