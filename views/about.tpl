<section class="panel content">
    <p class="eyebrow">Über das Projekt</p>
    <h1>Über FitCheck</h1>
    <p>FitCheck ist ein kleines Webprojekt mit Python und Bottle. Ziel der App ist es, einfache Fitnesswerte zu berechnen und verständlich anzuzeigen.</p>

    <h2>Technischer Aufbau</h2>
    <p>Die Datei app.py steuert die App. Die Seiten liegen im Ordner views. Das Design liegt im Ordner static.</p>

    <h2>Funktionen</h2>
    <ul>
        <li>BMI-Berechnung</li>
        <li>BMI-Bewertung</li>
        <li>Wasserbedarf pro Tag</li>
        <li>Proteinbedarf passend zum Ziel</li>
        <li>Gesamtumsatz und Kalorienziel</li>
        <li>Export der Ergebnisse als Textdatei</li>
        <li>Tipps zu Ernährung, Bewegung und Alltag</li>
        <li>Workout-Generator nach Ort und Level</li>
        <li>Fitness-Quiz</li>
        <li>Daily Challenge für kleine Tagesziele</li>
    </ul>

    <div class="actions">
        <a class="button primary" href="/eingabe">Zur Eingabe</a>
        <a class="button secondary" href="/">Startseite</a>
    </div>
</section>

% rebase('layout', title='Über FitCheck', stylesheet='/static/style.css', page_class='')
