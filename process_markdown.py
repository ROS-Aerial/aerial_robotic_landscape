import re
import requests

# URL of the external Markdown file
url = "https://raw.githubusercontent.com/knmcguire/best-of-robot-simulators/main/README.md"

# Fetch the content
response = requests.get(url)
if response.status_code == 200:
    content = response.text

    # Extract the section titled "## Aerial Robotic Simulators"
    section_title = "## Aerial Robotics Simulators"
    section_pattern = rf"{section_title}.*?(?=\n## |\Z)"  # Match until the next "##" or end of file
    match = re.search(section_pattern, content, re.DOTALL)
    if match:
        content = match.group(0)  # Extract the matched section

        # Replace <details> tags with pymdownx.details syntax
        def process_details(match):
            summary = match.group(1)
            details_content = match.group(2)
            # Indent all lines in the details content with a tab
            indented_content = "\n".join(f"\t{line}" for line in details_content.splitlines())
            return f'??? Note "{summary}"\n{indented_content}'  # Start closed

        # Match <details><summary>...</summary>...</details> and process the content
        content = re.sub(
            r"<details><summary>(.*?)</summary>(.*?)</details>",
            process_details,
            content,
            flags=re.DOTALL,
        )

        # Save the processed content locally
        with open("docs/processed_external.md", "w", encoding="utf-8") as file:
            file.write(content)
        print("Processed content saved to docs/processed_external.md")
    else:
        print(f"Section '{section_title}' not found in the external Markdown file.")
else:
    print(f"Failed to fetch the file: {response.status_code}")