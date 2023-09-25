import importlib.util
import json
import sys

class TestFramework:
    def __init__(self, module_name):
        self.module_name = module_name
        self.module = self.load_module(module_name)
        self.unimplemented_functions = []
        self.test_file = None
        self.total_score = 0

    def load_module(self, module_name):
        try:
            spec = importlib.util.spec_from_file_location(module_name, f"{module_name}.py")
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        except Exception as e:
            print(f"Error loading module '{module_name}': {e}")
            sys.exit(1)

    def load_test_file(self, test_file):
        try:
            spec = importlib.util.spec_from_file_location(test_file, test_file)
            test_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(test_module)
            return test_module
        except Exception as e:
            print(f"Error loading test file '{test_file}': {e}")
            sys.exit(1)

    def run_tests(self):
        tests_for_module = len(self.unimplemented_functions)
        temp = 0
        for function_name in self.unimplemented_functions:
            try:
                test_function = getattr(self.test_module, f"test_{function_name}")
                test_result = test_function()
                print(f"Function {function_name}: {test_result}")
                if(test_result == "PASSED"):
                    temp += 1
            except NotImplementedError:
                print(f"Function {function_name}: NOT IMPLEMENTED")
            except AssertionError:
                print(f"Function {function_name}: FAILED")
            except Exception as e:
                print(f"Function {function_name}: ERROR - {e}")
        if(temp == tests_for_module):
            self.total_score += 1
def main():
    problems_file = "assessment.json"
    with open(problems_file) as f:
        problems = json.load(f)

    for problem_name, problem_data in problems.items():
        print(f"Problem: {problem_name}")
        print(problem_data["description"])

        module_name = problem_data["module_name"]
        test_framework = TestFramework("problems/"+module_name)
        test_framework.test_module = test_framework.load_test_file("tests/"+problem_data["test_file"])

        for function_name in problem_data["unimplemented_functions"]:
            test_framework.unimplemented_functions.append(function_name)

        print(f"Running tests for {module_name}:")
        test_framework.run_tests()
        print()

    output_data = {"output": test_framework.total_score}

    with open('output.json', 'w') as json_file:
        json.dump(output_data, json_file)
if __name__ == "__main__":
    main()