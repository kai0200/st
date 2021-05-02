# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4
"""
查询日志的相关的收发记录
python g.py <Email> [1 2 3]

g.py user@domain.com 搜索当天日志
g.py user@domain.com -d n 两天以内的
g.py user@domain.com -f a.log b.log c.log 搜索多个日志文件
"""

import argparse
import datetime
import os
import re

from dateutil.parser import parse


# grep 查找记录email 或 quid
def search_record(record, logfile):
    ''' Search record(email_address or queueid) in logfile '''
    return os.popen('grep {} {}'.format(record, logfile)).readlines()


# 4FVfGH0brJz4wXZ /home/caler/wk/2021.04.28.log
def get_queueid_sender(sender, log):
    """ Get email queue id from log for sender return list"""
    return log.split(',')[0].split(': ')[-2] if sender in log else 'Null'


def convert_time(time_str):
    """ Return time of the log """
    time = re.search(r'\w{3}\ \d{2}\ \d{2}:\d{2}:\d{2}', time_str)
    return parse(
        time.group()).strftime("%Y-%m-%d %H:%M:%S") if time else 'Null'


def get_ipaddress(record):
    ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', record)
    return ip.group() if ip else 'Null'


def get_email_address(record):
    email = re.search(r'[\w\.-]+@[\w\.-]+', record)
    return email.group() if email else 'Null'


def get_status(record):
    status = re.search(r'\d{3}\ \d\.\d\.\d\ \w+', record)
    return status.group() if status else 'Null'


def get_today_logfile():
    return datetime.datetime.today().strftime("%Y.%m.%d.log")


# search 搜索一个文件
def search(email, logfile):
    records = search_record(email, logfile)
    for record in records:
        qid = get_queueid_sender(email, record)
        line = search_record(qid, logfile)

        if len(line) > 4:
            time = convert_time(line[0])
            ip = get_ipaddress(line[0])
            sender = get_email_address(line[2])
            to = get_email_address(line[3])
            status = get_status(line[3])
        else:
            time = 'Null'
            ip = 'Null'
            sender = 'Null'
            to = 'Null'
            status = 'Null'

        print("%s - <%s> %s Time:%s IP:%s From:<%s> To:<%s> Status:%s " %
              (logfile, email, qid, time, ip, sender, to, status))


def get_logfile_name(days):
    """get n days ago logfile name """
    file_names = []
    file_names.append(datetime.datetime.today().strftime("%Y.%m.%d.log"))
    if days > 0:
        for n in range(1, days + 1):
            n_day_ago = (datetime.datetime.today() -
                         datetime.timedelta(days=n))
            file_names.append(n_day_ago.strftime("%Y.%m.%d.log"))
    return file_names


if __name__ == "__main__":
    # 解析参数
    parser = argparse.ArgumentParser(description="search email from logfile")
    group = parser.add_mutually_exclusive_group()
    parser.add_argument("email_address", help='user@domain.com')
    parser.add_argument('--version',
                        '-v',
                        action='version',
                        version='%(prog)s version : v 0.01',
                        help='show the version')
    parser.add_argument(
        '--days',
        '-d',
        default=0,
        dest='days',
        type=int,
        #action='store_true',
        help='%(prog) user@domain.com -d 1[2 3]')
    # --file 支持接多个文件，使用nargs=‘+’
    parser.add_argument('--file',
                        '-f',
                        nargs='+',
                        dest='files',
                        help='%(prog) user@domain.com -f file1 file2 ...')
    args = parser.parse_args()

    # main
    # 通过参数days的天数获取相关几个日志文件名字，默认包含当天数据
    logfiles = get_logfile_name(args.days)

    # 如果参数-f 指定了相关多个文件，增加到logfiles 列表里
    if args.files:
        #logfiles += args.files
        logfiles = args.files if args.days == 0 else logfiles + args.files

    print(logfiles)

    for file in logfiles:
        print("LogFile: %s" % file)
        if os.path.exists(file):
            search(args.email_address, file)
        else:
            pass
