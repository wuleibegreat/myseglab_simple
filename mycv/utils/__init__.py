from .config import Config, DictAction
from .path import check_file_exist


try:
    import torch
except ImportError:
    __all__ = [
        'Config', 'DictAction', 'check_file_exist'
    ]