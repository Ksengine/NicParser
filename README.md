# NicParser

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
print('can vote: ' + 'Yes' if parsed_nic.can_vote else 'No')
print('check digit' + str(parsed_nic.check_digit))
print('gender: ' + 'Male' if parsed_nic.gender else 'Female')
print('serial number: ' + parsed_nic.serial_number)
print('special letter: ' + parsed_nic.special_letter)
print('is Id old or new?: ' + 'New' if parsed_nic.id_type else 'Old')
```
for Python 2
```python
# paste the code on nicparser.py here, or place nicparser.py in same directory/folder and uncomment(remove #) following line.
#from nicparser import NICParser


nic = '721245677v'
parsed_nic = NICParser(nic)
print 'birthday: ' + str(parsed_nic.birth_date)
print 'birth year: ' + str(parsed_nic.birth_year)
print 'can vote: ' + 'Yes' if parsed_nic.can_vote else 'No'
print 'check digit' + str(parsed_nic.check_digit)
print 'gender: ' + 'Male' if parsed_nic.gender else 'Female'
print 'serial number: ' + parsed_nic.serial_number
print 'special letter: ' + parsed_nic.special_letter
print 'is Id old or new?: ' + 'New' if parsed_nic.id_type else 'Old'
```

## Usage
**`NICParser(nic)`**
pass NIC number as string(`str`) or integear(`int`). returns parsed data as `Struct` object.
eg:-
```python
result = NICParser('721245677v')
```
result has following attributes.
- `birth_date` - birth day of 
