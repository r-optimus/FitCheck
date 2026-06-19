% import random
% challenges = [
%     "Trinke heute nur Wasser statt Softdrinks.",
%     "Gehe heute 20 Minuten spazieren.",
%     "Iss heute zu jeder Mahlzeit etwas Gemüse.",
%     "Verzichte heute auf Fast Food.",
%     "Gehe heute 30 Minuten früher ins Bett.",
%     "Mache heute einen Spaziergang nach dem Abendessen.",
%     "Lass heute eine unnötige Autofahrt weg und gehe zu Fuß.",
%     "Trinke direkt nach dem Aufstehen ein Glas Wasser.",
%     "Verzichte heute auf Süßigkeiten.",
%     "Stehe heute jede Stunde einmal kurz auf.",
%     "Mache heute etwas Sport, egal wie kurz.",
%     "Iss heute bewusst und ohne Handy oder Fernseher.",
%     "Nimm heute die Treppe statt den Aufzug.",
%     "Verbringe heute mindestens 30 Minuten draußen.",
%     "Achte heute auf eine aufrechte Haltung.",
%     "Trinke heute mindestens 2 Liter Wasser.",
%     "Mache heute einen kleinen Abendspaziergang.",
%     "Lass heute ein zuckerhaltiges Getränk weg.",
%     "Iss heute eine extra Portion Obst.",
%     "Plane heute deine Sporteinheit für die Woche.",
%     "Gehe heute mindestens 8.000 Schritte.",
%     "Mache heute 10 Minuten Dehnübungen.",
%     "Verzichte heute auf einen späten Mitternachtssnack.",
%     "Koche heute eine Mahlzeit selbst.",
%     "Iss heute langsam und ohne Eile.",
%     "Gehe heute für frische Luft nach draußen, auch wenn du keine Lust hast.",
%     "Stehe heute beim Telefonieren auf und bewege dich.",
%     "Trinke vor jeder Mahlzeit ein Glas Wasser.",
%     "Verbringe heute 30 Minuten ohne Social Media.",
%     "Mache heute etwas, das deinen Stress reduziert.",
%     "Gehe heute eine Haltestelle früher aus Bus oder Bahn.",
%     "Achte heute darauf, genug Protein zu essen.",
%     "Mache heute einen kurzen Spaziergang in deiner Mittagspause.",
%     "Lüfte heute mehrmals deine Wohnung.",
%     "Versuche heute mindestens 7 Stunden zu schlafen.",
%     "Iss heute keine Chips oder Snacks aus Langeweile.",
%     "Bewege dich heute insgesamt mindestens 30 Minuten.",
%     "Starte den Tag mit einem gesunden Frühstück.",
%     "Gehe heute bewusst ein paar Minuten in die Sonne.",
%     "Räume heute deinen Trainings- oder Arbeitsbereich auf.",
% ]
% challenge = random.choice(challenges) if show_challenge else None

<section class="hero-content">
    <img class="hero-logo" src="/static/logo.png" alt="FitCheck Logo">
    <p class="eyebrow">Fitnesswerte einfach berechnen</p>
    <p>Berechne deinen BMI, Wasserbedarf, Proteinbedarf und Kalorienbedarf.</p>
    <div class="actions home-primary-action">
        <a class="button primary" href="/eingabe">Berechnung starten</a>
    </div>
    <div class="actions home-secondary-actions">
        <a class="button secondary" href="/workout">Workout erstellen</a>
        <a class="button secondary" href="/challenge">Daily Challenge</a>
        <a class="button secondary" href="/fortschritt">Fortschritt tracken</a>
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
            <span>Track</span>
            <strong>Fortschritt</strong>
            <p>Speichere Werte und sieh deine Entwicklung.</p>
        </article>
    </div>

    <div class="home-highlights">
        <span>💧 Wasserbedarf</span>
        <span>🥚 Proteinbedarf</span>
        <span>🔥 Gesamtumsatz</span>
        <span>🎯 Daily Challenge</span>
    </div>
</section>

% rebase('layout', title='FitCheck', stylesheet='/static/style.css', page_class='hero')
