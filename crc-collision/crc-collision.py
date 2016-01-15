#!/usr/bin/python
#Naive brute-forcing of CRC32 using spaces
import binascii

t = '{"auth_url": "https://www.google.com"}'
tc = binascii.crc32(t)

#padding bytes; start with guess
p = 0
ai = '{"auth_url": "https://www.evil.example"}'
a = ai.ljust(p - len(ai))
ac = binascii.crc32(a)

attempt = 1

while True:
    if ac == tc:
        print 'Found in %i attempts: "%s" + " "*%i' % (attempt, ai, p-1)
        break
    if attempt % 1000000 == 0:
        print 'Attempt %i (p=%i): %s != %s' % (attempt, p, tc, ac)
    if p % 2**32 == 0:
        print 'Wrapped'
        ac = binascii.crc32(ai)
        p = 1
    else:
        ac = binascii.crc32(' ', ac)
        p += 1
    attempt += 1
