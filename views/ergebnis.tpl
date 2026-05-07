<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Ergebnis</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>

    <h1>Dein Ergebnis</h1>

    <p>Dein BMI ist: <strong>{{bmi}}</strong></p>
    <p>Bewertung: <strong>{{bewertung}}</strong></p>
    <p>Empfohlener Wasserbedarf: <strong>{{wasser_liter}} Liter pro Tag</strong></p>
    <p>Empfohlener Proteinbedarf: <strong>{{protein}} g pro Tag</strong></p>

    <a href="/eingabe">Neue Berechnung</a>
    <br>
    <a href="/">Zurück zur Startseite</a>

</body>
</html>
