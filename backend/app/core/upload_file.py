import os
from datetime import datetime

import aiofiles
from fastapi import UploadFile

from configs import app_configs


async def upload_file(file: UploadFile, path="images/"):
    if not os.path.exists(app_configs.MEDIA_ROOT / path):
        os.makedirs(app_configs.MEDIA_ROOT / path)
        # logger.debug("Created path: %s", app_configs.MEDIA_ROOT / link)
    timestamp = datetime.timestamp(datetime.now())
    filename = "{:.4f}_{}".format(timestamp, file.filename)
    contents = await file.read()
    async with aiofiles.open(
            mode="wb", file=app_configs.MEDIA_ROOT / path / filename
    ) as f:
        await f.write(contents)

    return path + filename
