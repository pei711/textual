from textual.content import Span
from textual.fuzzy import FuzzySearch, Matcher
from textual.style import Style


def test_no_match():
    """Check non matching score of zero."""
    matcher = Matcher("x")
    assert matcher.match("foo") == 0


def test_empty_query():
    """Regression test for https://github.com/Textualize/textual/issues/6776."""
    candidate = "Toggle dark mode"
    matcher = Matcher("")

    assert matcher.match(candidate) == 0
    assert matcher.highlight(candidate).spans == []
    assert FuzzySearch().match("", candidate) == (0.0, [])


def test_match_single_group():
    """Check that single groups rang higher."""
    matcher = Matcher("abc")
    assert matcher.match("foo abc bar") > matcher.match("fooa barc")


def test_boosted_matches():
    """Check first word matchers rank higher."""
    matcher = Matcher("ss")

    # First word matchers should score higher
    assert matcher.match("Save Screenshot") > matcher.match("Show Keys abcde")


def test_highlight():
    matcher = Matcher("foo.bar")

    spans = matcher.highlight("foo/egg.bar").spans
    print(repr(spans))
    assert spans == [
        Span(0, 1, Style(reverse=True)),
        Span(1, 2, Style(reverse=True)),
        Span(2, 3, Style(reverse=True)),
        Span(7, 8, Style(reverse=True)),
        Span(8, 9, Style(reverse=True)),
        Span(9, 10, Style(reverse=True)),
        Span(10, 11, Style(reverse=True)),
    ]
