#!/bin/python3

import sys

print('The default character encoding is', sys.getdefaultencoding())

# 0b is a prefix to denote the number is in binary
# utf-8 is unicode but variable length

# Hello
# أهلا
# 你好

def get_ascii_array(val):
  val_encoded = val.encode('ascii')
  val_num_array = []
  val_hex_array = []
  val_array = []
  for char in val_encoded:
    val_num_array.append(char)
    val_hex_array.append(hex(char))
    val_array.append(bin(char))
  return val_array, val_num_array, val_hex_array
    
def get_utf_array(val):
  val_array = []  
  val_hex_array = []
  val_num_array = []
  for char in val:
    val_array.append(bin(ord(char)))
    val_num_array.append(ord(char))
    val_hex_array.append(hex(ord(char)))
  return val_array, val_num_array, val_hex_array


val = input('What would you like to convert to binary?')
ascii = input("Would you like to use ascii encoding Y/N?")
if (ascii.lower() == 'y'):
  #ascii encoding
  ascii_char, ascii_val, ascii_hex = get_ascii_array(val)
  print('The ascii encoding is:', ascii_char)  
  print('The ascii encoding in hex is:', ascii_hex)
  print('The ascii encoding in decimals is:', ascii_val)
else:
  # unicode encoding
  utf_char, utf_val, utf_hex = get_utf_array(val)
  print('The utf encoding is:', utf_char)  
  print('The utf encoding in hex is:', utf_hex)
  print('The utf encoding in decimals is:', utf_val)
