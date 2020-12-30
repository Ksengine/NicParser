def test_basic():
    numbers = {
        '199136578548': {
            'birth_date': datetime(1991, 12, 31, 0, 0),
            'birth_year': 1991,
            'can_vote': False,
            'check_digit': 4,
            'gender': True,
            'id_type': True,
            'serial_number': '7854',
            'special_letter': None
        },
        '199226025738': {
            'birth_date': datetime(1992, 9, 16, 0, 0),
            'birth_year': 1992,
            'can_vote': False,
            'check_digit': 3,
            'gender': True,
            'id_type': True,
            'serial_number': '2573',
            'special_letter': None
        },
        '199236578548': {
            'birth_date': datetime(1992, 12, 30, 0, 0),
            'birth_year': 1992,
            'can_vote': False,
            'check_digit': 4,
            'gender': True,
            'id_type': True,
            'serial_number': '7854',
            'special_letter': None
        },
        '199336578548': {
            'birth_date': datetime(1993, 12, 31, 0, 0),
            'birth_year': 1993,
            'can_vote': False,
            'check_digit': 4,
            'gender': True,
            'id_type': True,
            'serial_number': '7854',
            'special_letter': None
        },
        '201626085734': {
            'birth_date': datetime(2016, 9, 16, 0, 0),
            'birth_year': 2016,
            'can_vote': False,
            'check_digit': 3,
            'gender': True,
            'id_type': True,
            'serial_number': '8573',
            'special_letter': None
        },
        '902580972V': {
            'birth_date': datetime(1990, 9, 15, 0, 0),
            'birth_year': 1990,
            'can_vote': True,
            'check_digit': 2,
            'gender': True,
            'id_type': False,
            'serial_number': '097',
            'special_letter': 'V'
        },
        '913014146V': {
            'birth_date': datetime(1991, 10, 28, 0, 0),
            'birth_year': 1991,
            'can_vote': True,
            'check_digit': 6,
            'gender': True,
            'id_type': False,
            'serial_number': '414',
            'special_letter': 'V'
        },
        '922602573': {
            'birth_date': datetime(1992, 9, 16, 0, 0),
            'birth_year': 1992,
            'can_vote': False,
            'check_digit': 3,
            'gender': True,
            'id_type': False,
            'serial_number': '257',
            'special_letter': None
        },
        '922602573V': {
            'birth_date': datetime(1992, 9, 16, 0, 0),
            'birth_year': 1992,
            'can_vote': True,
            'check_digit': 3,
            'gender': True,
            'id_type': False,
            'serial_number': '257',
            'special_letter': 'V'
        },
        '922602573v': {
            'birth_date': datetime(1992, 9, 16, 0, 0),
            'birth_year': 1992,
            'can_vote': True,
            'check_digit': 3,
            'gender': True,
            'id_type': False,
            'serial_number': '257',
            'special_letter': 'V'
        }
    }
    for number in numbers:
        nic = NICParser(number)
        for attr in numbers[number]:
            assert getattr(nic, attr) == numbers[number][
                attr], 'excepted "{}" for "{}" of "{}", got "{}".'.format(
                    str(numbers[number][attr]), attr, number,
                    str(getattr(nic, attr)))
