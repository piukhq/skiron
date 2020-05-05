FROM python:3.8-alpine
ENV TZ=UTC
WORKDIR /app
ADD . .
RUN pip install pipenv gunicorn && \
    pipenv install --deploy --system --ignore-pipfile && \
    pip uninstall --yes pipenv && \
    rm -rf /root/.cache

