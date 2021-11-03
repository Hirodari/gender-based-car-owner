import csv
import itertools
from datetime import datetime
from collections import namedtuple


def csv_reader(fname,*,delimiter=',', quotechar='"', include_header=False):
	with open(fname) as f:
		reader = csv.reader(f, delimiter=delimiter, quotechar=quotechar)
		if not include_header:
			next(f)
		yield from reader

def parse_date(value, *, format='%Y-%m-%dT%H:%M:%SZ'):
	return datetime.strptime(value, format)

def extract_field_name(fname):
	return next(csv_reader(fname, include_header=True))

def create_named_tuple_class(fname,class_name):
    fields = extract_field_name(fname)
    return namedtuple(class_name, fields)

def create_combo_named_tuple_class(fnames, compress_fields):
    compress_fields = itertools.chain.from_iterable(compress_fields)
    field_names = itertools.chain.from_iterable(
                extract_field_name(fname) for fname in fnames)
    compressed_field_names = itertools.compress(field_names,compress_fields)
    return namedtuple('Data', compressed_field_names)

def iter_file(fname, class_name, parser):
    nt_class = create_named_tuple_class(fname, class_name)
    reader = csv_reader(fname)
    for row in reader:
        parsed_data = (parser_fn(row) for row, parser_fn in zip(row,parser))
        yield nt_class(*parsed_data)

def iter_combined_plain_tuple(fnames,class_names,parsers, compress_fields):
    compress_fields = tuple(itertools.chain.from_iterable(compress_fields))
    zipped_tuples = zip(*(iter_file(fname,class_name,parser) for fname, class_name,
                    parser in zip(fnames, class_names, parsers)))
    merger_iter = (itertools.chain.from_iterable(zipped_tuple) for
                    zipped_tuple in zipped_tuples)

    for row in merger_iter:
        compressed_row = itertools.compress(row, compress_fields)
        yield tuple(compressed_row)

def iter_combined(fnames, class_names, parsers,compress_fields):
    combo_nt = create_combo_named_tuple_class(fnames, compress_fields)
    data = iter_combined_plain_tuple(fnames,class_names,parsers,
                    compress_fields)
    for row in data:
        yield combo_nt(*row)

def filtered_iter_combined(fnames, class_names, parsers,compress_fields,*,
                            key=None):
    row = iter_combined(fnames, class_names, parsers,compress_fields)
    yield from filter(key,row)

def group_data(fnames,class_names,parsers,compress_fields,
                filter_key,group_key):
    data = filtered_iter_combined(fnames, class_names, parsers,
                                    compress_fields, key=filter_key)
    # data_filtered = (row for row in data if row.gender == gender)
    sorted_data = sorted(data, key=group_key)
    grouped_data = itertools.groupby(sorted_data, key=group_key)
    grouped_data_counts = ((g[0],len(list(g[1]))) for g in grouped_data)
    return sorted(grouped_data_counts, key=lambda x: x[1], reverse=True)
