FROM python:3.6-slim

COPY . /app

ENV JAVA_HOME /usr/lib/jvm/java-1.7-openjdk/jre

RUN apt-get update && apt-get install -y g++ default-jdk
RUN python3 -m pip install --upgrade pip
RUN pip3 install flask konlpy torch tensorflow-cpu lime 

WORKDIR /app

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]