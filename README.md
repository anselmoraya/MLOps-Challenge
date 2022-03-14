# MLOps Workflow
This project is an example on how to apply MLOps principles to a Jupyter notebook.  Below are the topics that were to be covered.

* **MLOpsChallenge_v2.ipynb**

### Install Dependacies
```
❯ pipenv install && pipenv install --dev
```

### Create Virtual Env Shell
```
❯ pipenv shell
```

### Start notebook
```
❯ jupyter notebook
```
* http://localhost:8888/notebooks/src/MLOpsChallenge_v2.ipynb

### Build docker file
```
❯ docker build -t mlops:latest .
```

### Run docker (JSON Output)
```
❯ docker run -it mlops
Loading .env environment variables...
{"score_r2": 0.9000244324476292, "output": [3.7155025553662675]}
```

### Run Tests
```
❯ pytest tests --cov 
---------- coverage: platform darwin, python 3.9.10-final-0 ----------
Name    Stmts   Miss Branch BrPart  Cover   Missing
-------------------------------------------------
TOTAL      15      0      0      0   100%
```

### CI Tool
* [Github Actions](https://github.com/anselmoraya/MLOps-Challenge/actions)

### Accuracy
* tests/integration/test_accuracy.py

### Docmentation Files
* README.md
* .github/CODEOWNERS
* .github/CONTRIBUTING.md
* .github/ISSUE_TEMPLATE.md
* .github/PULL_REQUEST_TEMPLATE.md

### Security
* Dependacy Checking - Dependabot
* Vulnerability Management - Snyk
