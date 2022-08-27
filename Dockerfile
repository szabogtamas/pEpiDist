FROM python

RUN pip install numpy scipy pandas seaborn peptides scikit-learn

RUN mkdir -p /scripts
COPY test_data/test.fa /test_data/test.fa
COPY src/pEpiDist /scripts/pEpiDist
COPY scripts/slice_counter.py /scripts/slice_counter.py
RUN chmod +x /scripts/slice_counter.py

ENTRYPOINT [ "python", "/scripts/epitope_query.py" ]
CMD [ "/test_data/test.fa" ]
