# -*- coding: utf-8 -*-
"""tabung

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1d0SKEXQYfW1L_8AJvQQEBbwjJrPaWxsJ
"""

# 5. Menghitung volume tabung

import math

def hitung_volume_tabung(jari_jari, tinggi):
    return math.pi * jari_jari ** 2 * tinggi

jari_jari = 3
tinggi = 5
volume = hitung_volume_tabung(jari_jari, tinggi)

print(f"Volume tabung: {volume:.2f}")