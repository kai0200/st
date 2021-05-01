# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4
"""
查询日志的相关的收发记录
python g.py <Email> [1 2 3]

g.py user@domain.com 搜索当天日志
g.py user@domain.com -d 2 两天以内的
g.py user@domain.com -l a.log b.log c.log 搜索多个日志文件
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
    if sender in log:
        return log.split(',')[0].split(': ')[-2]
    else:
        return ''


def convert_time(time_str):
    time = re.search(r'\w{3}\ \d{2}\ \d{2}:\d{2}:\d{2}', time_str)
    if time:
        return parse(time.group()).strftime("%Y-%m-%d %H:%M:%S")
    else:
        return ''


def get_ipaddress(record):
    ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', record)
    if ip:
        return ip.group()
    else:
        return ''


def get_email_address(record):
    email = re.search(r'[\w\.-]+@[\w\.-]+', record)
    if email:
        return email.group()
    else:
        return ''


def get_status(record):
    status = re.search(r'\d{3}\ \d\.\d\.\d\ \w+', record)
    if status:
        return status.group()
    else:
        return ''


def get_today_logfile():
    return datetime.datetime.today().strftime("%Y.%m.%d.log")


# search 搜索指定的文件（单独一个）
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

        print("%s-<%s> - Time: %s IP: %s From: <%s> To: <%s> Status: %s " %
              (logfile, email, time, ip, sender, to, status))


def get_logfile_name(days):
    d = []
    d.append(datetime.datetime.today().strftime("%Y.%m.%d.log"))
    if days > 0:
        for n in range(0, days):
            n_day_ago = (datetime.datetime.today() -
                         datetime.timedelta(days=n))
            d.append(n_day_ago.strftime("%Y.%m.%d.log"))
    return d


if __name__ == "__main__":
    #email = "support@salesforce.com"
    #logfile = "/home/caler/wk/2021.04.28.log"

    parser = argparse.ArgumentParser(description="search email from logfile")
    parser.add_argument("email_address", help='user@domain.com')
    parser.add_argument('--version',
                        '-v',
                        action='version',
                        version='%(prog)s version : v 0.01',
                        help='show the version')
    parser.add_argument('--days',
                        '-d',
                        default=0,
                        type=int,
                        dest='days',
                        help='%(prog) user@domain.com -d 1[2 3]')
    parser.add_argument(
        '--file',
        '-f',
        nargs='+',
        dest='files',
        help='%(prog) user@domain.com -f xxxx.xx.xx.log xxxx.xx.xx.log ...')
    args = parser.parse_args()

    # main
    # 通过参数days的天数获取相关几个日志文件名字，默认包含当天数据
    logfiles = get_logfile_name(args.days)

    # 如果参数-f 指定了相关多个文件，增加到logfiles 列表里
    if args.files:
        logfiles += args.files

    print(logfiles)

    for file in logfiles:
        if os.path.exists(file):
            search(args.email_address, file)
        else:
            pass
