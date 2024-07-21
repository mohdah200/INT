def evaluate(test_annotation_file, user_submission_file, phase_codename, **kwargs):
    print("Starting Evaluation.....")

    # Load ground truth and user submission CSV files
    ground_truth = []
    user_submission = []

    with open(test_annotation_file, 'r') as f:
        for line in f:
            ground_truth.append(line.strip())

    with open(user_submission_file, 'r') as f:
        for line in f:
            user_submission.append(line.strip())

    # Extract labels
    y_true = ground_truth
    y_pred = user_submission

    # Calculate accuracy
    correct = sum(1 for true, pred in zip(y_true, y_pred) if true == pred)
    total = len(y_true)
    accuracy = correct / total

    # Prepare the output dictionary
    output = {}
    output["result"] = [
        {
            "test_split": {
                "Accuracy": accuracy
            }
        }
    ]
    output["submission_result"] = output["result"][0]["test_split"]

    print("Completed evaluation.")
    return output
