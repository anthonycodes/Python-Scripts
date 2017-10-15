# Steganography Cypher Program
Original name, I know.

This is a command line utility designed to keep strings encrypted.
When encrypted your string should look something like this:

7ca1FaA36B1a6d3e83d002695B260e0c:+Ba^I3.3a^
The format is like so: <encrypted-string>:<verifier>

The verifier should only be used when comparing important strings, such as passwords.
It should never be used when storing other things as, it is used to identify the sum of character > scv values.

In other words, let's say we're encrypting "abc".
Let's also say in your config.py, a = 1000, b = 2000, and c = 3000.
If we looked at the verifier (without it being obfuscated) it would read 6000.
The trouble with this is, if the attacker knew what your values are, he could go through all of them and see which combinations make up 6000.
This issue was fixed in 0.2 luckliy.
