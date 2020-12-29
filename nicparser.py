#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  nicparser.py
#
#  Copyright 2020 Kavindu Santhusa <Ksengine>
#
from datetime import datetime
import re


class Struct(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def NICParser(nic):
    nic = str(nic).lower()
    _type = True if len(nic) == 12 else False
    regex = r'^(\d{4})(\d{3})(\d{4})(\d{1})$' if _type else '^(\d{2})(\d{3})(\d{3})(\d{1})(\w)$'
    matches = re.search(regex, nic)
    year = matches.group(1) if _type else '19' + matches.group(1)
    gender = True
    try:
        match = int(matches.group(2))
        if match > 500:
            match -= 500
            gender = False
        date_time = datetime.strptime('{0},{1}'.format(match, year), '%j,%Y')
    except ValueError:
        raise ValueError('Birth date not within range.')
    return Struct(birth_year=int(year),
                  birth_date=date_time,
                  gender=gender,
                  serial_number=int(matches.group(3)),
                  check_digit=int(matches.group(4)),
                  special_letter=matches.group(5) if matches.group(5)
                  and matches.group(5) not in '1234567890' else None,
                  id_type=_type,
                  can_vote=matches.group(5) and matches.group(5) == 'v')
