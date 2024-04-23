FROM python:3.11.0-alpine

WORKDIR /app

RUN pip install \
  --upgrade \
  --no-cache-dir \
  --ignore-installed \
  --trusted-host pypi.python.org \
  --trusted-host pypi.org \
  --trusted-host files.pythonhosted.org \
  pipenv==2023.11.15

ENV PIPENV_VENV_IN_PROJECT=1

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pipenv install --deploy

USER 1000
ENV PATH="/app/.venv/bin:${PATH}"

COPY ./src ./src
WORKDIR /app/src

CMD ["gunicorn", "-b", "0.0.0.0:8000", "main:app"]
