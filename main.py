from parse_utils import group_data
from functools import partial
from datetime import datetime
from constants import *

my_date = datetime(2017,3,1)

def group_key(item):
    return item.vehicle_make

def filter_key(my_date,gender,row):
    return row.last_updated >= my_date and row.gender == gender

for gender in ("Male", "Female"):
    data = group_data(fnames, class_names, parsers, compress_fields,
                     partial(filter_key,my_date, gender),
                     group_key)
    print(f"{'*'*50} {gender} {'*'*50}")

    print(list(data))
    cnt = 0
    for row in list(data):
        cnt += row[1]
    print(f"{'*'*50} {cnt} car for {gender} {'*'*50}")
    # for row in data:
    #     print(row)
    #     cnt += row[1]
    # # print(sum(row[1]))
    # print(cnt)
