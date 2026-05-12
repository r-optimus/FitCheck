<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Über FitCheck</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>

    <main class="page-shell">
        <nav class="nav">
            <a class="brand" href="/">
                <img class="nav-logo" src="/static/logo-mini.png" alt="FitCheck">
            </a>
            <div>
                <a href="/">Start</a>
                <a href="/eingabe">Rechner</a>
            </div>
        </nav>

        <section class="panel content">
            <p class="eyebrow">Über das Projekt</p>
            <h1>Über FitCheck</h1>

            <p>
                FitCheck ist ein kleines Webprojekt mit Python und Bottle.
                Ziel der App ist es, einfache Fitnesswerte zu berechnen und verständlich anzuzeigen.
            </p>

            <h2>Technischer Aufbau</h2>

            <p>
                Die Datei app.py steuert die App. 
                Die Seiten liegen im Ordner views. 
                Das Design liegt im Ordner static.
            </p>

            <h2>Funktionen</h2>

            <ul>
                <li>BMI-Berechnung</li>
                <li>BMI-Bewertung</li>
                <li>Wasserbedarf pro Tag</li>
            </ul>

            <div class="actions">
                <a class="button primary" href="/eingabe">Zur Eingabe</a>
                <a class="button secondary" href="/">Startseite</a>
            </div>
        </section>

        <footer class="footer">
            <a href="/impressum">Impressum</a>
            <a href="/agb">AGB</a>
            <a href="/datenschutz">Datenschutz</a>
            <a href="/about">Über uns</a>
        </footer>
    </main>

</body>
</html>
