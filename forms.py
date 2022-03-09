<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Snacks</title>
</head>
<body>
    <h1> New Snack </h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {% for field in form 
            if field.widget.input_type != 'hidden' %}
        <p>
            {{field.label}}
            {{field}}

            {% for err in field.errors %}
            {{err}}
            {% endfor %}
        </p>
        {%endfor%}
    <button> Add Snack </button>
    </form>
    
</body>
</html> 
