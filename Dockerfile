FROM python:3.7.3-stretch

RUN mkdir -p /root/projects/automation-ui-tests
WORKDIR /root/projects/automation-ui-tests
COPY src src
COPY test test
COPY conftest.py conftest.py
COPY requirements.txt requirements.txt
RUN find -name __pycache__ -exec rm -rf {} \; | true
#RUN find -name .pyc -exec rm -rf {} \;
RUN pip install -r requirements.txt -U

