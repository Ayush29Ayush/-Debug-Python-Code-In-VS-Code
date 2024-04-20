class Language:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def message(self):
        print("Hello, My name is " + self.name)


languages = [
    Language("C++"),
    Language("JavaScript"),
]

for language in languages:
    language.message()

# output = Language("Python")
# output.message()
# output.set_name("Python Version 3.12.0")
# output.message()
