import pytest
from string_utils import StringUtils


# Принимает на вход текст, делает первую букву заглавной
# и возвращает этот же текст

# Позитивные тесты
@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("testing", "Testing"),   # обычная строка
        ("Capital", "Capital"),   # строка с заглавной буквой
        ("a few words", "A few words"),  # строка с пробелами
        ("  space", "  space"),  # пробелы в начале
        ("REGISTERdifference", "Registerdifference"),  # разный регистр
        ("!@#$", "!@#$"),   # строка со спецсимволами
        ("", ""),  # пустая строка
        (" ", " "),  # строка с одним пробелом
        ("    ", "    ")  # строка с несколькими пробелами
    ],
)
def test_capitalize_positive(input_string, expected_output):
    utils = StringUtils()
    assert utils.capitilize(input_string) == expected_output


# Негативные тесты
@pytest.mark.parametrize(
    "input_string",
    [
        12345,  # число вместо строки
        None,   # отсутствие значения
        [1, 2, 3]  # список вместо строки
    ],
)
@pytest.mark.xfail(raises=AttributeError)  # AttributeError для неверного типа
def test_capitalize_negative(input_string):
    utils = StringUtils()
    utils.capitilize(input_string)


# Принимает на вход текст и удаляет пробелы в начале, если они есть

# Позитивные тесты
@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("  space", "space"),  # пробелы в начале
        ("nospace", "nospace"),  # строка без пробелов
        ("   !@#$", "!@#$"),   # строка со спецсимволами и пробелами
        ("   ", ""),  # только пробелы, ожидаем пустую строку
        ("", "")  # пустая строка
    ],
)
def test_trim_positive(input_string, expected_output):
    utils = StringUtils()
    assert utils.trim(input_string) == expected_output


# Негативные тесты
@pytest.mark.parametrize(
    "input_string",
    [
        12345,  # число вместо строки
        None,   # отсутствие значения
        [1, 2, 3]  # список вместо строки
    ],
)
# ожидаем AttributeError для неверного типа
@pytest.mark.xfail(raises=AttributeError)
def test_trim_negative(input_string):
    utils = StringUtils()
    utils.trim(input_string)


# Принимает на вход текст с разделителем и возвращает список строк

# Позитивные тесты
@pytest.mark.parametrize(
    "input_string, delimeter, expected_output",
    [
        ("a,a,b,b", ",", ["a", "a", "b", "b"]),  # буквы через запятую
        ("7:7:7", ":", ["7", "7", "7"]),  # разделитель двоеточие
        ("new,now,mew", ",", ["new", "now", "mew"]),  # текст через запятую
        ("", ",", []),  # пустая строка
        (" , ", ",", [" ", " "]),  # строка с пробелами, как два элемента
        (",", ",", ["", ""]),  # строка с разделителем только
        (",,a,b,", ",", ["", "", "a", "b", ""]),  # строки с несколькими
    ],                                            # разделителями
)
def test_to_list_positive(input_string, delimeter, expected_output):
    utils = StringUtils()
    assert utils.to_list(input_string, delimeter) == expected_output


# Негативные тесты
@pytest.mark.parametrize(
    "input_string, delimeter",
    [
        (12345, ","),  # число вместо строки
        (None, ","),  # отсутствие значения
        ([1, 2, 3], ",")  # список вместо строки
    ],
)
# ожидаем AttributeError для неверного типа
@pytest.mark.xfail(raises=AttributeError)
def test_to_list_negative(input_string, delimeter):
    utils = StringUtils()
    utils.to_list(input_string, delimeter)


# Возвращает `True`, если строка содержит искомый символ и `False` - если нет

# Позитивные тесты
@pytest.mark.parametrize(
    "input_string, symbol, expected_output",
    [
        ("Alphabet", "a", True),  # символ в начале строки
        ("Beautiful", "l", True),  # символ в конце строки
        ("Ginger", "n", True),  # символ в середине строки
        ("Halloween", "v", False),  # символ, которого нет в строке
        ("", "f", False),  # пустая строка
        ("Hi, kid!", ",", True),  # специальный символ
        ("1408", "0", True)  # число как символ
    ],
)
def test_contains_positive(input_string, symbol, expected_output):
    utils = StringUtils()
    assert utils.contains(input_string, symbol) == expected_output


# Негативные тесты
@pytest.mark.parametrize(
    "input_string, symbol",
    [
        (None, "a"),  # отсутствие значения вместо строки
        ("test", None),  # отсутствие значения вместо искомого символа
        (12345, "5"),  # число вместо строки
        ([], "a"),  # список вместо строки
        ("test", ["a"])  # список вместо искомого символа
    ],
)
# ожидаем AttributeError или TypeError для неверного типа
@pytest.mark.xfail(raises=(AttributeError, TypeError))
def test_contains_negative(input_string, symbol):
    utils = StringUtils()
    utils.contains(input_string, symbol)


# Удаляет все подстроки из переданной строки

# Позитивные тесты
@pytest.mark.parametrize(
    "input_string, symbol, expected_output",
    [
        ("Alphabet", "h", "Alpabet"),  # удаление символа из строки
        ("Beautiful", "l", "Beautifu"),  # удаление символа в конце
        ("Hi, kid!", "i", "H, kd!"),  # удаление символа из предложения
        ("babcdbcb", "b", "acdc"),  # удаление нескольких символов
        ("", "f", ""),  # пустая строка
        ("fffffff", "f", ""),  # удаление всех символов
        ("88005553535", "5", "880033"),  # удаление числа
    ],
)
def test_delete_symbol_positive(input_string, symbol, expected_output):
    utils = StringUtils()
    assert utils.delete_symbol(input_string, symbol) == expected_output


# Негативные тесты
@pytest.mark.parametrize(
    "input_string, symbol",
    [
        (None, "a"),  # отсутствие значения вместо строки
        ("testing", None),  # отсутствие значения вместо символа
        (12345, "5"),   # число вместо строки
        ([], "a"),  # список вместо строки
        ("testing", ["a"])  # список вместо символа
    ],
)
# ожидаем AttributeError или TypeError для неверного типа
@pytest.mark.xfail(raises=(AttributeError, TypeError))
def test_delete_symbol_negative(input_string, symbol):
    utils = StringUtils()
    utils.delete_symbol(input_string, symbol)


# Возвращает `True`, если строка начинается с заданного символа
# и `False` - если нет

# Позитивные тесты
@pytest.mark.parametrize(
    "input_string, symbol, expected_output",
    [
        ("Alphabet", "A", True),  # начинается с заданной буквы
        ("Beautiful", "U", False),  # начинается не с заданной буквы
        ("123444", "1", True),  # число передается как строка
        ("", "a", False),  # пустая строка
        (" Space", " ", True)  # начинается с пробела
    ],
)
def test_starts_with_positive(input_string, symbol, expected_output):
    utils = StringUtils()
    assert utils.starts_with(input_string, symbol) == expected_output


# Негативные тесты
@pytest.mark.parametrize(
    "input_string, symbol",
    [
        (None, "a"),  # отсутствие значения вместо строки
        ("testing", None),  # отсутствие значения вместо символа
        (12345, "5"),  # число вместо строки
        ([], "a"),  # список вместо строки
        ("testing", ["a"])  # список вместо символа
    ],
)
# ожидаем AttributeError или TypeError для неверного типа
@pytest.mark.xfail(raises=(AttributeError, TypeError))
def test_starts_with_negative(input_string, symbol):
    utils = StringUtils()
    utils.starts_with(input_string, symbol)


# Возвращает `True`, если строка заканчивается заданным символом
#  и `False` - если нет

# Позитивные тесты
@pytest.mark.parametrize(
    "input_string, symbol, expected_output",
    [
        ("Alphabet", "t", True),  # заканчивается на заданную букву
        ("Hi, kid", "d", True),  # строка заканчивается на заданную букву
        ("Gemini", "e", False),  # не заканчивается на заданную букву
        ("", "", True),  # пустая строка заканчивается на пустую строку
        ("Testing123", "3", True),  # строка заканчивается на заданную цифру
        ("Testing456", "8", False)  # строка не заканчивается на заданную цифру
    ],
)
def test_end_with_positive(input_string, symbol, expected_output):
    utils = StringUtils()
    assert utils.end_with(input_string, symbol) == expected_output


# Негативные тесты
@pytest.mark.parametrize(
    "input_string, symbol",
    [
        (12345, "5"),  # число вместо строки
        (None, "o"),  # отсутствие значения вместо строки
        ([1, 2, 3], "3")  # список вместо строки
    ],
)
@pytest.mark.xfail(raises=AttributeError)  # ожидаем ошибку AttributeError
def test_end_with_negative(input_string, symbol):
    utils = StringUtils()
    utils.end_with(input_string, symbol)


# Возвращает `True`, если строка пустая и `False` - если нет

# Позитивные проверки
@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("", True),  # пустая строка
        (" ", True),  # строка с пробелом
        ("   ", True),  # строка с тремя пробелами
        ("Testing", False),  # не пустая строка
        (" f ", False)  # не пустая строка: буква с пробелами по краям
    ],
)
def test_is_empty_positive(input_string, expected_output):
    utils = StringUtils()
    assert utils.is_empty(input_string) == expected_output


# Негативные тесты
@pytest.mark.parametrize(
    "input_string",
    [
        12345,  # число вместо строки
        None,  # отсутствие значения вместо строки
        [1, 2, 3]  # список вместо строки
    ],
)
@pytest.mark.xfail(raises=AttributeError)  # ожидаем ошибку AttributeError
def test_is_empty_negative(input_string):
    utils = StringUtils()
    utils.is_empty(input_string)


# Преобразует список элементов в строку с указанным разделителем

# Позитивные проверки
@pytest.mark.parametrize(
    "input_list, joiner, expected_output",
    [
        ([3, 1, 0, 5], ", ", "3, 1, 0, 5"),  # список чисел
        (["Hi", "kid"], ", ", "Hi, kid"),  # список строк
        (["Walkie", "talkie"], "-", "Walkie-talkie"),  # разделитель "-"
        ([], ", ", ""),  # пустой список
        (["Uno"], ", ", "Uno"),  # список с одним элементом
        ([1, "dos", 3.14], ", ", "1, dos, 3.14"),  # смешанные типы данных
        (["b", "b", "c"], ":", "b:b:c"),  # разделитель ":"
    ],
)
def test_list_to_string_positive(input_list, joiner, expected_output):
    utils = StringUtils()
    assert utils.list_to_string(input_list, joiner) == expected_output


# Негативные тесты
@pytest.mark.parametrize(
    "input_list, joiner",
    [
        ([12345], ","),  # список с числом
        (None, ","),  # отсутствие значения вместо списка
        ("stroka", ","),  # строка вместо списка
        ([1, 2, 3, 4], None)  # список с отсутствующим значением разделителя
    ],
)
# Ожидаем ошибку TypeError
@pytest.mark.xfail(raises=TypeError)
def test_list_to_string_negative(input_list, joiner):
    utils = StringUtils()
    utils.list_to_string(input_list, joiner)
