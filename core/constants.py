class Status:
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"


class LogDefaultRecord:
    name = "name"
    levelno = "levelno"
    levelname = "levelname"
    pathname = "pathname"
    filename = "filename"
    module = "module"
    lineno = "lineno"
    funcName = "funcName"
    created = "created"
    asctime = "asctime"
    msecs = "msecs"
    relativeCreated = "relativeCreated"
    thread = "thread"
    threadName = "threadName"
    process = "process"
    message = "message"


class LogCustomRecord(LogDefaultRecord):
    microServiceID = "microServiceID"
    url = "url"


LOG_RECORD_FORMAT = f"[%({LogCustomRecord.asctime})s.%({LogCustomRecord.msecs})03d] | %({LogCustomRecord.levelname})s | %({LogCustomRecord.microServiceID})s (%({LogCustomRecord.url})s) [process: %({LogCustomRecord.process})s] [thread: %({LogCustomRecord.threadName})s (%({LogCustomRecord.thread})s)]: %({LogCustomRecord.message})s"

LOG_DATETIME_FORMAT = "%d-%m-%Y %H-%M-%S"
