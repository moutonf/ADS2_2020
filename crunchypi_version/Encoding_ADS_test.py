
import string
import Encoding_ADS as enc


# Test cases are structured as nested lists inside 'cases', where
# index 0 represents content to be encoded; index 1 represents 
# shift amount; and index 2 represents expected encoding results.
# Note, these cases are written for the english alphabet.
# 
# Test case results generated with https://www.boxentriq.com/code-breaking/caesar-cipher
cases = [
    # Normal case.
    ["version control system is fun", 4,"zivwmsr gsrxvsp wcwxiq mw jyr"],
    # Check bounds handling.
    ["version control system is fun", -4,"ranoekj ykjpnkh ouopai eo bqj"],
    ["version control system is fun", 999,"gpcdtzy nzyeczw djdepx td qfy"],
    # Multiple alphabets (lower & upper).
    ["VeRsIoN CoNtRoL SySteM Is FuN", 4,"ZiVwMsR GsRxVsP WcWxiQ Mw JyR"],
    ["VeRsIoN CoNtRoL SySteM Is FuN", -4,"RaNoEkJ YkJpNkH OuOpaI Eo BqJ"]
]



def test_encoding(case:list):
    content, shift, expect = case
    r = enc.encode(
        alphabets=[string.ascii_lowercase, string.ascii_uppercase],
        content=content,
        shift=shift
    )
    if r !=  expect:
        return f"failed to encode. wanted '{expect}' but got '{r}'"

def test_decoding(case:list):
    expect, shift, content = case
    r = enc.decode(
        alphabets=[string.ascii_lowercase, string.ascii_uppercase],
        content=content,
        shift=shift
    )
    if r !=  expect:
        return f"failed to encode. wanted '{expect}' but got '{r}'"


# Run all test cases with all funcs.
testfuncs = [test_encoding, test_decoding]
for f in testfuncs:
    for i, case in enumerate(cases):
        status = f'{f.__name__} case {i}: '
        errmsg = f(case)
        status += f"fail ({errmsg})" if errmsg else "ok"
        print(status)

