FROM python
RUN pip install pydicom
RUN pip install numpy
COPY train.py /train.py
COPY score.py /score.py
COPY train.sh /train.sh
COPY score_sc1.sh /score_sc1.sh
COPY score_sc2.sh /score_sc2.sh
COPY preprocess.sh /preprocess.sh
