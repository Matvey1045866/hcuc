import time

# Чистый текст выводится через print
time.sleep(2)
print("✨ Подожди немного... ✨")
time.sleep(2)
print("📝 Собираю все свои чувства...")
time.sleep(1.5)
print("💭 Думаю о тебе...")
time.sleep(1)
print("❤️")
time.sleep(0.5)
print("❤️❤️")
time.sleep(0.5)
print("❤️❤️❤️")
time.sleep(0.5)

# Теперь используем Element для HTML-вывода
from pyscript import Element

msg = Element("msg")

# Добавляем красивое HTML-сообщение
msg.element.innerHTML += """
    <div style="margin-top: 20px; padding: 15px; background: #ff6b6b; border-radius: 10px; color: white;">
        <h2 style="margin: 0;">💖 Люблю тебя, мамочка! 💖</h2>
        <p style="margin: 10px 0 0;">Ты самая лучшая!</p>
    </div>
"""