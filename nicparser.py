#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  nicparser.py
#
#  Copyright 2020 Kavindu Santhusa <kavindu@orangepiplus>
#
from datetime import datetime


class Struct(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def NICParser(nic):
    nic = str(nic).upper()
    nic_type = len(nic) == 12
    year = nic[:4] if nic_type else '19' + nic[:2]
    try:
        birth_date = datetime.strptime(
            '{0},{1}'.format(nic[4:7] if nic_type else nic[2:5], year),
            '%j,%Y')
    except ValueError:
        raise ValueError('Birth date not within range.')
    return Struct(
        birth_year=int(year),
        birth_date=birth_date,
        gender=int(nic[4:7]) < 500 if nic_type else int(nic[2:5]) < 500,
        serial_number=nic[5:8] if not nic_type else nic[7:11],
        check_digit=int(nic[8]) if not nic_type else int(nic[10]),
        special_letter=nic[-1] if nic[-1] not in '1234567890' else None,
        id_type=nic_type,
        can_vote=nic[-1] == 'V')
