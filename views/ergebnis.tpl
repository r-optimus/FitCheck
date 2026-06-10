<section class="panel">
    <p class="eyebrow">Auswertung</p>
    <h1>Dein Ergebnis</h1>

    <div class="result-grid">
        % for label, value, icon, tip, css in metrics:
        <article class="metric {{css}}">
            <span class="metric-info" data-tooltip="{{tip}}">
                <img class="metric-info-icon" src="/static/infobox.png" alt="" width="15" height="15">
            </span>
            <span class="metric-label"><span class="metric-emoji">{{icon}}</span>{{label}}</span>
            <strong>{{value}}</strong>
        </article>
        % end
    </div>

    <div class="actions result-actions">
        <form class="export-form" action="/export" method="post">
            % for name, value in export_fields:
            <input type="hidden" name="{{name}}" value="{{value}}">
            % end
            <button class="primary" type="submit">Ergebnis herunterladen</button>
        </form>
        <a class="button secondary" href="/eingabe">Neue Berechnung</a>
        <a class="button secondary" href="/tipps">Tipps ansehen</a>
        <a class="button secondary" href="/">Startseite</a>
    </div>
</section>

% rebase('layout', title='Ergebnis', stylesheet='/static/style.css', page_class='')
