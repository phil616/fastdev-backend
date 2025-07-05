import sys
from datetime import datetime
from pathlib import Path

from loguru import logger as _logger

# 日志存储路径
LOG_DIR = Path("logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

# 日志文件名（带日期）
LOG_FILE = LOG_DIR / f"fastapi_{datetime.now().strftime('%Y-%m-%d')}.log"

# 日志保留天数
LOG_RETENTION_DAYS = 7

# 日志格式
LOG_FORMAT = (
    "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level>"
)


def setup__logger(debug: bool = False) -> None:
    """
    初始化日志配置，debug 模式打印 DEBUG 日志，非 debug 模式打印 INFO 及以上。
    """
    _logger.remove()

    # 控制台日志
    _logger.add(
        sys.stdout,
        level="DEBUG" if debug else "INFO",
        format=LOG_FORMAT,
        enqueue=True,  # 多线程/多进程安全
        backtrace=True,  # 输出异常堆栈
        diagnose=True,  # 变量诊断
    )

    # 文件日志（每天轮转、保留N天）
    _logger.add(
        str(LOG_DIR / "fastapi_{time:YYYY-MM-DD}.log"),
        rotation="00:00",  # 每天0点新文件
        retention=f"{LOG_RETENTION_DAYS} days",  # 保留日志天数
        compression="zip",  # 压缩日志文件为 zip，
        # 可选：gz, bz2, xz, lzma, tar, tar.gz, ...
        level="DEBUG" if debug else "INFO",
        format=LOG_FORMAT,
        encoding="utf-8",
        enqueue=True,
    )


# 在模块导入时初始化
setup__logger(debug=True)  # 生产环境默认关闭 debug

logger = _logger
