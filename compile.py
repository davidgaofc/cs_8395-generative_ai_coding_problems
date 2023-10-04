import os
import openai

import sys
from llm_test_helpers import get_llm, get_args

args = get_args(sys.argv)
llm = get_llm(args.model)

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

    response = llm.predict(file_content)
    new_content = response.choices[0].text.strip()
    output = new_content.replace("```python", "").replace("```py", "").replace("```", "").strip()

    with open(file_path, 'w') as f:
        f.write(output)


# The directory containing your Python files
DIRECTORY_PATH = "problems"
try:
    process_directory(DIRECTORY_PATH)
except:
    pass


