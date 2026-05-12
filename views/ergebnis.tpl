<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Ergebnis</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>

    <main class="page-shell">
        <nav class="nav">
            <a class="brand" href="/">
                <img class="nav-logo" src="/static/logo-mini.png" alt="FitCheck">
            </a>
            <div>
                <a href="/eingabe">Rechner</a>
            </div>
        </nav>

        <section class="panel">
            <p class="eyebrow">Auswertung</p>
            <h1>Dein Ergebnis</h1>

            <div class="result-grid">
                <article class="metric {{bmi_klasse}}">
                    <span>BMI</span>
                    <strong>{{bmi}}</strong>
                </article>
                <article class="metric {{bmi_klasse}}">
                    <span>Bewertung</span>
                    <strong>{{bewertung}}</strong>
                </article>
                <article class="metric">
                    <span>Wasserbedarf</span>
                    <strong>{{wasser_liter}} L</strong>
                </article>
                <article class="metric">
                    <span>Proteinbedarf</span>
                    <strong>{{protein}} g</strong>
                </article>
                <article class="metric">
                    <span>Grundumsatz</span>
                    <strong>{{grundumsatz}} kcal/Tag</strong>
                </article>
            </div>

            <div class="actions">
                <a class="button primary" href="/eingabe">Neue Berechnung</a>
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
