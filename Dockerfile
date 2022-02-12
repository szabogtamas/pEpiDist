FROM python

RUN pip install numpy peptides scikit-learn

RUN mkdir -p /scripts
COPY test_data/test.fa /test_data/test.fa
COPY scripts/slice_counter.py /scripts/slice_counter.py
RUN chmod +x /scripts/slice_counter.py

ENTRYPOINT [ "python", "/scripts/slice_counter.py" ]
CMD [ "/test_data/test.fa" ]
