import re

def main():
    print(count(input("Text: ")))

def count(text):
    # \b ensures "um" is a standalone word
    matches = re.findall(r'\bum\b', text, re.IGNORECASE)
    return len(matches)

if __name__ == "__main__":
    main()
