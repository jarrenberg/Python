"""
Ejercicio 10 — Normaliza nombres (cadenas)
Escribe una función normaliza_nombre(s: str) -> str que:
- Elimine espacios al inicio/fin y reduzca espacios múltiples internos a uno.
- Convierta a "Title Case" (primera letra de cada palabra en mayúscula, resto minúsculas),
sin usar .title() directamente.
Entrada de ejemplo: " aNa péRez loPEz " → "Ana Pérez Lopez"
Pista: separa por espacios, filtra vacíos, y vuelve a unir con ' '. Usa slicing y
.lower()/.upper().
"""

