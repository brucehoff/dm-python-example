FROM python
RUN pip install pydicom
RUN pip install numpy
COPY train.py /train.py
COPY score_sc1.py /score_sc1.py
COPY score_sc2.py /score_sc2.py
COPY train.sh /train.sh
COPY score_sc1.sh /score_sc1.sh
COPY score_sc2.sh /score_sc2.sh
COPY preprocess.sh /preprocess.sh
