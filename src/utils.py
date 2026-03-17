import argparse
from statistics import median as stat_median
import csv
import logging
from typing import List, Tuple, Dict

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def median(rows: Dict[str, List[int]]) -> List[Tuple[str, float]]:
    result_lst = []
    for student_name, coffee_spent in rows.items():
        # logger.info(f"{student_name} потратила на кофе: {coffee_spent}")
        result_lst.append((student_name, stat_median(coffee_spent)))
    return result_lst


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", type=str, nargs="+", required=True)
    parser.add_argument("--report", type=str, required=True)
    
    return parser


def get_args():
    parser = get_parser()
    args = parser.parse_args()
    files = args.files
    report = args.report
    
    return files, report


def read_files(files: List[str]) -> Dict[str, List[int]]:
    students_spent = {}
    for f in files:
        # logger.info(f"File {f}")
        with open(f, 'r', newline='', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)
            for row in csvreader:
                students_spent.setdefault(row[0], []).append(int(row[2]))
    return students_spent


if __name__ == "__main__":
    files = ["empty_with_headers.csv"]
    res = read_files(files)
    print(res)