import pyAesCrypt
import os
import Files_deshifr
# Функция шифрования
def encryption(file, password):

    # задаем размер буфера
    buffer_size = 512 + 1024

    # вызываем метод шифрования
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crypt",
        password,
        buffer_size

    )

    # чтобы видеть результат, будем выводить процесс шифрования
    print(f"Файл: {str(os.path.splitext(file)[0])} зашифрован")

    # удалим исходный файл методом remove
    os.remove(file)

# функция сканирования директорий
def walking_by_dirs(dir, password):

    # перебираем все поддиректории в указанной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # если нашли файл, вызываем метод шифрования
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        # если находим директорию, то повторяем цикл
        else:
            walking_by_dirs(path, password)

n = input("Введите y - для шифрования или n - для дешифрования, для выхода exit \n").lower()
while n != "exit":
    if n == "y":
        password = input("Введите пароль для шифрования...:\n")
        walking_by_dirs("/home/kornil/test", password)
        n = input("Введите y - для шифрования или n - для дешифрования, для выхода exit \n").lower()
    elif n == "n":
        password = input("Введите пароль для дешифрования...:\n")
        Files_deshifr.walking_by_dirs("/home/kornil/test", password)
        n = input("Введите y - для шифрования или n - для дешифрования, для выхода exit \n").lower()
    else:
        print("Вы ввели недопустимое значение, попробуйте еще раз :)")
        n = input("Введите y - для шифрования или n - для дешифрования, для выхода exit \n").lower()
print("Спасибо за использования нашей программы для файлов, будем рады видеть вас снова. Удачи!)")
