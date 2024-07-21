import pandas as pd

def evaluate(test_annotation_file, user_submission_file, phase_codename, **kwargs):
    print("Starting Evaluation.....")
    
    # Load ground truth and submission files
    ground_truth = pd.read_csv(test_annotation_file, header=None)
    submission = pd.read_csv(user_submission_file, header=None)
    
    # Extract labels (assuming they are in the first column)
    y_true = ground_truth[0]
    y_pred = submission[0]
    
    # Calculate accuracy
    correct_predictions = sum(y_true == y_pred)
    total_predictions = len(y_true)
    accuracy = correct_predictions / total_predictions
    
    # Return results in the required format
    output = {
        'result': [
            {
                'single_phase_split': {  # Match this to your dataset split name
                    'Accuracy': accuracy
                }
            }
        ]
    }
    
    print("Evaluation Completed Successfully!")
    return output

