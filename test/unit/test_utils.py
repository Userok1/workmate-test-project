import pytest
from typing import List, Tuple
from statistics import StatisticsError

from src.utils import read_files, median, get_parser


class TestReadFiles:

    def test_read_one_file(self, single_file):
        files = [single_file]
        table_data = read_files(files)
        assert isinstance(table_data, dict)
        for student_name, spents in table_data.items():
            assert len(spents) > 0
            

    def test_read_multiple_files(self, multiple_files):
        files = [multiple_files[0], multiple_files[1]]
        table_data = read_files(files)
        assert isinstance(table_data, dict)
        for student_name, spents in table_data.items():
            assert len(spents) > 0
        expected_dict = {
            "Алексей Смирнов": [450, 580],
            "Дарья Петрова": [200, 340],
            "Иван Кузнецов": [600, 750]
        }
        assert table_data == expected_dict
            

    def test_read_files_spent_is_not_int(self, bad_file):
        files = [bad_file]
        with pytest.raises(ValueError):
            read_files(files)
            

    def test_read_files_empty_file(self, empty_file):
        files = [empty_file]
        with pytest.raises(StopIteration):
            read_files(files)
            

    def test_read_files_empty_file_with_headers(self, only_headers_file):
        files = [only_headers_file]
        res_dict = read_files(files)
        assert len(res_dict) == 0
        

    def test_read_files_correct_str_to_int_corvert(self, single_file):
        files = [single_file]
        res_dict = read_files(files)
        for val in res_dict.values():
            assert isinstance(val[0], int)


class TestMedian:
    
    def test_median_odd_amount(self):
        data = {"test": [1, 3, 5]}
        median_res = median(data)
        assert len(median_res) > 0
        assert median_res[0][1] == 3
        

    def test_median_even_amount(self):
        data = {"test": [1, 3, 5, 7]}
        median_res = median(data)
        assert len(median_res) > 0
        assert median_res[0][1] == 4
        

    def test_median_no_data(self):
        data = {"test": []}
        with pytest.raises(StatisticsError):
            median(data)
            

    def test_median_one_value(self):
        data = {"test": [1]}
        median_res = median(data)
        assert len(median_res) > 0
        assert median_res[0][1] == 1
        

class TestParser:

    def test_valid_arguments(self, multiple_files):
        parser = get_parser()
        args = parser.parse_args([
            "--files", multiple_files[0], multiple_files[1],
            "--report", "rep"
        ])
        assert args.files[0] == multiple_files[0]
        assert args.files[1] == multiple_files[1]
        assert args.report == "rep"
        

    def test_argument_absense(self):
        parser = get_parser()
        with pytest.raises(SystemExit):
            parser.parse_args([
                "--report", "rep"
            ])
            

    def test_unrecognised_command(self):
        parser = get_parser()
        with pytest.raises(SystemExit):
            parser.parse_args([
                "--files", "file1", "file2",
                "--report", "rep",
                "--invalidcommand"
            ])