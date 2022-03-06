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

def test_predict_linear_numpy_called(mocked_LinearRegression, mocked_numpy):
    notebook.predict_linear()
    assert mocked_numpy.called

def test_predict_linear_numpy_called(mocked_LinearRegression, mocked_numpy):
    notebook.predict_linear()
    assert mocked_LinearRegression.called

def test_predict_linear_LinearRegression_called(mocked_LinearRegression, mocked_numpy):
    notebook.predict_linear()
    assert mocked_numpy.called

def test_serialize_results_returns_json():
    result = notebook.serialize_results(np.array([1]))
    assert '[1]' == result

def test_main_calls_methods(mocker):
    mock_predict_linear = mocker.patch.object(notebook, 'predict_linear', autospec=True)
    mock_serialize_results = mocker.patch.object(notebook, 'serialize_results', autospec=True)
    notebook.main()
    assert mock_predict_linear.called
    assert mock_serialize_results.called
