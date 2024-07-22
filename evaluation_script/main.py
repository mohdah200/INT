import pandas as pd

def evaluate(test_annotation_file, user_submission_file, phase_codename, **kwargs):
    print("Starting Evaluation.....")

    # Load the ground truth and the user submission
    ground_truth = pd.read_csv(test_annotation_file)
    user_submission = pd.read_csv(user_submission_file)

    # Calculate accuracy
    correct = (ground_truth['label'] == user_submission['label']).sum()
    total = ground_truth.shape[0]
    accuracy = correct / total

    # Prepare the output
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
        # To display the results in the result file
        output["submission_result"] = output["result"][0]["test_split"]
        print("Completed evaluation for Single Phase")

    return output
