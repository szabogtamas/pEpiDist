FROM python

RUN pip install numpy

COPY ./scripts/slicer.py /scripts/slice_counter.py
RUN chmod +x /scripts/slice_counter.py

ENTRYPOINT [ "python", "/scripts/slice_counter.py" ]
CMD [ "human" ]