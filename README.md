# MLOps-Challenge

## Instructions
* Set up a repository for this model in a public github repo
* Serialize this model
* Containerize this model (ie write a Dockerfile that the model can run in)
* Write a minimal unittest in the framework of your choice
* Set up a CI Tool on your repo. Because your repo is public many CI Tools have free licenses for open source software, please use one of those
* Add a test for the accuracy of your model
* Minimal documentation


### Pubic Github Repo
```
https://github.com/anselmoraya/MLOps-Challenge
```

### Serialize this model (JSON)
```
❯ docker run -it mlops                
[3.7155025553662675]
```

### Containerize this model 
```
❯ docker images      
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
mlops        latest    a9e9e4831e1b   1 hours ago    1.3GB
```

### Minimal Unit Test
```
❯ pytest tests --cov                                       
---------- coverage: platform darwin, python 3.9.10-final-0 ----------
Name    Stmts   Miss Branch BrPart  Cover   Missing
---------------------------------------------------
---------------------------------------------------
TOTAL      15      0      0      0   100%
```

### Set up a CI Tool
* [Github Actions](https://github.com/anselmoraya/MLOps-Challenge/actions)

### Test for the accuracy
