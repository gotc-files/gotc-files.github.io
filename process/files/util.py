from argparse import ArgumentError


def id_int64_str_to_hex(id_int64_str):
    return id_int64_to_hex(int(id_int64_str))


def id_int64_to_hex(id_int64):
    if id_int64 < 0:
        id_int64 += (1 << 64)
    if id_int64 < 0 or id_int64 >= (1 << 64):
        raise ValueError('Given input is not int64 format: %s' % id_int64)

    return hex(id_int64)[2:]
