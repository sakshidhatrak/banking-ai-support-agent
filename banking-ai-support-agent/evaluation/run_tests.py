import json
import logging
import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import generate_response


# Configure logging
logging.basicConfig(
    filename="logs/test_results.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


def run_tests():
    with open("evaluation/test_prompts.json", "r") as file:
        test_cases = json.load(file)

    print("\n===== Running Banking Agent Tests =====\n")

    passed = 0
    failed = 0

    for test in test_cases:
        user_input = test["user_input"]
        expected_output = test["expected_output"]

        actual_output = generate_response(user_input)

        # Simple validation
        test_passed = expected_output.lower() in actual_output.lower()

        result = "PASS" if test_passed else "FAIL"

        if test_passed:
            passed += 1
        else:
            failed += 1

        # Console Output
        print(f"Test ID: {test['id']}")
        print(f"Category: {test['category']}")
        print(f"User Input: {user_input}")
        print(f"Expected: {expected_output}")
        print(f"Actual: {actual_output}")
        print(f"Result: {result}")
        print("-" * 60)

        # Log Output
        logging.info(f"TEST ID: {test['id']}")
        logging.info(f"CATEGORY: {test['category']}")
        logging.info(f"USER INPUT: {user_input}")
        logging.info(f"EXPECTED: {expected_output}")
        logging.info(f"ACTUAL: {actual_output}")
        logging.info(f"RESULT: {result}")
        logging.info("-" * 60)

    print("\n===== Test Summary =====")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")

    logging.info(f"TOTAL PASSED: {passed}")
    logging.info(f"TOTAL FAILED: {failed}")


if __name__ == "__main__":
    run_tests()