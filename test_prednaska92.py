import pytest
from prednaska92 import deleni

def test_deleni():
    assert deleni(10, 2) == 5
    assert deleni(1, 1) == 1

def test_deleni_nulou():
    with pytest.raises(ZeroDivisionError) as exc_info:
        deleni(10, 0)
    assert "Nelze dělit nulou" in str(exc_info.value)
