FROM python:3.8-slim-buster

WORKDIR flask

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run the application:
COPY . .
CMD ["gunicorn", "--bind=0.0.0.0:5000", "--workers=4", "start:app"]