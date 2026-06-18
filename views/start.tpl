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
