#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def filter_all(arg_dict, arg):
    '''simp_tag  筛选全部函数'''
    """
    {% if arg_dict.articletype_id == 0 %}
        <a class="active" href="/article/0-{{ arg_dict.category_id }}.html">全部</a>
    {% else %}
        <a href="/article/0-{{ arg_dict.category_id }}.html">全部</a>
    {% endif %}
    :return:
    """
    if arg == 'articletype_id':
        '''全部的类型'''
        n1 = arg_dict[arg]
        n2 = arg_dict['category_id']
        if n1 == 0:
            ret = '<a class="active" href="/article/0-%s.html">全部</a>' % n2
        else:
            ret = '<a href="/article/0-%s.html">全部</a>' % n2
    else:
        '''全部的分类'''
        n1 = arg_dict['articletype_id']
        n2 = arg_dict[arg]
        if n2 == 0:
            ret = '<a class="active" href="/article/%s-0.html">全部</a>'%n1
        else:
            ret = '<a href="/article/%s-0.html">全部</a>'%n1
    return mark_safe(ret)


@register.simple_tag
def filter_article_type(arg_dict,article_type):
    """
    {% for row in article_type %}
        {% if row.nid == arg_dict.articletype_id %}
            <a class="active" href="/article/{{ row.nid }}-{{ arg_dict.category_id }}.html">{{ row.articletype }}</a>
        {% else %}
            <a href="/article/{{ row.nid }}-{{ arg_dict.category_id }}.html">{{ row.articletype }}</a>
        {% endif %}

    {% endfor %}
    :return:
    """
    ret = []
    for row in article_type:
        if row.nid == arg_dict['articletype_id']:
            temp = '<a class="active" href="/article/%s-%s.html">%s</a>'\
                  %(row.nid,arg_dict['category_id'],row.articletype)
        else:
            temp = '<a  href="/article/%s-%s.html">%s</a>'\
                  %(row.nid,arg_dict['category_id'],row.articletype)
        ret.append(temp)
    return mark_safe(''.join(ret))


@register.simple_tag
def filter_category(arg_dict,categorys):
    """
    {% for row in categorys %}
        {% if row.nid == arg_dict.category_id %}
            <a class="active" href="/article/{{ arg_dict.articletype_id }}-{{ row.nid }}.html">{{ row.category }}</a>
        {% else %}
            <a href="/article/{{ arg_dict.articletype_id }}-{{ row.nid }}.html">{{ row.category }}</a>
        {% endif %}
    {% endfor %}
    :return:
    """
    ret = []
    for row in categorys:
        if row.nid == arg_dict['category_id']:
            temp = '<a class="active" href="/article/%s-%s.html">%s</a>'\
                  %(arg_dict['articletype_id'],row.nid,row.category)
        else:
            temp = '<a  href="/article/%s-%s.html">%s</a>'\
                  %(arg_dict['articletype_id'],row.nid,row.category)
        ret.append(temp)
    return mark_safe(''.join(ret))