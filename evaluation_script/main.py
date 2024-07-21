import pandas as pd

def evaluate(test_annotation_file, user_submission_file, phase_codename, **kwargs):
    print("Starting Evaluation.....")

    # Load the ground truth and user submission files
    ground_truth = pd.read_csv(test_annotation_file)
    user_submission = pd.read_csv(user_submission_file)

    # Calculate accuracy
    accuracy = (ground_truth['class3'] == user_submission['class3']).mean()

    output = {}
    if phase_codename == "single_phase":
        print("Evaluating for Single Phase")
        output["result"] = [
            {
                "test_split": {
                    "Accuracy": accuracy,
                }
            }
        ]
        output["submission_result"] = output["result"][0]["test_split"]
        print("Completed evaluation for Single Phase")

    return output

