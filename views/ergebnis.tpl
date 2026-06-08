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
                <a href="/">Start</a>
                <a href="/eingabe">Rechner</a>
                <a href="/tipps">Tipps</a>
                <a href="/quiz">Quiz</a>
                <a href="/workout">Workout</a>
            </div>
        </nav>

        <section class="panel">
            <p class="eyebrow">Auswertung</p>
            <h1>Dein Ergebnis</h1>

            <div class="result-grid">
                <article class="metric {{bmi_klasse}}">
                    <span class="metric-info" data-tooltip="Der BMI bewertet dein Gewicht im Verhältnis zu deiner Körpergröße.">
                        <img class="metric-info-icon" src="/static/infobox.png" alt="" width="15" height="15">
                    </span>
                    <span class="metric-label"><span class="metric-emoji">⚖️</span>BMI</span>
                    <strong>{{bmi}}</strong>
                </article>
                <article class="metric {{bmi_klasse}}">
                    <span class="metric-info" data-tooltip="Diese Kategorie zeigt, wie dein BMI grob eingeordnet wird.">
                        <img class="metric-info-icon" src="/static/infobox.png" alt="" width="15" height="15">
                    </span>
                    <span class="metric-label"><span class="metric-emoji">✅</span>Bewertung</span>
                    <strong>{{bewertung}}</strong>
                </article>
                <article class="metric">
                    <span class="metric-info" data-tooltip="Das ist eine grobe Empfehlung für deine tägliche Trinkmenge.">
                        <img class="metric-info-icon" src="/static/infobox.png" alt="" width="15" height="15">
                    </span>
                    <span class="metric-label"><span class="metric-emoji">💧</span>Wasserbedarf</span>
                    <strong>{{wasser_liter}} L</strong>
                </article>
                <article class="metric">
                    <span class="metric-info" data-tooltip="Protein unterstützt Muskeln, Sättigung und Regeneration.">
                        <img class="metric-info-icon" src="/static/infobox.png" alt="" width="15" height="15">
                    </span>
                    <span class="metric-label"><span class="metric-emoji">🥚</span>Proteinbedarf</span>
                    <strong>{{protein}} g</strong>
                </article>
                <article class="metric">
                    <span class="metric-info" data-tooltip="Dein geschätzter täglicher Kalorienverbrauch mit Aktivitätslevel.">
                        <img class="metric-info-icon" src="/static/infobox.png" alt="" width="15" height="15">
                    </span>
                    <span class="metric-label"><span class="metric-emoji">🔥</span>Gesamtumsatz</span>
                    <strong>{{gesamtumsatz}} kcal</strong>
                </article>
                <article class="metric">
                    <span class="metric-info" data-tooltip="Dieses Ziel passt den Gesamtumsatz an dein ausgewähltes Ziel an.">
                        <img class="metric-info-icon" src="/static/infobox.png" alt="" width="15" height="15">
                    </span>
                    <span class="metric-label"><span class="metric-emoji">🎯</span>Kalorienziel ({{ziel_name}})</span>
                    <strong>{{kalorienziel}} kcal</strong>
                </article>
            </div>

            <div class="actions result-actions">
                <form class="export-form" action="/export" method="post">
                    <input type="hidden" name="geschlecht" value="{{geschlecht}}">
                    <input type="hidden" name="alter" value="{{alter}}">
                    <input type="hidden" name="gewicht" value="{{gewicht}}">
                    <input type="hidden" name="groesse" value="{{groesse_cm}}">
                    <input type="hidden" name="aktivitaet" value="{{aktivitaet}}">
                    <input type="hidden" name="ziel" value="{{ziel}}">
                    <button class="primary" type="submit">Ergebnis herunterladen</button>
                </form>
                <a class="button secondary" href="/eingabe">Neue Berechnung</a>
                <a class="button secondary" href="/tipps">Tipps ansehen</a>
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
