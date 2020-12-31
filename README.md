
# NicParser

![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/ksengine/nicparser/Python%20package/main?logo=github&style=for-the-badge)
[![GitHub issues](https://img.shields.io/github/issues/Ksengine/NicParser?logo=github&style=for-the-badge)](https://github.com/Ksengine/NicParser/issues)
[![GitHub forks](https://img.shields.io/github/forks/Ksengine/NicParser?logo=github&style=for-the-badge)](https://github.com/Ksengine/NicParser/network)
[![GitHub stars](https://img.shields.io/github/stars/Ksengine/NicParser?logo=github&style=for-the-badge)](https://github.com/Ksengine/NicParser/stargazers)
[![GitHub license](https://img.shields.io/github/license/Ksengine/NicParser?logo=github&style=for-the-badge)](https://github.com/Ksengine/NicParser/LICENSE)
![GitHub file size in bytes](https://img.shields.io/github/size/ksengine/nicparser/nicparser.py?logo=Python&logoColor=lightblue&style=for-the-badge)
[![Twitter](https://img.shields.io/static/v1?message=%20&label=tweet&style=for-the-badge&logo=twitter&color=white&labelColor=f2f2f2)](https://twitter.com/intent/tweet?text=Sri%20Lankan%20national%20identity%20card%20number%20validator%20and%20parser.:&url=https%3A%2F%2Fgithub.com%2FKsengine%2FNicParser)

Sri Lankan national identity card number validator and parser.

## About
This parser is simple and lightweight. Rules of parser are extracted from this [article](https://en.wikipedia.org/wiki/National_identity_card_%28Sri_Lanka%29) in Wikipedia. Following table is copied from that article. It is an example for parse national identity card numbers.
||Birth  by year|Birth day of the year|Serial number|Check digit|Special letter|
|-|-|-|-|-|-|
|Old NIC number|74|192|275|7|V|
|New NIC number|1964|104|0275|7|-|

© Wikipedia - [license](https://en.wikipedia.org/wiki/Wikipedia:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License)

In the name **NicParser**. Nic means _national identity card_.
This Idea came because I saw a project named **NICParser**(not NicParser) written in PHP programming language. Tests are extracted from that.

## Getting Started
### Prerequisites
You need following things to use this tool.
- Python(install from [here](https://python.org))
_Python 2 and 3 versions are supported._
## Installation
No Installation. Just copy the code in [nicparser.py](nicparser.py) to your code file or download [nicparser.py](nicparser.py) and include on your project directory/folder.
## Example
for Python 3(This should work for most situations.)
```python
# paste the code on nicparser.py here, or place nicparser.py in same directory/folder and uncomment(remove #) following line.
#from nicparser import NICParser


nic = '721245677v'
parsed_nic = NICParser(nic)
print('birthday: ' + str(parsed_nic.birth_date))
print('birth year: ' + str(parsed_nic.birth_year))
print('can vote: ' + ('Yes' if parsed_nic.can_vote else 'No'))
print('check digit' + str(parsed_nic.check_digit))
print('gender: ' + ('Male' if parsed_nic.gender else 'Female'))
print('serial number: ' + parsed_nic.serial_number)
print('special letter: ' + parsed_nic.special_letter)
print('is Id old or new?: ' + ('New' if parsed_nic.id_type else 'Old'))
```
for Python 2
```python
# paste the code on nicparser.py here, or place nicparser.py in same directory/folder and uncomment(remove #) following line.
#from nicparser import NICParser


nic = '721245677v'
parsed_nic = NICParser(nic)
print 'birthday: ' + str(parsed_nic.birth_date)
print 'birth year: ' + str(parsed_nic.birth_year)
print 'can vote: ' + ('Yes' if parsed_nic.can_vote else 'No')
print 'check digit' + str(parsed_nic.check_digit)
print 'gender: ' + ('Male' if parsed_nic.gender else 'Female')
print 'serial number: ' + parsed_nic.serial_number
print 'special letter: ' + parsed_nic.special_letter
print 'is Id old or new?: ' + ('New' if parsed_nic.id_type else 'Old')
```

## Usage
**`NICParser(nic)`**
pass NIC number as string(`str`) or integear(`int`). returns parsed data as `Struct` object.
eg:-
```python
result = NICParser('721245677v')
```
result has following attributes.
- `birth_date` - birth day of NIC number owner. as `datetime.datetime` object.
   ```python
  print(result.birth_date)
  ```
  `datetime.datetime` object
  - `datetime.year`
  Get the birth year of NIC owner. Same to the `birth_year` attribute of result.
     ```python
    print(result.birth_date.year)
     ```
  - `datetime.month`
Get the month of birth of NIC owner. Returns integer (`int`).
     ```python
    monthnames = [None, "January", "February", "March", "April", "May", "June",
                        "July", "August", "September", "October", "November", "December"]
    print(monthnames[result.birth_date.month])
     ```
  - `datetime.day`
  Between 1 and the number of days in the given month of the given year.
     ```python
    print(result.birth_date.day)
     ```
  - `date.weekday()`
  Return the day of the week as an integer, where Monday is 0 and Sunday is 6. For example, `result.birth_date.weekday()  ==  2`, a Wednesday. See also `isoweekday()`.
     ```python
    daynames = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    print(daynames[result.birth_date.weekday()])
     ```
  - `date.isoweekday()`
  Return the day of the week as an integer, where Monday is 1 and Sunday is 7. For example, `date(2002,  12,  4).isoweekday()  ==  3`, a Wednesday. See also `weekday()`.
     ```python
    daynames = [None, "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    print(daynames[result.birth_date.weekday()])
     ```
  for more info - [Python Docs]([https://docs.python.org/3/library/datetime.html#datetime-objects](https://docs.python.org/3/library/datetime.html#datetime-objects))

- `birth_year` - Get the birth year of NIC owner. Same to the `birth_date.year` attribute of result. Returns integer(`int`).
  ```python
  print(result.birth_year)
  ```

- `can_vote` - eligibility of the NIC owner to vote in local area as boolean(`bool`). `True` means can and `False` means can't.
  ```python
  print(result.can_vote)
  ```

- `check_digit` - Single digit.
  ```python
  print(result.check_digit)
  ```

- `gender` - Gender of NIC owner as boolean(`bool`). `True` means gender is male and `False` means gender is female.
  ```python
  print(result.gender)
  ```
- `serial_number` - Serial number of the issued day as string(`str`).
  ```python
  print(result.serial_number)
  ```
  > Note: Don't convert serial number to integer(`int`). It makes `0735` same to `0735`.

- `special_letter` - The final letter of old type. NIC numbers. It is generally a 'V' which indicates that the holder is eligible to vote in the area. In some cases the it can be 'X' which usually indicates the holder is not eligible to vote; possibly because they were not permanent residents of Sri Lanka when applying for an NIC. See also `can_vote`. `special_letter` is always capitalized. If no special letter, it is `None`. So it is always `None` for new NIC numbers.
  ```python
  print(result.special_letter)
  ```
- `id_type` - Type of the NIC number.
  - New(`True`) - NIC number issued from 1 January 2016.
  - Old(`False`) - NIC number issued before 1 January 2016.
  ```python
  print(result.id_type)
  ```
## Roadmap

See the  [open issues](issues)  for a list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are  **greatly appreciated**. We specially accepts new language implementations(NICParser in java, c, ect). Even giving a star, opening issue or sharing are great contributions.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

_git commands are placed in brackets for command line git users_
## License

Distributed under the MIT License. See  [`LICENSE`](LICENSE)  for more information.
