<section class="panel content auth-panel">
    <p class="eyebrow">Account</p>
    <h1>Login</h1>
    <p>Melde dich an, damit du deinen individuellen Fortschritt tracken kannst.</p>

    % if error:
    <div class="auth-error"><p>{{error}}</p></div>
    % end

    <div class="auth-grid">
        <form action="/login" method="post">
            <h2>Anmelden</h2>
            <label for="login_username">Benutzername</label>
            <input id="login_username" type="text" name="username" autocomplete="username" required>

            <label for="login_password">Passwort</label>
            <input id="login_password" type="password" name="password" autocomplete="current-password" required>

            <button class="primary" type="submit">Einloggen</button>
        </form>

        <form action="/registrieren" method="post">
            <h2>Registrieren</h2>
            <label for="register_username">Benutzername</label>
            <input id="register_username" type="text" name="username" autocomplete="username" required>

            <label for="register_password">Passwort</label>
            <input id="register_password" type="password" name="password" autocomplete="new-password" required>

            <button class="secondary" type="submit">Account erstellen</button>
        </form>
    </div>
</section>

% rebase('layout', title='Login', stylesheet='/static/style.css', page_class='')
