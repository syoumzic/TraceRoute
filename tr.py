import subprocess
import re
import json
from urllib import request


def get_args(count, info):
    try:
        as_number = info['org'].split()[0][2::]
        provider = " ".join(info['org'].split()[1::])
    except KeyError:
        as_number, provider = '*', '*'
    return [f"{count}.", info['ip'], info['country'], as_number, provider]


def get_bogon_args(count, info):
    return [f"{count}.", info['ip'], '*', '*', '*']


def is_complete(text_data):
    return 'Trace complete' in text_data \
           or 'Трассировка завершена' in text_data


def is_beginning(text_data):
    return 'Tracing route' in text_data \
           or 'Трассировка маршрута' in text_data


def is_invalid_input(text_data):
    return 'Unable to resolve' in text_data \
           or 'Не удается разрешить' in text_data

def get_ip_info(ip):
    return json.loads(request.urlopen('http://ip-api.com/json/' + ip).read())

def get_or_else(dic, value):
    try:
        return dic[value]
    except Exception:
        return "*"



def trace_as(address):
    print("ip-аддрес, страна, автономная система, владелец:")
    tracert_proc = subprocess.Popen(["tracert", address], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for raw_line in iter(tracert_proc.stdout.readline, ''):
        line = raw_line.decode('cp866')
        ip = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)

        if is_complete(line):
            return
        if is_invalid_input(line):
            print('неправильный ввод')
            return
        if is_beginning(line):
            continue
        if ip:
            info = get_ip_info(ip[0])
            print(", ".join([get_or_else(info, 'query'), get_or_else(info, 'country'), get_or_else(info, 'as'), get_or_else(info, 'isp')]))


def main():
    address = input('введите ip-аддрес или имя хоста: ')
    trace_as(address)


if __name__ == '__main__':
    main()