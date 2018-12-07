from Lesson_6.errors import UsernameLenError, MandatoryKeyError, \
    ResponseCodeLenError, ResponseCodeError, AccountNameNotStr, ResponseNotDict
import functools

class Log:
    def __init__(self, logger):
        self.logger = logger

    @staticmethod
    def _create_message(result=None, *args, **kwargs):
        message = ''
        if args:
            message += 'args: {}'.format(args)
        if kwargs:
            message += 'kwargs: {}'.format(kwargs)
        if result:
            message += '= {}'.format(result)
        return message

    def __call__(self, func):
        @functools.wraps(func)
        def decorator(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except (AccountNameNotStr,
                    MandatoryKeyError,
                    ResponseCodeLenError,
                    ResponseCodeError,
                    UsernameLenError,
                    ResponseNotDict) as e:
                result = e
                message = Log._create_message(result, *args, **kwargs)
                # self.logger.error('{} - {} - {}'.format(message, func.__name__, func.__module__))
                self.logger.exception('{} - {} - {}'.format(message, func.__name__, func.__module__))
                raise
            message = Log._create_message(result, *args, **kwargs)
            self.logger.info('{} - {} - {}'.format(message, func.__name__, func.__module__))
            return result

        return decorator

