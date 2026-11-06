import requests
import time
import logging
from pathlib import Path

from config.settings import BASE_URL,TIMEOUT



# 创建日志目录
PROJECT_ROOT = Path(__file__).resolve().parent.parent
LOG_DIR = PROJECT_ROOT / "logs"
LOG_DIR.mkdir(parents=True,exist_ok=True)


LOG_FILE = LOG_DIR / "test_run.log"


# 配置日志记录器
logger = logging.getLogger("api_test")
logger.setLevel(logging.INFO)
logger.propagate = False


# 避免重复添加日志处理器
if not logger.handlers:
    handler = logging.FileHandler(LOG_FILE,encoding="utf-8")
    formatter = logging.Formatter(
        " %(asctime)s| %(levelname)s | %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)


class APIclient:
    def __init__(self):
        self.session = requests.Session()


    def request(self, method, path, **kwargs):
        url = f"{BASE_URL}{path}"

        kwargs.setdefault("timeout", TIMEOUT)

        start_time = time.perf_counter()

        try:
            response = self.session.request(
                url=url,
                method=method,
                **kwargs
            )

            elapsed = time.perf_counter() - start_time

            logger.info(
                "%s %s | status=%s | elapsed=%.3fs",
                method.upper(),
                url,
                response.status_code,
                elapsed
            )

            return response

        except requests.RequestException:
            elapsed = time.perf_counter() - start_time

            logger.exception(
                "%s %s | request failed | elapsed=%.3fs",
                method.upper(),
                url,
                elapsed
            )

            raise


    def get(self,path,**kwargs):
        return self.request("GET",path,**kwargs)


    def post(self,path,**kwargs):
         return self.request("POST",path,**kwargs)


    def close(self):
        self.session.close()



