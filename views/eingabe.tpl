<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Eingabe</title>

    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>

<body>

<h1>Eingabe</h1>

<form action="/ergebnis" method="post">

    <label>Alter:</label>
    <input type="number" name="alter">

    <br><br>

    <label>Name:</label>
    <input type="text" name="name">

    <br><br>

    <button type="submit">Absenden</button>

</form>

<script src="{{ url_for('static', filename='script.js') }}"></script>

</body>
</html>
