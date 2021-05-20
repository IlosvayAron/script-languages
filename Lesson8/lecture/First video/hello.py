#!/usr/bin/env python3


class Hello:
    def create_name(self, name):
        self.name = name

    def display_name(self):
        return self.name

    def greet(self):
        print(f"Hello {self.name}!")


def main():
    h = Hello()
    #print(h.name) - hibát dob mert a létrehozott Hello() objektumnak csak a 'create_name()' meghivását
    #követően lesz 'name' példányváltozója.
    h.create_name('Alice')
    print(h.display_name())
    h.greet()
    print(h.name)

##############################################################################

if __name__ == "__main__":
    main()