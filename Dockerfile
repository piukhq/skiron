FROM ghcr.io/binkhq/python:3.9-pipenv

WORKDIR /app
ADD . .
RUN pipenv install --deploy --system --ignore-pipfile

ENV PROMETHEUS_MULTIPROC_DIR=/dev/shm
ENTRYPOINT [ "linkerd-await", "--" ]
CMD ["gunicorn", "--workers=2", "--threads=2", "--error-logfile=-", \
                 "--access-logfile=-", "--bind=0.0.0.0:9000", "wsgi:app" ]
