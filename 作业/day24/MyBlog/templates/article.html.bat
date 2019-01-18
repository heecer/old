<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .condition a{
            display: inline-block;
            padding: 3px 5px;
            margin: 5px;
            border: 1px solid #dddddd;
        }
        .condition a.active{
            background-color: #dd5b25;
        }
    </style>
</head>
<body>
    <h4>条件筛选:</h4>
    <div class="condition">
    <div>
        <span>类型：</span>
    {% if arg_dict.articletype_id == 0 %}
        <a class="active" href="/article/0-{{ arg_dict.category_id }}.html">全部</a>
    {% else %}
        <a href="/article/0-{{ arg_dict.category_id }}.html">全部</a>
    {% endif %}

        {% for row in article_type %}
            {% if row.nid == arg_dict.articletype_id %}
                <a class="active" href="/article/{{ row.nid }}-{{ arg_dict.category_id }}.html">{{ row.articletype }}</a>
            {% else %}
                <a href="/article/{{ row.nid }}-{{ arg_dict.category_id }}.html">{{ row.articletype }}</a>
            {% endif %}

        {% endfor %}
    </div>
    <div>
        <span>分类：</span>
    {% if arg_dict.category_id == 0 %}
        <a class="active" href="/article/{{ arg_dict.articletype_id }}-0.html">全部</a>
    {% else %}
        <a href="/article/{{ arg_dict.articletype_id }}-0.html">全部</a>
    {% endif %}

        {% for row in categorys %}
            {% if row.nid == arg_dict.category_id %}
                <a class="active" href="/article/{{ arg_dict.articletype_id }}-{{ row.nid }}.html">{{ row.category }}</a>
            {% else %}
                <a href="/article/{{ arg_dict.articletype_id }}-{{ row.nid }}.html">{{ row.category }}</a>
            {% endif %}
        {% endfor %}
    </div>
    </div>
    <h2>文章结果：</h2>
    <ul>
     {% for row in articles %}
        <li>{{ row.nid }}--{{ row.title }}</li>
    {% endfor %}
    </ul>

</body>
</html>