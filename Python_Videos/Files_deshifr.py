import pyAesCrypt
import os

# Функция дешифрования
def decryption(file, password):

    # задаем размер буфера
    buffer_size = 512 + 1024

    # вызываем метод дешифрования
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size

    )

    # чтобы видеть результат, будем выводить процесс шифрования
    print(f"Файл: {str(os.path.splitext(file)[0])} расшифрован")

    # удалим исходный файл методом remove
    os.remove(file)

# функция сканирования директорий
def walking_by_dirs(dir, password):

    # перебираем все поддиректории в указанной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # если нашли файл, вызываем метод дешифрования
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        # если находим директорию, то повторяем цикл
        else:
            walking_by_dirs(path, password)

# password = input("Введите пароль для дешифрования...:'\n'")
# walking_by_dirs("/home/kornil/test", password)