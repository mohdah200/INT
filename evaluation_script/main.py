import pandas as pd
from sklearn.metrics import roc_auc_score

def evaluate(test_annotation_file, user_submission_file, phase_codename, **kwargs):
    print("Starting Evaluation.....")
    
    # Load ground truth and submission files
    ground_truth = pd.read_csv(test_annotation_file)
    submission = pd.read_csv(user_submission_file)
    
    # Ensure that the labels are correctly named in both files
    y_true = ground_truth['class3']
    y_pred = submission['class3']
    
    # Calculate AUC-ROC
    auc_roc = roc_auc_score(y_true, y_pred)
    
    # Return results in the required format
    output = {
        'result': [
            {
                'single_phase_split': {  # Match this to your dataset split name
                    'AUC-ROC': auc_roc
                }
            }
        ]
    }
    
    print("Evaluation Completed Successfully!")
    return output
