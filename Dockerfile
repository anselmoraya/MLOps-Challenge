FROM python:3.9 AS build
LABEL maintainer="raya.anselmo@gmail.com"

ENV PYTHONPATH /
ENV PIPENV_VENV_IN_PROJECT=true
COPY . .
RUN pip install pipenv
RUN pipenv lock -r > requirements.txt
RUN pipenv lock --dev -r > requirements-dev.txt
RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt
RUN jupyter nbconvert --to script src/MLOpsChallenge_v2.ipynb


ENTRYPOINT ["pipenv","run", "python", "src/MLOpsChallenge_v2.py"]
CMD ["version"]
