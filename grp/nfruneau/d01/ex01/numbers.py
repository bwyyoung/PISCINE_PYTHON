#!/usr/local/bin/python3

if __name__ == '__main__':
    with open("numbers.txt", 'r') as f:
        line = f.readline().strip()
        print(line.replace(",", "\n"))
