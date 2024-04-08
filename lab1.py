#Write a program take text file as an input and print word, character count and ascii value of each characters as output. 
def count(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            word_count = len(text.split())
            char_count = len(text)
            print(f"Word Count: {word_count}")
            print(f"Character Count: {char_count}")
    except FileNotFoundError:
        print("Could not open the file.")

if __name__ == "__main__":
    filename = input("Enter the name of the text file: ")
    count(filename)
