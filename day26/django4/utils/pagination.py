#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
from django.utils.safestring import mark_safe

'''网站页码'''


class Page:
    """******页码显示功能******
    当前页：current_page;
    总数据：data_count;
    每页显示数据：per_page_data;
    每页显示页码：per_page;
    """

    def __init__(self, current_page, data_count, per_page_data=10, per_page=11):
        self.current_page = current_page
        self.data_count = data_count
        self.per_page_data = per_page_data
        self.per_page = per_page

    @property
    def start(self):
        """起始数据"""
        return (self.current_page - 1) * self.per_page_data

    @property
    def end(self):
        """结束数据"""
        return self.current_page * self.per_page_data

    @property
    def all_pages(self):
        """总页数"""
        pages, remiander = divmod(self.data_count, self.per_page_data)
        if remiander:
            pages += 1
        return pages

    def page_str(self, base_url):
        """页码显示"""
        if self.all_pages < self.per_page:
            start_page = 1
            end_page = self.all_pages + 1
        else:
            if self.current_page <= (self.per_page + 1) / 2:
                start_page = 1
                end_page = self.per_page
            else:
                start_page = self.current_page - (self.per_page - 1) / 2
                end_page = self.current_page + (self.per_page + 1) / 2
                if (self.current_page + (self.per_page - 1) / 2) > self.all_pages:
                    start_page = self.all_pages - self.per_page + 1
                    end_page = self.all_pages + 1
        page_list = []
        if self.current_page == 1:
            prev = '<a class="page" href="javascript:void(0);">上一页</a>'
        else:
            prev = '<a class="page" href="%s?p=%s">上一页</a>' % (base_url, self.current_page - 1)
        page_list.append(prev)
        for i in range(int(start_page), int(end_page)):
            if i == self.current_page:
                temp = '<a class="page active" href="%s?p=%s">%s</a>' % (base_url, i, i)
            else:
                temp = '<a class="page" href="%s?p=%s">%s</a>' % (base_url, i, i)
            page_list.append(temp)
        if self.current_page == self.all_pages:
            Next = '<a class="page" href="javascript:void(0);">下一页</a>'
        else:
            Next = '<a class="page" href="%s?p=%s">下一页</a>' % (base_url, self.current_page + 1)
        page_list.append(Next)

        jump = '''
        <input type="text" />
        <a onclick="jumpTo(this,'%s?p=');" id="i1">跳转</a>
        ''' % (base_url,)
        page_list.append(jump)
        pages_str = mark_safe(''.join(page_list))
        return pages_str
