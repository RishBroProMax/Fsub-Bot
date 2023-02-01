FROM python-3.10.4

WORKDIR /fsubbot.py
COPY . /fsubbot.py

RUN pip3 install -U pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt

CMD ["python3", "-m", "fsubbot"]
