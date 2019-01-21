# -*- coding: utf-8 -*-
import re

def main():
    with open("README.md", "r", encoding="utf-8") as f:

        pattern = re.compile("##+")  # create pattern to find number sequence

        for line in f:
            m = pattern.match(line)
            if m:
                print(line) ## output line


if __name__ == "__main__":
    main()