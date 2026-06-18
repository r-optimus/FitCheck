<section class="panel content">
    <p class="eyebrow">Rechtliches</p>
    <h1>Datenschutzerklärung</h1>
    <p>Diese Webanwendung wurde als lokales FitCheck-Projekt entwickelt. Sie dient dazu, Fitnesswerte zu berechnen und persönliche Fortschritte zu speichern.</p>

    <h2>Gespeicherte Daten</h2>
    <p>Wenn ein Benutzerkonto erstellt wird, speichert die Anwendung den Benutzernamen und ein technisch geschütztes Passwort-Hash. Für den Fortschritt werden Datum, Gewicht, BMI und optionale Notizen gespeichert.</p>

    <h2>Speicherort</h2>
    <p>Die Daten werden lokal in der SQLite-Datenbank <strong>fitcheck_progress.db</strong> gespeichert. Es findet keine automatische Übertragung an externe Server statt.</p>

    <h2>Cookies</h2>
    <p>Für den Login verwendet die Anwendung ein technisch notwendiges Cookie. Dieses Cookie speichert die Anmeldung, damit der Fortschritt dem richtigen Benutzer zugeordnet werden kann.</p>

    <h2>Keine Analyse</h2>
    <p>Die Anwendung verwendet keine Tracking-Tools, keine Werbung und keine externen Analyse-Dienste.</p>

    <h2>Hinweis</h2>
    <p>Alle Berechnungen dienen ausschließlich Informationszwecken und ersetzen keine medizinische Beratung.</p>
    <div class="actions"><a class="button primary" href="/">Startseite</a></div>
</section>

% rebase('layout', title='Datenschutz', stylesheet='/static/style.css', page_class='')
