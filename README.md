
# Automated Coding Ability Testing Suite

## Introduction

Welcome to the Automated Coding Ability Testing Suite, a unique project aimed at evaluating a candidate's coding skills by not only assessing their ability to solve problems from scratch but also to take existing code and broad requirements to craft solutions. The suite provides an array of problems housed under the `problems` directory, with tests available in the `tests` directory to validate the solutions.

## Project Structure

Here's the layout of the project:

```
Root Directory
|-- problems/
|    |-- problem_1/
|    |-- problem_2/
|    |-- ...
|    |-- problem_100/
|
|-- tests/
|    |-- test_1/
|    |-- test_2/
|    |-- ...
|    |-- test_100/
|
|-- test_framework.py
|-- assessment.json
```

### Directories and Files

- `problems/`: Contains folders named `problem_1` to `problem_100`, each housing an individual problem that the candidate needs to solve. Candidates might need to enhance existing code or create new solutions based on the broad requirements mentioned in each problem folder.
  
- `tests/`: Contains folders named `test_1` to `test_100`, each containing test cases that correspond to the problems in the `problems/` folder. These tests will be used to evaluate the correctness of the solutions.
  
- `test_framework.py`: The main script that orchestrates the testing of the problems against the respective test cases. When executed, it will run all the test cases against the problems and output the results.
  
- `assessment.json`: A JSON file that contains the evaluation criteria and other configurations needed for the assessment.

## Getting Started

### Prerequisites

Before you begin, ensure that you have the following installed:
- Python 3.x
- (Other dependencies if any)

### Setting Up

1. Clone the repository to your local machine.
2. Navigate to the root directory.
3. Install any necessary dependencies as mentioned in the prerequisites.
4. You are now set to start solving the problems.

### Instructions for Candidates

1. Navigate to the `problems/` folder and choose a problem to solve.
2. Read the problem statement and the accompanying documents to understand the requirements.
3. Modify the existing code or create new code to solve the problem.
4. Ensure that your solution meets the broad requirements mentioned in the problem folder.
5. Repeat steps 1 to 4 for other problems as necessary.

## Running the Tests

Once you have completed solving the problems, you can test them by running the `test_framework.py` script. Here are the steps to do so:

1. Navigate to the root directory in your terminal.
2. Run the command `python test_framework.py`.
3. The script will execute all the test cases against the problems and output the results in the terminal.
4. Review the results to ensure that your solutions are correct and meet the requirements.

## Evaluation

The candidates' solutions will be evaluated based on the following criteria (as mentioned in `assessment.json`):
- Correctness: The solution produces the expected output for all test cases.
- Code Quality: The solution follows good coding practices, including readability and maintainability.
- Problem-Solving Skills: The solution demonstrates the candidate's ability to solve complex problems and create effective solutions.

## What Makes This Project Unique

In the vast sea of coding assessment platforms, this project stands out due to its unique approach to evaluating a candidate's coding ability. Here are some distinguishing features:

1. **Holistic Evaluation**: Beyond just writing code from scratch, candidates are evaluated on their ability to understand, modify, and enhance existing code, which mirrors real-world scenarios where developers often work with existing codebases.

2. **Broad Requirements**: The problems come with broad requirements, encouraging candidates to think critically and creatively to come up with effective solutions, rather than just following a rigid set of instructions.

3. **Real-World Simulation**: This project closely simulates real-world software development scenarios, testing not just technical skills but also skills such as problem-solving, critical thinking, and the ability to work with ambiguous requirements.

4. **Comprehensive Testing Suite**: The `tests/` folder contains a comprehensive set of test cases that ensure solutions are not only correct but also efficient and robust, preparing candidates for the kind of testing they would encounter in real-world development environments.

5. **Flexible Assessment Criteria**: The `assessment.json` allows for flexible and configurable evaluation criteria, ensuring that the assessment can be tailored to suit various levels of complexity and different skill sets.

6. **Self-Contained Environment**: The project provides a self-contained environment for candidates to demonstrate their skills, without the need for external dependencies or platforms, ensuring a smooth and straightforward assessment process.

By participating in this assessment, candidates not only get to showcase their coding skills but also their ability to work with real-world scenarios, making this project a unique and comprehensive tool for evaluating coding ability.

## Contribution

If you would like to contribute to this project, please follow the contribution guidelines (if any).

## License

This project is licensed under the (mention license here) License - see the LICENSE.md file for details.

## Contact

If you have any questions or need further clarification, feel free to reach out to (mention contact details).

We wish you the best of luck with your assessment!
