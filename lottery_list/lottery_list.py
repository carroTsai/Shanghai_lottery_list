#!/usr/bin/python

# -*- coding:utf-8 -*-

"""
    author  : carroTsai
    date    : 05/07/2018
    target  : get the list of Shanghai housing lottery and save as a csv file
"""

import requests
import csv
import re


# 获取页面的内容
def get_html_text(url):
    """
        返回url的全部文本
    :param url:
    :return: text
    """

    r = requests.get(url, timeout=30)

    return r.text


def main():
    b_id = input('请输入楼盘编号: ')
    range_id = 3127
    url = 'http://180.169.74.6:8081/yaohao/publicity/lotteryList?pageNumber=1&pageSize='\
          + str(range_id) + '&buildingDishId=' + b_id
    print(url)
    url_text = get_html_text(url)
    g = re.search("\[.*\]", url_text)
    url_text_edit = g.group()
    url_text_edited = url_text_edit[1:-1]
    print(url_text_edited)

    p = re.compile(r'[{](.*?)[}]', re.S)
    lottery_list = p.findall(url_text_edited)
    print(lottery_list)

    q = re.compile(r'":"(.*?)","')
    # list_1 = q.findall(lottery_list[0])
    # print(type(list_1))

    header = ['signUpNum', 'resultNum', 'name', 'cardNum']

    with open('lottery_list.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        i = 0
        while i < range_id:
            list_1 = q.findall(lottery_list[i])
            row = list_1
            writer.writerow(row)
            i += 1


if __name__ == '__main__':
    main()
