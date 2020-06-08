{% extends 'layout.html' %}
{% block body_content %}

<h3>Random post time!</h3>
{% for post in posts %}
    {{ post.title }}<br>
    {{ post.name.first}}<br>
    {{ post.name.last}}<br>
    {{ post.content }}<br><br>

{% endfor %}

{% endblock %}

~                                                                                                 
~                              