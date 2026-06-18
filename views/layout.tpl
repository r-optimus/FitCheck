<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>{{title}}</title>
    <script>
        (function () {
            if (localStorage.getItem('fitcheck-theme') === 'dark') {
                document.documentElement.classList.add('dark-mode');
            }
        }());
    </script>
    <link rel="stylesheet" href="{{stylesheet}}">
</head>
<body>
    <main class="page-shell{{' ' + page_class if page_class else ''}}">
        <nav class="nav">
            <a class="brand" href="/"><img class="nav-logo" src="/static/logo-mini.png" alt="FitCheck"></a>
            <div>
                <a href="/">Start</a>
                <a href="/eingabe">Rechner</a>
                <a href="/tipps">Tipps</a>
                <a href="/workout">Workout</a>
                <a href="/fortschritt">Fortschritt</a>
                % if current_user:
                <span class="nav-user">{{current_user["username"]}}</span>
                <a href="/logout">Logout</a>
                % else:
                <a href="/login">Login</a>
                % end
                <button class="theme-toggle" type="button" aria-label="Dark Mode umschalten" aria-pressed="false">
                    <span class="theme-toggle-track"><span class="theme-toggle-thumb"></span></span>
                    <span class="theme-toggle-text">☀️</span>
                </button>
            </div>
        </nav>

        {{!base}}

        <footer class="footer">
            <a href="/impressum">Impressum</a>
            <a href="/agb">AGB</a>
            <a href="/datenschutz">Datenschutz</a>
            <a href="/about">Über uns</a>
        </footer>
    </main>
    <script>
        (function () {
            var toggle = document.querySelector('.theme-toggle');
            var root = document.documentElement;

            function setTheme(isDark) {
                root.classList.toggle('dark-mode', isDark);
                localStorage.setItem('fitcheck-theme', isDark ? 'dark' : 'light');
                toggle.setAttribute('aria-pressed', isDark ? 'true' : 'false');
                toggle.querySelector('.theme-toggle-text').textContent = isDark ? '🌙' : '☀️';
            }

            if (toggle) {
                setTheme(root.classList.contains('dark-mode'));
                toggle.addEventListener('click', function () {
                    setTheme(!root.classList.contains('dark-mode'));
                });
            }
        }());
    </script>
</body>
</html>
