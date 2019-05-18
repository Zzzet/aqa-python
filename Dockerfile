FROM python:3.7.3-stretch

RUN mkdir -p /root/projects/automation-ui-tests
WORKDIR /root/projects/automation-ui-tests
COPY . .
RUN pip install -r requirements.txt -U

