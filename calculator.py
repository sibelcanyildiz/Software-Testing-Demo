def add(a, b):
    """İki sayıyı toplar."""
    return a + b

def divide(a, b):
    """İki sayıyı böler, sıfıra bölünme hatasını kontrol eder."""
    if b == 0:
        raise ValueError("Bir sayı sıfıra bölünemez!")
    return a / b