from pathlib import Path
from typing import Union


def get_file_format(filename: Union[str, Path]):
    if isinstance(filename, str):
        return filename.split('.')[-1]
    else:
        return str(filename).split('.')[-1]


def get_photo_save_path_url(photos_dir: Union[str, Path], *other_paths) -> str:
    str_paths = [str(path) for path in other_paths]
    joined_paths = '/'.join(str_paths)
    if isinstance(photos_dir, Path):
        return str(photos_dir / joined_paths)
    return photos_dir + '/' + joined_paths
