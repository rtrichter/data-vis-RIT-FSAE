SEP_EXT_DONT_MATCH_ERROR = "extension ({ext}) does not match separator ({sep})"
INVALID_SEP = "The separator ({sep}) is not supported. Try using force=True or updating the sep/ext configuration"
INVALID_EXT = "The extension ({ext}) is not supported. Try using force=True or updating the sep/ext configuration"
NONSTRING_EXT_W_FORCE = "Extension {ext} must be a string but is not"
NONSTRING_SEP_W_FORCE = "Separator {sep} must be a string but is not"

SEPARATORS = {
    "csv": ',',
    "tsv": '\t',
    "psv": '|'
}

def get_key(d, value):
    return list(d.keys())[list(d.values()).index(value)]

def handle_sep_ext(sep=None, ext=None, force=False):
    # if you use force, the program will 
    # attempt to use potentially invalid separators

    if force:
        if type(sep) != str:
            raise ValueError(NONSTRING_SEP_W_FORCE.format(sep=sep))
        if type(ext) != str:
            raise ValueError(NONSTRING_EXT_W_FORCE.format(ext=ext))
        else:
            return sep, ext

    # input checks    
    if not (ext is None):
        if ext not in SEPARATORS.keys():
            raise ValueError(INVALID_EXT.format(ext=ext))
    
    if not (sep is None):
        if sep not in SEPARATORS.values():
            raise ValueError(INVALID_SEP.format(sep=sep))

    # assume csv
    if sep is None and ext is None:
        sep = ","
        ext = "csv"
        return sep, ext

    # if only given extension
    if not (ext is None) and sep is None:
        sep = SEPARATORS[ext]
        return sep, ext

    # if only given sep
    if not (sep is None) and ext is None:
        ext = get_key(SEPARATORS, sep)

    # if both were given 
    if sep is None or ext is None:
        raise RuntimeError(f"This should never happen but either sep ({sep}) or ext ({ext}) is None")

    if SEPARATORS[ext] != sep:
        raise ValueError(SEP_EXT_DONT_MATCH_ERROR.format(sep=sep, ext=ext))

    return sep, ext

            