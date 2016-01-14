nfirvine/crc-collision.py
=========================

Implements a naive brute force attack on CRC32. Given a target string `t` and an evil string `a`, finds the number of padding ' ' bytes needed to be appended to `a` such that `crc32(a+padding) == crc(t)`. This would work fine on e.g., Python's JSON parser, which ignores extra whitespace.

On my Macbook Pro (2.6 GHz Intel Core i5), does about 200,000 attempts/second. If we assume CRC32 is evenly distributed (probably not), we can get values for all digests in 6 hours.

Shows that CRC32 is insecure simply on the basis collisions being not unlikely.

Improvements
============

- Divide the search space and distribute the problem among threads or CPUs.
- Keep messages shorter by allowing more whitespace/no-op characters and cycling through them (needs more domain knowledge)
- There's certainly a way to coerce `crc32(a+padding)` towards `crc32(t)` without brute force
