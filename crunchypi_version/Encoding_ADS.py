'''
Module contains funcs for a ceaser cipher implementation

'''



def _alphashifter(alphabet:str, content:str, shift:int) -> str:
    ''' General-purpose func for shifting characters in 'content'
        by 'shift' amount (with wrap), using a specified alphabet.
        Example:
            alphabet='abcd'
            content='a99'
            shift=5

            this would give 'b99' because 'a' was shifted around the
            alphabet a complete turn + 1, and '99' was ignored since
            it was not given in the alphabet.
    '''
    # Convert alphabet to dict for performance.
    alphamap = {c:i for i,c in enumerate(alphabet)}

    res = ''
    for char in content:
        position_old = alphamap.get(char)
        # Ignore character if it is not in the alphabet.
        if position_old == None:
            res += char
            continue

        res += alphabet[(position_old+shift)%len(alphabet)]
    return res


def encode(alphabets:list, content:str, shift:int) -> str:
    ''' Implementation of Caesar Cipher encoding. The specified
        content will be shifted by 'shift' amount (with wrap),
        using the specified alphabets (english lower, english
        upper, etc). Note that if a character in 'contant' appears
        in multiple alphabets, then the last one will be used.
    '''
    for alphabet in alphabets:
        content = _alphashifter(alphabet=alphabet, content=content, shift=shift)

    return content


def decode(alphabets:list, content:str, shift:int) -> str:
    ''' Implementation of Caesar Cipher decoding. Reverses
        encoding done with the 'encode' func found in this mod.
    '''
    for alphabet in alphabets:
        # Simply invert the shift to reverse encoding.
        content = _alphashifter(alphabet=alphabet, content=content, shift=shift*-1)

    return content


