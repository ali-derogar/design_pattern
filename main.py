from source.logs import Loggers

logger = Loggers("logs.log")
for i in range(15):
    logger.info(f"state new round {i + 1}")
    logger.warning(f"{i + 1}"*(i+1))
    logger.error(f"errorrrrrrrr")