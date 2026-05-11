import pytest
from calculator import add, divide

# Başarılı toplama testi
def test_add_success():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

# Başarılı bölme testi
def test_divide_success():
    assert divide(10, 2) == 5

# Hata durumu testi (Validation: Beklenen hata oluşuyor mu?)
def test_divide_by_zero():
    with pytest.raises(ValueError, match="Bir sayı sıfıra bölünemez!"):
        divide(10, 0)