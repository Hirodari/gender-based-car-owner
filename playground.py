import csv
import itertools
from constants import fnames, parsers, class_names, compress_fields
from functools import partial
# from parse_utils import (csv_reader, extract_field_name,
#                         create_named_tuple_class, iter_file,
#                         create_combo_named_tuple_class)
from parse_utils import *
from datetime import datetime

data_iter = iter_combined(fnames, class_names, parsers, compress_fields)
# for row in itertools.islice(data_iter,1):
#     print(row)

print("="*100)
my_date = datetime(2017,3,1)
print(my_date)
# test = filtered_iter_combined(fnames, class_names, parsers, compress_fields,
#                              key=lambda x: x.last_updated >= my_date)
data_iter = filtered_iter_combined(fnames, class_names, parsers, compress_fields,
                             key=lambda x: x.employee_id == '98-7952860')
# for row in data_iter:
#     print(row)

print("="*100)
# print(list(test)[0])test
# print(test._fields)

# for field in test:
#     print(field)

data = filtered_iter_combined(fnames, class_names, parsers, compress_fields,
                                key=lambda x: x.last_updated >= my_date and
                                x.gender == 'Female')
def group_key(item):
    # return item.gender, item.vehicle_make
    return item.vehicle_make
# sorted_data = sorted(data,key=group_key)
# groups = itertools.groupby(sorted_data, key=group_key)
# for row in groups:
#     print(row)
# data_1, data_2 = itertools.tee(data,2)
#
# data_m = (row for row in data_1 if row.gender == 'Male')
# sorted_data_m = sorted(data_m, key=group_key)
# groups_m = itertools.groupby(sorted_data_m, key=group_key)
# group_m_counts = ((g[0], len(list(g[1]))) for g in groups_m)
# print(groups_m)
# print(f'{"="*20} Male {"="*22}')
# for row in  group_m_counts:
#     print(row)
#
# data_f = (row for row in data_2 if row.gender == 'Female')
# sorted_data_f = sorted(data_f, key=group_key)
# groups_f = itertools.groupby(sorted_data_f,key=group_key)
# group_f_counts = ((g[0], len(list(g[1]))) for g in groups_f)
# print(f'{"="*20} Female {"="*20}')
# for row in group_f_counts:
#     print(row)
# group_data(fnames,class_names,parsers,compress_fields,
#                 key,group_key,gender)

def filter_key(my_date,gender,row):
    return row.last_updated >= my_date and row.gender == gender

data_1 = group_data(fnames, class_names, parsers, compress_fields,
                 lambda x: filter_key(my_date,'Male',x),
                 group_key
                 )
cnt = 0
for row in data_1:
    print(row)
    cnt += row[1]
# print(sum(row[1]))
print(cnt)

data_2 = group_data(fnames, class_names, parsers, compress_fields,
                 partial(filter_key,my_date, "Female"),
                 group_key)
cnt = 0
for row in data_2:
    print(row)
    cnt += row[1]
print(cnt)
