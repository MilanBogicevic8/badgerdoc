from dev_runner.conf import settings

from .base_runner import BaseRunner


class ConvertRunner(BaseRunner):
    PACKAGE_NAME = "convert"
    PORT = settings.CONVERT_PORT
    APP_NAME = "convert"
    ENVIRONMENT = {"IMPORT_COCO_URL": "http://0.0.0.0:8080/converter/import/"}