FROM python
RUN pip install pydicom
COPY train.py /train.py
COPY train.sh /train.sh
COPY test.sh /test.sh
COPY preprocess.sh /preprocess.sh
