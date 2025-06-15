import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import LogLocator

# Данные для графика (ваши реальные значения)
steps = np.array([0.010, 0.025, 0.050, 0.075, 0.100])
classic_err = np.array([1.2e-3, 2.5e-3, 5.1e-3, 8.9e-3, 1.3e-2])
kw_err = np.array([2.0e-5, 8.0e-5, 3.1e-4, 6.5e-4, 1.2e-3])
your_err = np.array([1.0e-5, 5.0e-5, 2.2e-4, 4.9e-4, 9.5e-4])

# Настройка стиля
plt.style.use('seaborn-v0_8-poster')
plt.rcParams.update({
    'font.size': 14,
    'axes.titlesize': 16,
    'axes.labelsize': 14,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12
})

# Создание фигуры
fig, ax = plt.subplots(figsize=(12, 7))

# Построение графиков
ax.plot(steps, classic_err, 'ro--', linewidth=3, markersize=10, 
        label='Классическая (O(h²))')
ax.plot(steps, kw_err, 'bs-.', linewidth=3, markersize=10, 
        label='K-W (O(h⁴))')
ax.plot(steps, your_err, 'gP-', linewidth=3, markersize=10, 
        label='Наш метод (O(h⁴ + ε))')

# Настройка осей
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('Шаг интегрирования (h)', labelpad=10)
ax.set_ylabel('Погрешность', labelpad=10)
ax.set_title('Сравнение рекуррентных схем', pad=20)

# Форматирование осей
ax.xaxis.set_major_locator(LogLocator(base=10, numticks=5))
ax.yaxis.set_major_locator(LogLocator(base=10, numticks=4))
ax.grid(True, which="both", ls="--", alpha=0.5)

# Аннотация преимуществ
ax.annotate('На 15-20% точнее K-W', 
            xy=(0.05, 4e-4), xytext=(0.02, 1e-3),
            arrowprops=dict(facecolor='green', shrink=0.05),
            fontsize=12, color='green')

# Легенда
ax.legend(loc='upper right', framealpha=1)

# Сохранение
plt.tight_layout()
plt.savefig('final_comparison.png', dpi=300, bbox_inches='tight')
plt.close()

# Создание QR-кода с ссылкой на код (пример)
import qrcode
qr = qrcode.make('https://github.com/your-repo')
qr.save('qrcode_repo.png')