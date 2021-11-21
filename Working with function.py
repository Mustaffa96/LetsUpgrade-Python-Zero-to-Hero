class biodata:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    ## this method will be called when we print the object
    def __str__(self):
        return f'{self.name} is {self.age} years old.'
muse = biodata("Mustaffa", 25)

## it'll wake up the __str__() method
print(f"{muse}")
