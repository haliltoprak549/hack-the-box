import sys

# Encrypted message given in the parameters, should provided with the downloaded file from app.hackthebox.com/challenges/228
encrypted_msg = sys.argv[1]

# Revert the hex format to bytes format
bytes_format = bytes.fromhex(encrypted_msg)

# Revert the byte array to an integer array
int_arr = []
for i in bytearray(bytes_format):
	int_arr.append(i)

# The value of the int_arr should look like this:
# [110, 10, 147, 114, 236, 73, 163, 246, 147, 14, 216, 114, 63, 157, 246, 246, 114, 14, 216, 216, 157, 196, 147, 114, 34, 236, 114, 20, 216, 157, 30, 14, 53, 44, 224, 170, 110, 200, 43, 246, 34, 34, 123, 183, 14, 127, 183, 53, 34, 73, 183, 216, 147, 196, 147, 216, 83, 157, 236, 143, 183, 147, 93, 73, 14, 127, 157, 34, 236, 137, 183, 163, 34, 236, 143, 216, 14, 127, 137, 33]

# ASCII codes of the chars
ascii_dict = {i: chr(i) for i in range(128)}

# ascii_dict dictionary should look like this:
# {0: '\x00', 1: '\x01', 2: '\x02', 3: '\x03', 4: '\x04', 5: '\x05', 6: '\x06', 7: '\x07', 8: '\x08', 9: '\t', 10: '\n', 11: '\x0b', 12: '\x0c', 13: '\r', 14: '\x0e', 15: '\x0f', 16: '\x10', 17: '\x11', 18: '\x12', 19: '\x13', 20: '\x14', 21: '\x15', 22: '\x16', 23: '\x17', 24: '\x18', 25: '\x19', 26: '\x1a', 27: '\x1b', 28: '\x1c', 29: '\x1d', 30: '\x1e', 31: '\x1f', 32: ' ', 33: '!', 34: '"', 35: '#', 36: '$', 37: '%', 38: '&', 39: "'", 40: '(', 41: ')', 42: '*', 43: '+', 44: ',', 45: '-', 46: '.', 47: '/', 48: '0', 49: '1', 50: '2', 51: '3', 52: '4', 53: '5', 54: '6', 55: '7', 56: '8', 57: '9', 58: ':', 59: ';', 60: '<', 61: '=', 62: '>', 63: '?', 64: '@', 65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E', 70: 'F', 71: 'G', 72: 'H', 73: 'I', 74: 'J', 75: 'K', 76: 'L', 77: 'M', 78: 'N', 79: 'O', 80: 'P', 81: 'Q', 82: 'R', 83: 'S', 84: 'T', 85: 'U', 86: 'V', 87: 'W', 88: 'X', 89: 'Y', 90: 'Z', 91: '[', 92: '\\', 93: ']', 94: '^', 95: '_', 96: '`', 97: 'a', 98: 'b', 99: 'c', 100: 'd', 101: 'e', 102: 'f', 103: 'g', 104: 'h', 105: 'i', 106: 'j', 107: 'k', 108: 'l', 109: 'm', 110: 'n', 111: 'o', 112: 'p', 113: 'q', 114: 'r', 115: 's', 116: 't', 117: 'u', 118: 'v', 119: 'w', 120: 'x', 121: 'y', 122: 'z', 123: '{', 124: '|', 125: '}', 126: '~', 127: '\x7f'}

# Find the values of ASCII codes after implementing (123 * char + 18) % 256 formula to them
crypted_ascii = []
for i in range(0, 128):
	crypted_ascii.append((123 * i + 18) % 256)
	
# crypted_ascii list should look like this:
# [18, 141, 8, 131, 254, 121, 244, 111, 234, 101, 224, 91, 214, 81, 204, 71, 194, 61, 184, 51, 174, 41, 164, 31, 154, 21, 144, 11, 134, 1, 124, 247, 114, 237, 104, 227, 94, 217, 84, 207, 74, 197, 64, 187, 54, 177, 44, 167, 34, 157, 24, 147, 14, 137, 4, 127, 250, 117, 240, 107, 230, 97, 220, 87, 210, 77, 200, 67, 190, 57, 180, 47, 170, 37, 160, 27, 150, 17, 140, 7, 130, 253, 120, 243, 110, 233, 100, 223, 90, 213, 80, 203, 70, 193, 60, 183, 50, 173, 40, 163, 30, 153, 20, 143, 10, 133, 0, 123, 246, 113, 236, 103, 226, 93, 216, 83, 206, 73, 196, 63, 186, 53, 176, 43, 166, 33, 156, 23]

# Create a dictionary with updated ASCII codes and their values
decrypt_dict = dict(zip(crypted_ascii, ascii_dict.values()))

# decrypt_dict dictionary should look like this:
# {18: '\x00', 141: '\x01', 8: '\x02', 131: '\x03', 254: '\x04', 121: '\x05', 244: '\x06', 111: '\x07', 234: '\x08', 101: '\t', 224: '\n', 91: '\x0b', 214: '\x0c', 81: '\r', 204: '\x0e', 71: '\x0f', 194: '\x10', 61: '\x11', 184: '\x12', 51: '\x13', 174: '\x14', 41: '\x15', 164: '\x16', 31: '\x17', 154: '\x18', 21: '\x19', 144: '\x1a', 11: '\x1b', 134: '\x1c', 1: '\x1d', 124: '\x1e', 247: '\x1f', 114: ' ', 237: '!', 104: '"', 227: '#', 94: '$', 217: '%', 84: '&', 207: "'", 74: '(', 197: ')', 64: '*', 187: '+', 54: ',', 177: '-', 44: '.', 167: '/', 34: '0', 157: '1', 24: '2', 147: '3', 14: '4', 137: '5', 4: '6', 127: '7', 250: '8', 117: '9', 240: ':', 107: ';', 230: '<', 97: '=', 220: '>', 87: '?', 210: '@', 77: 'A', 200: 'B', 67: 'C', 190: 'D', 57: 'E', 180: 'F', 47: 'G', 170: 'H', 37: 'I', 160: 'J', 27: 'K', 150: 'L', 17: 'M', 140: 'N', 7: 'O', 130: 'P', 253: 'Q', 120: 'R', 243: 'S', 110: 'T', 233: 'U', 100: 'V', 223: 'W', 90: 'X', 213: 'Y', 80: 'Z', 203: '[', 70: '\\', 193: ']', 60: '^', 183: '_', 50: '`', 173: 'a', 40: 'b', 163: 'c', 30: 'd', 153: 'e', 20: 'f', 143: 'g', 10: 'h', 133: 'i', 0: 'j', 123: 'k', 246: 'l', 113: 'm', 236: 'n', 103: 'o', 226: 'p', 93: 'q', 216: 'r', 83: 's', 206: 't', 73: 'u', 196: 'v', 63: 'w', 186: 'x', 53: 'y', 176: 'z', 43: '{', 166: '|', 33: '}', 156: '~', 23: '\x7f'}

# Iterate over int_arr to find their ASCII values, and store them in a result array
result_arr = []
for i in int_arr: 
	result_arr.append(decrypt_dict[i])
	
# Join the result array to get the string result
result_str = ''.join(result_arr)
print(result_str)

# The output should look like this:
# Th3 nucl34r w1ll 4rr1v3 0n fr1d4y.
# HTB{l00k_47_y0u_r3v3rs1ng_3qu4710n5_c0ngr475}
