import importlib
import os
import sys

def get_curr_working_dir():
    curr_working_dir = os.getcwd()
    return curr_working_dir

def run():
    current_working_directory = get_curr_working_dir()
    sys.path.append(current_working_directory)
    sys.path.append(f"{current_working_directory}/challenge_data/challenge_1")

    challenge_id = 1
    challenge_phase = "single_phase"  # Update with your actual phase codename
    annotation_file_path = f"{current_working_directory}/annotations/ground_truth.csv"  # Path to your ground truth labels
    user_submission_file_path = f"{current_working_directory}/submission.csv"  # Path to the sample submission file

    CHALLENGE_IMPORT_STRING = "challenge_data.challenge_1.main"
    challenge_module = importlib.import_module(CHALLENGE_IMPORT_STRING)

    EVALUATION_SCRIPTS = {}
    EVALUATION_SCRIPTS[challenge_id] = challenge_module
    print("Trying to evaluate")
    submission_metadata = {
        "status": u"running",
        "when_made_public": None,
        "participant_team": 5,
        "input_file": "https://abc.xyz/path/to/submission/file.csv",
        "execution_time": u"123",
        "publication_url": u"ABC",
        "challenge_phase": 1,
        "created_by": u"ABC",
        "stdout_file": "https://abc.xyz/path/to/stdout/file.json",
        "method_name": u"Test",
        "stderr_file": "https://abc.xyz/path/to/stderr/file.json",
        "participant_team_name": u"Test Team",
        "project_url": u"http://foo.bar",
        "method_description": u"ABC",
        "is_public": False,
        "submission_result_file": "https://abc.xyz/path/result/file.json",
        "id": 123,
        "submitted_at": u"2017-03-20T19:22:03.880652Z",
    }
    result = EVALUATION_SCRIPTS[challenge_id].evaluate(
        annotation_file_path,
        user_submission_file_path,
        challenge_phase,
        submission_metadata=submission_metadata,
    )
    print("Evaluated Successfully!")
    print(result)

if __name__ == "__main__":
    run()
