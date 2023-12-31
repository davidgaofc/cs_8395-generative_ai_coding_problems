import os
import openai
from langchain.llms import OpenAI

import sys

try:
    from llm_test_helpers import get_llm, get_args

    args = get_args(sys.argv)
    llm = get_llm(args.model)
except:
    llm = OpenAI()

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

    response = llm.predict("Generate a Python function adhering to the following prompt: \n"+file_content +"\nProvide only the code. If you need to use helper functions, they should be defined before the function. Do not include tests or any other information. Your response will be directly executed and tested.")
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


