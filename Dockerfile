FROM python
RUN pip install pandas
RUN pip install lxml html5lib beautifulsoup4

COPY . /home
WORKDIR /home
CMD python main.py