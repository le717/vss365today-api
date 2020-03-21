from typing import Dict, Tuple

from src.core.config import load_app_config


__all__ = [
    "date_iso_format",
    "make_response",
    "make_error_response"
]


CONFIG = load_app_config()


def date_iso_format(dt) -> str:
    return dt.strftime("%Y-%m-%d")


def make_response(data: dict, status: int) -> Tuple[dict, int]:
    return (data, status)


def make_error_response(msg: str, status: int) -> Tuple[Dict[str, str], int]:
    return make_response({"error_msg": msg}, status)