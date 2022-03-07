# MLOps-Challenge



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

### Build docker file
```
❯ docker build -t mlops:latest .
```

### Run docker (JSON Output)
```
❯ docker run -it mlops   
[3.7155025553662675]
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


### Docmentation Files
* README.md
* .github/CODEOWNERS
* .github/CONTRIBUTING.md
* .github/ISSUE_TEMPLATE.md
* .github/PULL_REQUEST_TEMPLATE.md