import pandas as pd

def evaluate(test_annotation_file, user_submission_file, phase_codename, **kwargs):
    print("Starting Evaluation.....")

    # Load the ground truth and submission files
    ground_truth = pd.read_csv(test_annotation_file)
    submission = pd.read_csv(user_submission_file)

    # Compute accuracy
    correct = (ground_truth['class3'] == submission['class3']).sum()
    total = len(ground_truth)
    accuracy = correct / total

    # Return the accuracy
    output = {
        'result': [
            {
                'test_split': {
                    'Accuracy': accuracy
                }
            }
        ],
        'submission_result': {
            'Accuracy': accuracy
        }
    }
    return output
