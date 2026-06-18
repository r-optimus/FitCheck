<section class="panel progress-panel">
    <p class="eyebrow">Tracking</p>
    <h1>Fortschritt</h1>
    <p>Speichere regelmäßig deine Werte und vergleiche, wie sich Gewicht und BMI entwickeln.</p>

    % if error:
    <div class="result-card"><p>{{error}}</p></div>
    % end

    <form action="/fortschritt" method="post" class="progress-form">
        <label for="entry_date">Datum</label>
        <input id="entry_date" type="date" name="entry_date" value="{{today}}" required>

        <label for="weight">Gewicht</label>
        <input id="weight" type="number" name="weight" step="0.1" min="1" max="600" placeholder="in kg" required>

        <label for="bmi">BMI</label>
        <input id="bmi" type="number" name="bmi" step="0.01" min="1" max="100" placeholder="z. B. 23.4">

        <label for="note">Notiz</label>
        <input id="note" type="text" name="note" maxlength="160" placeholder="z. B. Lauf, Gym oder Gefühl">

        <button class="button primary" type="submit">Eintrag speichern</button>
    </form>
</section>

<section class="panel content progress-panel">
    <p class="eyebrow">Auswertung</p>
    <h2>Statistik</h2>

    <div class="progress-stats">
        % for label, value in stats:
        <article class="progress-stat">
            <span>{{label}}</span>
            <strong>{{value}}</strong>
        </article>
        % end
    </div>

    % if chart_entries:
    <h2>Gewichtsverlauf</h2>
    <div class="progress-chart">
        % for entry in chart_entries:
        <div class="progress-bar-wrap">
            <span class="progress-bar-value">{{entry["weight"]}} kg</span>
            <div class="progress-bar" style="height: {{entry["height"]}}px"></div>
            <span class="progress-bar-date">{{entry["label"]}}</span>
        </div>
        % end
    </div>
    % end

    <h2>Einträge</h2>
    % if entries:
    <div class="progress-table-wrap">
        <table class="progress-table">
            <thead>
                <tr>
                    <th>Datum</th>
                    <th>Gewicht</th>
                    <th>BMI</th>
                    <th>Notiz</th>
                    <th>Aktion</th>
                </tr>
            </thead>
            <tbody>
                % for entry in entries:
                <tr>
                    <td>{{entry["entry_date"]}}</td>
                    <td>{{entry["weight"]}} kg</td>
                    <td>
                        % if entry["bmi"] is not None:
                        {{entry["bmi"]}}
                        % else:
                        -
                        % end
                    </td>
                    <td>{{entry["note"] or '-'}}</td>
                    <td>
                        <form class="delete-entry-form" action="/fortschritt/{{entry['id']}}/loeschen" method="post">
                            <button class="danger" type="submit">Löschen</button>
                        </form>
                    </td>
                </tr>
                % end
            </tbody>
        </table>
    </div>
    % else:
    <div class="result-card">
        <p>Noch keine Einträge. Speichere deinen ersten Wert, dann entsteht hier deine Statistik.</p>
    </div>
    % end
</section>

% rebase('layout', title='Fortschritt', stylesheet='/static/style.css', page_class='')
