import utils.file_tools.globals as g
import pytest

d = g.SEPARATORS
get_key_params = [
    (d, '|', 'psv'),
    (d, '\t', 'tsv'),
    (d, ',', 'csv'),
]
@pytest.mark.parametrize('d, value, expected', get_key_params)
def test_get_key(d, value, expected):
    # invoke
    actual = g.get_key(d, value)
    # analyze
    assert actual == expected

# gives (sep, ext) pairs
both = [(g.SEPARATORS[key], key, False, (g.SEPARATORS[key], key)) for key in g.SEPARATORS]
# gives (sep, None) pairs
sep_only = [(g.SEPARATORS[key], None, False, (g.SEPARATORS[key], key)) for key in g.SEPARATORS]
# gives (None, ext) pairs
ext_only = [(None, key, False, (g.SEPARATORS[key], key)) for key in g.SEPARATORS]
handle_sep_ext_params = [
    *both, *sep_only, *ext_only,
    ("", "", True, ("", "")),
    (",", "tsv", True, (",", "tsv")),
    (",", "tsv", False, (ValueError(g.SEP_EXT_DONT_MATCH_ERROR.format(sep=",", ext='tsv')))),
    ("BAD_SEP", None, False, (ValueError(g.INVALID_SEP.format(sep="BAD_SEP")))),
    ("BAD_SEP", "BAD_EXT", False, (ValueError(g.INVALID_EXT.format(ext="BAD_EXT")))),
    (None, "BAD_EXT", False, (ValueError(g.INVALID_EXT.format(ext="BAD_EXT")))),
    (None, None, False, (",", "csv")),
    (None, None, True, (ValueError(g.NONSTRING_SEP_W_FORCE.format(sep=None)))),
    ("sep", None, True, (ValueError(g.NONSTRING_EXT_W_FORCE.format(ext=None)))),
    (None, "ext", True, (ValueError(g.NONSTRING_SEP_W_FORCE.format(sep=None)))),
]
@pytest.mark.parametrize("sep, ext, force, expected", handle_sep_ext_params)
def test_handle_sep_ext(sep, ext, force, expected):
    # invoke
    try:
        actual = g.handle_sep_ext(sep, ext, force)
    except ValueError as e:
        expected = (type(expected), expected.args)
        actual = (type(e), e.args)
    assert actual == expected