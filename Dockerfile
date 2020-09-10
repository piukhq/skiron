FROM binkhq/python:3.8

ENV TZ=UTC
WORKDIR /app
ADD . .
RUN pip install --no-cache-dir pipenv==2018.11.26 gunicorn && \
    pipenv install --deploy --system --ignore-pipfile && \
    pip uninstall --yes pipenv

CMD ["gunicorn", "--workers=2", "--threads=2", "--error-logfile=-", \
                 "--access-logfile=-", "--bind=0.0.0.0:9000", "wsgi:app" ]
