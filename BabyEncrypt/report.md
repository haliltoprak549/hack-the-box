# Decrypting a message in BabyEncryption

## Description
In this challange, there is a python script, that encryptes a message and a file that includes the encrypted message. And I will explain my own solution to decrypting this message.

## Steps to Reproduce
The following steps indicate a proof of concept outlined in one(1) step to reproduce and execute the issue.

**Step 1:**
Download the python script in this repository called `baby-encrypt.py`

**Step 2:**
Browse to the downloaded files location.

**Step 3:**
Run the command `python3 baby-encrypt.py [content of msg.enc file]` in the terminal to display the decrypted message.

## Proof of Concept
Download your `openvpn` file from [HTB Labs section](https://app.hackthebox.com/). And run this file in Kali Linux Terminal by command
```
openvpn [your-openvpn-file]
```
Start the instance and download files in .zip format from the button seen in Figure 1.1.

| ![image](https://user-images.githubusercontent.com/112284234/227726648-5917aa76-1d7f-4ffe-99e7-99a6c129131a.png) | 
|:--:| 
| *Figure 1.1* |

Browse to the downloaded file location. Unzip it with `unzip BabyEncryption.zip`, provide the zip password which is given in the lab: `hackthebox`. When we unzip the zip folder, it will have a `msg.enc` file and a `chall.py` python script. 

This is how `chall.py` script looks like:
```python
import string
from secret import MSG

def encryption(msg):
    ct = []
    for char in msg:
        ct.append((123 * char + 18) % 256)
    return bytes(ct)

ct = encryption(MSG)
f = open('./msg.enc','w')
f.write(ct.hex())
f.close()
```
This shows us how they encrypted a provided message. And the `msg.enc` file looks like this:
```
6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921
```
And this is the message to be encrypted.

I created a python script to decrypt this message according to `chall.py`. And I will explain how this script works. First of all, the script looks like this:
```python
import sys

# Encrypted message given in the parameters, should provided with the downloaded file from app.hackthebox.com/challenges/228
encrypted_msg = sys.argv[1]

# Revert the hex format to bytes format
bytes_format = bytes.fromhex(encrypted_msg)

# Revert the byte array to an integer array
int_arr = []
for i in bytearray(bytes_format):
	int_arr.append(i)

# ASCII codes of the chars
ascii_dict = {i: chr(i) for i in range(128)}

# Find the values of ASCII codes after implementing (123 * char + 18) % 256 formula to them
crypted_ascii = []
for i in range(0, 128):
	crypted_ascii.append((123 * i + 18) % 256)
	
# Create a dictionary with updated ASCII codes and their values
decrypt_dict = dict(zip(crypted_ascii, ascii_dict.values()))

# Iterate over int_arr to find their ASCII values, and store them in a result array
result_arr = []
for i in int_arr: 
	result_arr.append(decrypt_dict[i])
	
# Join the result array to get the string result
result_str = ''.join(result_arr)
print(result_str)
```

In the first line, I imported `sys` module to get the parameter of encrypted message from the terminal. I assigned the parameter to a variable.

We will go from the end to the beginning of the `chall.py` script. The last encryption method is the `hex()` method. To revert that method, we will use `bytes.fromhex(encrypted_msg)`. The output of this method should look like this:
```
b'n\n\x93r\xecI\xa3\xf6\x93\x0e\xd8r?\x9d\xf6\xf6r\x0e\xd8\xd8\x9d\xc4\x93r"\xecr\x14\xd8\x9d\x1e\x0e5,\xe0\xaan\xc8+\xf6""{\xb7\x0e\x7f\xb75"I\xb7\xd8\x93\xc4\x93\xd8S\x9d\xec\x8f\xb7\x93]I\x0e\x7f\x9d"\xec\x89\xb7\xa3"\xec\x8f\xd8\x0e\x7f\x89!\xe0'
```

After retreiving the byte format of the message, we will convert it with `bytearray()` method to a bytearray, and then iterate over the bytearray to get the integer array of the message. This array is an array which consists of **updated** values of ASCII values of the message characters. This integer array should look like this:

```
[110, 10, 147, 114, 236, 73, 163, 246, 147, 14, 216, 114, 63, 157, 246, 246, 114, 14, 216, 216, 157, 196, 147, 114, 34, 236, 114, 20, 216, 157, 30, 14, 53, 44, 224, 170, 110, 200, 43, 246, 34, 34, 123, 183, 14, 127, 183, 53, 34, 73, 183, 216, 147, 196, 147, 216, 83, 157, 236, 143, 183, 147, 93, 73, 14, 127, 157, 34, 236, 137, 183, 163, 34, 236, 143, 216, 14, 127, 137, 33]
```

Now we will find ASCII values, and update them with given formula in `chall.py`. And then with the updated values, we will find the corresponding char to that value. To get ASCII dictionary, we will use this command:

`ascii_dict = {i: chr(i) for i in range(128)}`

The ascii_dict dictionary should look like this:
```
{0: '\x00', 1: '\x01', 2: '\x02', 3: '\x03', 4: '\x04', 5: '\x05', 6: '\x06', 7: '\x07', 8: '\x08', 9: '\t', 10: '\n', 11: '\x0b', 12: '\x0c', 13: '\r', 14: '\x0e', 15: '\x0f', 16: '\x10', 17: '\x11', 18: '\x12', 19: '\x13', 20: '\x14', 21: '\x15', 22: '\x16', 23: '\x17', 24: '\x18', 25: '\x19', 26: '\x1a', 27: '\x1b', 28: '\x1c', 29: '\x1d', 30: '\x1e', 31: '\x1f', 32: ' ', 33: '!', 34: '"', 35: '#', 36: '$', 37: '%', 38: '&', 39: "'", 40: '(', 41: ')', 42: '*', 43: '+', 44: ',', 45: '-', 46: '.', 47: '/', 48: '0', 49: '1', 50: '2', 51: '3', 52: '4', 53: '5', 54: '6', 55: '7', 56: '8', 57: '9', 58: ':', 59: ';', 60: '<', 61: '=', 62: '>', 63: '?', 64: '@', 65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E', 70: 'F', 71: 'G', 72: 'H', 73: 'I', 74: 'J', 75: 'K', 76: 'L', 77: 'M', 78: 'N', 79: 'O', 80: 'P', 81: 'Q', 82: 'R', 83: 'S', 84: 'T', 85: 'U', 86: 'V', 87: 'W', 88: 'X', 89: 'Y', 90: 'Z', 91: '[', 92: '\\', 93: ']', 94: '^', 95: '_', 96: '`', 97: 'a', 98: 'b', 99: 'c', 100: 'd', 101: 'e', 102: 'f', 103: 'g', 104: 'h', 105: 'i', 106: 'j', 107: 'k', 108: 'l', 109: 'm', 110: 'n', 111: 'o', 112: 'p', 113: 'q', 114: 'r', 115: 's', 116: 't', 117: 'u', 118: 'v', 119: 'w', 120: 'x', 121: 'y', 122: 'z', 123: '{', 124: '|', 125: '}', 126: '~', 127: '\x7f'}
```
Now we will create a new list, with values from 0 to 127, just like the keys of ascii_dict, and will update this values according to the formula in the `chall.py`. And then update the keys of ascii_dict with the new list. To create the list:
```
crypted_ascii = []
for i in range(0, 128):
	crypted_ascii.append((123 * i + 18) % 256)
```
And the output should contain 128 items with updated values of 0-127:
```
[18, 141, 8, 131, 254, 121, 244, 111, 234, 101, 224, 91, 214, 81, 204, 71, 194, 61, 184, 51, 174, 41, 164, 31, 154, 21, 144, 11, 134, 1, 124, 247, 114, 237, 104, 227, 94, 217, 84, 207, 74, 197, 64, 187, 54, 177, 44, 167, 34, 157, 24, 147, 14, 137, 4, 127, 250, 117, 240, 107, 230, 97, 220, 87, 210, 77, 200, 67, 190, 57, 180, 47, 170, 37, 160, 27, 150, 17, 140, 7, 130, 253, 120, 243, 110, 233, 100, 223, 90, 213, 80, 203, 70, 193, 60, 183, 50, 173, 40, 163, 30, 153, 20, 143, 10, 133, 0, 123, 246, 113, 236, 103, 226, 93, 216, 83, 206, 73, 196, 63, 186, 53, 176, 43, 166, 33, 156, 23]
```
And now using this values, we will create a new dictionary with ascii_dict values and updated keys list:
`decrypt_dict = dict(zip(crypted_ascii, ascii_dict.values()))`

And the final ASCII dictionary should look like this:
```
{18: '\x00', 141: '\x01', 8: '\x02', 131: '\x03', 254: '\x04', 121: '\x05', 244: '\x06', 111: '\x07', 234: '\x08', 101: '\t', 224: '\n', 91: '\x0b', 214: '\x0c', 81: '\r', 204: '\x0e', 71: '\x0f', 194: '\x10', 61: '\x11', 184: '\x12', 51: '\x13', 174: '\x14', 41: '\x15', 164: '\x16', 31: '\x17', 154: '\x18', 21: '\x19', 144: '\x1a', 11: '\x1b', 134: '\x1c', 1: '\x1d', 124: '\x1e', 247: '\x1f', 114: ' ', 237: '!', 104: '"', 227: '#', 94: '$', 217: '%', 84: '&', 207: "'", 74: '(', 197: ')', 64: '*', 187: '+', 54: ',', 177: '-', 44: '.', 167: '/', 34: '0', 157: '1', 24: '2', 147: '3', 14: '4', 137: '5', 4: '6', 127: '7', 250: '8', 117: '9', 240: ':', 107: ';', 230: '<', 97: '=', 220: '>', 87: '?', 210: '@', 77: 'A', 200: 'B', 67: 'C', 190: 'D', 57: 'E', 180: 'F', 47: 'G', 170: 'H', 37: 'I', 160: 'J', 27: 'K', 150: 'L', 17: 'M', 140: 'N', 7: 'O', 130: 'P', 253: 'Q', 120: 'R', 243: 'S', 110: 'T', 233: 'U', 100: 'V', 223: 'W', 90: 'X', 213: 'Y', 80: 'Z', 203: '[', 70: '\\', 193: ']', 60: '^', 183: '_', 50: '`', 173: 'a', 40: 'b', 163: 'c', 30: 'd', 153: 'e', 20: 'f', 143: 'g', 10: 'h', 133: 'i', 0: 'j', 123: 'k', 246: 'l', 113: 'm', 236: 'n', 103: 'o', 226: 'p', 93: 'q', 216: 'r', 83: 's', 206: 't', 73: 'u', 196: 'v', 63: 'w', 186: 'x', 53: 'y', 176: 'z', 43: '{', 166: '|', 33: '}', 156: '~', 23: '\x7f'}
```

We then find the values corresponding to the integers in the integer array and create the string version of the message:
```
# Iterate over int_arr to find their ASCII values, and store them in a result array
result_arr = []
for i in int_arr: 
	result_arr.append(decrypt_dict[i])
	
# Join the result array to get the string result
result_str = ''.join(result_arr)
print(result_str)
```

The output and the final result should look like this in the Figure 1.2.

| ![found the flag](https://user-images.githubusercontent.com/112284234/227734933-d75e5837-4fe4-482e-bdf4-88b8b59b5b02.png) |
|:--:|
| *Figure 1.2* |

And we found the flag.


## Impact

