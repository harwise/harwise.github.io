{% for staff_member in site.programming %}
<h2>
   <a href="{{ staff_member.url }}">
      - {{ staff_member.title }}
   </a>
</h2>
{% endfor %}
