import os
import openai

# Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

def process_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                process_file(file_path)


def process_file(file_path):
    print(file_path)
    with open(file_path, 'r') as f:
        file_content = f.read()

    response = openai.Completion.create(
        engine="davinci",
        prompt=file_content,
        max_tokens=150  # Adjust as necessary
    )

    new_content = response.choices[0].text.strip()

    with open(file_path, 'w') as f:
        f.write(new_content)


# The directory containing your Python files
DIRECTORY_PATH = "problems"

process_directory(DIRECTORY_PATH)


