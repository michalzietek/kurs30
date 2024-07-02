import os

print(os.getcwd())
os.chdir("/home/michal/future_collars/kurs30")
print(os.getcwd())
obecny_folder = os.getcwd()
pliki = os.listdir(obecny_folder)
print(pliki)
