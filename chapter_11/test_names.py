def test_names():
    from names import get_formatted_name
    assert get_formatted_name('janis', 'joplin') == 'Janis Joplin'
    assert get_formatted_name('john', 'hooker', 'lee') == 'John Lee Hooker'
    