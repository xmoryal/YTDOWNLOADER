import os
from datetime import datetime

def parse_cookie_line(line):
    """
    Parse a single line of Chrome cookie export format (tab-separated).
    Format: name\tvalue\tdomain\tpath\texpires\tlength\tsecure\thttpOnly\tsameSite\tpriority
    """
    parts = line.split('\t')
    if len(parts) < 10:
        return None  # Invalid line

    name = parts[0].strip()
    value = parts[1].strip()
    domain = parts[2].strip()
    path = parts[3].strip()
    expires_str = parts[4].strip()
    secure = 'TRUE' if parts[6].strip() == '✓' else 'FALSE'
    flag = 'TRUE' if domain.startswith('.') else 'FALSE'

    # Convert expires from ISO 8601 to Unix timestamp
    try:
        expires_dt = datetime.fromisoformat(expires_str.replace('Z', '+00:00'))
        expires = str(int(expires_dt.timestamp()))
    except ValueError:
        expires = '0'  # Default to session cookie if parsing fails

    return f"{domain}\t{flag}\t{path}\t{secure}\t{expires}\t{name}\t{value}"

def main():
    file_path = input("Enter the path to the cookie file (e.g., cookies.txt): ").strip()
    if not os.path.isfile(file_path):
        print("File not found. Please check the path and try again.")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        netscape_lines = []
        for line in lines:
            line = line.strip()
            if line:  # Skip empty lines
                netscape_line = parse_cookie_line(line)
                if netscape_line:
                    netscape_lines.append(netscape_line)

        if not netscape_lines:
            print("No valid cookies found in the file.")
            return

        # Generate output file name
        base, ext = os.path.splitext(file_path)
        output_path = f"{base}_netscape{ext}"

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(netscape_lines) + '\n')

        print(f"Converted cookies saved to: {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
