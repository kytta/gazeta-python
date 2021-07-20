import gazeta


def test_name():
    """Tests the module's metadata.

    Makes sure that the package supplied metadata fields, such as "__name__"
    and "__package__", hold correct names.
    """
    assert gazeta.__name__ == 'gazeta'
