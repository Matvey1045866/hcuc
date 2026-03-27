import time

# Теперь используем Element для HTML-вывода
from js import getElementById

msg = getElementById("msg")

# Добавляем красивое HTML-сообщение
msg.element.innerHTML += """
    <div style="margin-top: 20px; padding: 15px; background: #ff6b6b; border-radius: 10px; color: white;">
        <h2 style="margin: 0;">💖 Люблю тебя, мамочка! 💖</h2>
        <p style="margin: 10px 0 0;">Ты самая лучшая!</p>
    </div>
"""