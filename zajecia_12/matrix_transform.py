'''
**Zadanie: Transformacja Macierzy**
Napisz program, który przetworzy plik CSV zawierający tablicę liczb i zastosuje serię transformacji określonych przez użytkownika. Program powinien odczytać plik wejściowy, zastosować zadane transformacje, a następnie zapisać go do wskazanego pliku wyjściowego.
Uruchomienie programu przez terminal:
python matrix_transform.py <plik_wejsciowy> <plik_wyjsciowy> <transformacja_1> <transformacja_2> ... <transformacja_n>
- <plik_wejsciowy> - nazwa pliku, z którego odczytane zostaną dane, np. data.csv
- <plik_wyjsciowy> - nazwa pliku, do którego zostanie zapisany wynik, np. result.csv
- <transformacja_x> - Transformacja w postaci "operacja, parametry" - operacja może być np. 'add', 'mult', 'div', a parametry będą określały wartości do zastosowania transformacji (np. dla 'add' będą to wartości dodane do każdej komórki w danej kolumnie lub wierszu).
Operacje transformacji:
- add,row,index,value - Dodaj wartość do każdego elementu w wierszu o zadanym indeksie.
- add,col,index,value - Dodaj wartość do każdego elementu w kolumnie o zadanym indeksie.
- mult,row,index,value - Pomnóż każdy element w wierszu przez wartość.
- mult,col,index,value - Pomnóż każdy element w kolumnie przez wartość.
'''
import sys
from file_handler import FileHandler

arguments = sys.argv
print(arguments)
handler = FileHandler(input_file=arguments[1], output_file=arguments[2], changes=arguments[3:])
handler.transform()
handler.save_data_to_file()