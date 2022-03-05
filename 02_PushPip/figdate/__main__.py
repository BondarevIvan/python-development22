import time
import pyfiglet
import sys
import locale


def date(format_: str, font_: str):
    current_date = time.strftime(format_, time.gmtime())
    return pyfiglet.figlet_format(current_date, font=font_)


if __name__ == '__main__':
    locale.setlocale(locale.LC_TIME, ('ru_RU', 'UTF-8'))
    index = { 'format_' : 1, 'font_' : 2 }
    default = {'format_' : '%Y %d %b, %A', 'font_' : 'graceful'}
    kwargs = {keyword : default[keyword] if len(sys.argv) <= index[keyword] else sys.argv[index[keyword]] for keyword in index}
    print(date(**kwargs))