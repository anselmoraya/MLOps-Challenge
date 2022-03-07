import src.MLOpsChallenge_v2 as notebook
import json

def test_accuracy_over_90_percent():
    response = notebook.create_prediction()
    assert response['score_r2'] > .90

if __name__ == '__main__':
    test_accuracy_over_90_percent()