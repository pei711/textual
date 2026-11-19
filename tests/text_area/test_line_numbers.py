from textual.widgets import TextArea


def test_gutter_width_with_negative_line_numbers() -> None:
    text_area = TextArea("aaa\nbbb\nccc", show_line_numbers=True, line_number_start=-10)

    assert text_area.gutter_width == 5
