# -*- coding: utf-8 -*-

def main(namelist):
    def get_format(is_angy):
        return "{0}.My name is {1}" if is_angy else "{0}.{1} is my classmate"

    for i, n in enumerate(namelist):
        print(get_format(n == "Angy").format(i, n))

if __name__ == "__main__":
    namelist = ("Bill", "Anne", "Angy", "Cony", "Daniel", "Occhan")
    main(namelist)