from pathlib import Path


def get_abs_path(rel_path):
    base_path = Path(__file__).parent
    file_path = (base_path / ("../../" + rel_path)).resolve()
    return file_path
