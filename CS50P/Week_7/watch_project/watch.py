import re

def main():
    print(parse(input("HTML: ")))

def parse(html):
    html = html.strip()
    # Extracts YouTube embed URL from HTML and converts it to a short link.
    match = re.search(r'<iframe[^>]+src="https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"[^>]*></iframe>', str)

    if match:
        video_id = match.group(2)   # Extracts the video ID
        return f"https://youtu.be/{video_id}"

    return None # Returns None if no match found

if __name__ == "__main__":
    main()
