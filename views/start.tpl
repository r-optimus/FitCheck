<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>FitCheck</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>

    <main class="page-shell hero">
        <nav class="nav">
            <a class="brand" href="/">
                <img class="nav-logo" src="/static/logo-mini.png" alt="FitCheck">
            </a>
            <div>
                <a href="/">Start</a>
                <a href="/eingabe">Rechner</a>
                <a href="/tipps">Tipps</a>
                <a href="/quiz">Quiz</a>
                <a href="/workout">Workout</a>
            </div>
        </nav>

        <section class="hero-content">
            <img class="hero-logo" src="/static/logo.png" alt="FitCheck Logo">
            <p class="eyebrow">Fitnesswerte einfach berechnen</p>

            <p>
                Berechne deinen BMI, Wasserbedarf, Proteinbedarf und Kalorienbedarf.
            </p>

            <div class="actions">
                <a class="button primary" href="/eingabe">Berechnung starten</a>
                <a class="button secondary" href="/challenge">Daily Challenge</a>
                <a class="button secondary" href="/quiz">Quiz starten</a>
                <a class="button secondary" href="/workout">Workout erstellen</a>
            </div>

            % if challenge:
            <div class="challenge-box">
                <span>Deine Challenge:</span>
                <strong>{{challenge}}</strong>
            </div>
            % end
        </section>

        <section class="home-sections">
            <div class="feature-grid">
                <article class="feature-card">
                    <span>BMI</span>
                    <strong>BMI &amp; Bewertung</strong>
                    <p>Sieh sofort, wie dein Wert eingeordnet wird.</p>
                </article>
                <article class="feature-card">
                    <span>kcal</span>
                    <strong>Kalorienziel</strong>
                    <p>Erhalte ein Ziel passend zu Abnehmen, Halten oder Aufbau.</p>
                </article>
                <article class="feature-card">
                    <span>Quiz</span>
                    <strong>Fitnesswissen</strong>
                    <p>Teste dein Wissen mit 10 kurzen Fragen.</p>
                </article>
            </div>

            <div class="home-highlights">
                <span>💧 Wasserbedarf</span>
                <span>🥚 Proteinbedarf</span>
                <span>🔥 Gesamtumsatz</span>
                <span>🎯 Daily Challenge</span>
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
