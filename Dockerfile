FROM python

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONONBUFFERED=1

WORKDIR /core
COPY . /core/

RUN pip install --upgrade pip
RUN pip install -r requirement.txt
