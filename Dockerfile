FROM arm32v7/python:2.7.13-jessie

LABEL NAME="Vijay Donthireddy" VERSION=1.0

COPY led-blink.py ./

RUN pip install --no-cache-dir rpi.gpio

CMD ["python", "./led-blink.py"]
