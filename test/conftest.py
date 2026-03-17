import pytest


@pytest.fixture
def single_table_data():
    csv_t1_data = "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"\
    "Алексей Смирнов,2024-06-01,450,4.5,12,норм,Математика\n"\
    "Дарья Петрова,2024-06-01,200,7.0,6,отл,Математика\n"\
    "Иван Кузнецов,2024-06-01,600,3.0,15,зомби,Математика\n"
    return csv_t1_data


@pytest.fixture
def multiple_tables_data(single_table_data):
    csv_t2_data = "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"\
    "Алексей Смирнов,2024-06-08,580,3.0,17,зомби,Физика\n"\
    "Дарья Петрова,2024-06-08,340,5.5,9,устал,Физика\n"\
    "Иван Кузнецов,2024-06-08,750,1.5,20,труп,Физика\n"
    return single_table_data, csv_t2_data


@pytest.fixture
def bad_table_data():
    csv_bad_table = \
    """
    student,date,coffee_spent,sleep_hours,study_hours,mood,exam
    Дарья Петрова,2024-06-02,250.0,6.5,8,норм,Математика
    Дарья Петрова,2024-06-03,300.0,6.0,9,норм,Математика
    Иван Кузнецов,2024-06-01,600.3,3.0,15,зомби,Математика
    """
    return csv_bad_table


@pytest.fixture
def single_file(tmp_path, single_table_data):
    t1_file = tmp_path / "table_1.csv" 
    t1_file.write_text(single_table_data, encoding='utf-8')
    return str(t1_file)


@pytest.fixture
def multiple_files(tmp_path, multiple_tables_data):
    t1_table = tmp_path / "table_1.csv"
    t2_table = tmp_path / "table_2.csv"
    t1_table.write_text(multiple_tables_data[0], encoding='utf-8')
    t2_table.write_text(multiple_tables_data[1], encoding='utf-8')
    return str(t1_table), str(t2_table)


@pytest.fixture
def bad_file(tmp_path, bad_table_data):
    bad_table = tmp_path / "bad_table.csv"
    bad_table.write_text(bad_table_data, encoding='utf-8')
    return str(bad_table)


@pytest.fixture
def empty_file(tmp_path):
    empty_table = tmp_path / "bad_table.csv"
    empty_table.write_text("", encoding="utf-8")
    return str(empty_table)


@pytest.fixture
def only_headers_file(tmp_path):
    only_headers_string = "student,date,coffee_spent,sleep_hours,study_hours,mood,exam"
    table_only_headers = tmp_path / "only_headers_table.csv"
    table_only_headers.write_text(only_headers_string, encoding='utf-8')
    return str(table_only_headers)