import re
import json
import aiofiles
from typing import Dict
from pathlib import Path


async def load_json(path: Path | str) -> Dict[str, str]:
    async with aiofiles.open(
        file=path,
        mode='r',
        encoding='utf-8'
    ) as file:
        data = await file.read()
        return json.loads(data)


def format_phone(phone: str) -> str:
    digits = re.sub(
        pattern='\D',
        repl='',
        string=phone
    )
    if len(digits) == 11 and digits.startswith('8'):
        digits = '7' + digits[1:]
    elif len(digits) == 10 and digits.startswith('9'):
        digits = '7' + digits
    return f"+{digits[0]}({digits[1:4]}){digits[4:7]}-{digits[7:9]}-{digits[9:11]}"


def validate_phone(phone: str) -> bool:
    pattern = r'\+\d\(\d{3}\)\d{3}-\d{2}-\d{2}'
    return bool(re.fullmatch(
        pattern=pattern,
        string=phone
    ))