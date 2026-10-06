from extract import transform


def test_transform():
    rows = [
        ["name", "age"],
        ["Malu", "22"],
        ["Anu", "23"]
    ]

    result = transform(rows)

    assert result == rows