import binascii

print binascii.crc32('{"auth_url": "https://www.evil.example"}' + ' '*2303357834)
print binascii.crc32('{"auth_url": "https://www.google.com"}')
# print 2**33

# import binascii

# t = 'hello'
# tc = binascii.crc32(t)
#
# #padding bytes; start with guess
# p = 0
# ai = '1111aaaa'
# a = ai.ljust(1)
# ac = binascii.crc32(a)
#
# print a
# print len(a)