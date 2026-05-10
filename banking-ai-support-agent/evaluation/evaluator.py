import json

from app.main import generate_response

from evaluation.evaluation_prompts import (
    evaluation_test_cases
)

results = []

for test in evaluation_test_cases:

    question = test["question"]

    response = generate_response(question)

    result = {
        "category": test["category"],
        "question": question,
        "response": response
    }

    results.append(result)

with open(
    "evaluation/evaluation_results.json",
    "w"
) as file:

    json.dump(
        results,
        file,
        indent=4
    )

print("Evaluation completed.")