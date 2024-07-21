import pandas as pd

def evaluate(test_annotation_file, user_submission_file, phase_codename, **kwargs):
    print("Starting Evaluation.....")
    """
    Evaluates the submission for a particular challenge phase and returns score
    Arguments:
        `test_annotations_file`: Path to test_annotation_file on the server
        `user_submission_file`: Path to file submitted by the user
        `phase_codename`: Phase to which submission is made
        `**kwargs`: keyword arguments that contains additional submission
        metadata that challenge hosts can use to send slack notification.
        You can access the submission metadata
        with kwargs['submission_metadata']
    """
    # Load the ground truth and submission
    ground_truth = pd.read_csv(test_annotation_file)
    submission = pd.read_csv(user_submission_file)

    # Ensure the correct columns are present
    assert 'class3' in ground_truth.columns
    assert 'class3' in submission.columns

    # Calculate accuracy
    correct = (ground_truth['class3'] == submission['class3']).sum()
    total = ground_truth.shape[0]
    accuracy = correct / total

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

    print("Completed evaluation for Test Phase")
    return output
