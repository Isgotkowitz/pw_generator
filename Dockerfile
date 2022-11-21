FROM python:3

ADD pw_generator.py /

RUN pip install mongoengine

ENTRYPOINT [ "python", "./pw_generator.py" ]
