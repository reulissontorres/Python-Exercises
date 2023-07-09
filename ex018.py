"""Seno, Cosseno e Tangente"""
from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que você deseja: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print(f'O ângulo de {ang:}° tem o SENO de {sen:.2f}')
print(f'O ângulo {ang}° tem o COSSENO de {cos:.2f}')
print(f'O ângulo {ang}° tem a TANGENTE de {tan:.2f}')
