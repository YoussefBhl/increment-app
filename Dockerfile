FROM python
WORKDIR /src
COPY ./src /src
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python /src/app.py