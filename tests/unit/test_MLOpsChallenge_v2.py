import src.MLOpsChallenge_v2 as notebook
import numpy as np
from numpyencoder import NumpyEncoder
from sklearn.linear_model import LinearRegression
import pytest

@pytest.fixture
def mocked_numpy(mocker):
    mock_model = mocker.patch.object(np, 'array', autospec=True)
    mock_model.return_value = np.array([11])
    return mock_model

@pytest.fixture
def mocked_LinearRegression(mocker):
    mock_LinearRegression = mocker.patch.object(LinearRegression, 'fit', autospec=True)
    mock_LinearRegression.return_value = LinearRegression().fit([1],[1])
    return mock_LinearRegression

def test_create_prediction_methods_called(mocker, mocked_LinearRegression, mocked_numpy):
    mocker.patch.object(notebook, 'generate_reponse', autospec=True)
    notebook.create_prediction()
    assert mocked_numpy.called
    assert mocked_LinearRegression.called

def test_generate_reponse():
    result = notebook.generate_reponse(1, np.array([1]))
    assert {'score_r2': 1, 'output': [1]} == result

def test_main_calls_methods(mocker):
    mock_create_prediction = mocker.patch.object(notebook, 'create_prediction', autospec=True)
    mock_create_prediction.return_value = {}
    notebook.main()
    assert mock_create_prediction.called
