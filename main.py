import csv
from tabulate import tabulate
import logging
from typing import Dict, List

from src.utils import median, get_args, read_files

logging.basicConfig(
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def main() -> None:
    files, report = get_args()
    rows = read_files(files)
    table_data = median(rows)
    table_data.sort(key=lambda x: x[1], reverse=True)
    print()
    print(tabulate(table_data, headers=['student_name', report]))


if __name__ == "__main__":
    main()