import itertools
from string import digits, punctuation, ascii_letters
import win32com.client as client


def brute_excel_doc():
    print("***Hello freind!***")

    try:
        password_len = input("Введите длину пароля, от скольки - до скольки символов, например 3 - 7:")
        password_len = [int(item) for item in password_len.split("-")]
    except:
        print("Проверьте введенные данные")

    print("Если пароль содержит только цифры, введите: 1\nЕсли пароль содержит только буквы, введите: 2\nЕсли пароль содержит цифры и буквы, введите: 3\nЕсли пароль содержит цирф, буквы и спецсимволы, введите: 4")

    try:
        choice = int(input(": "))
        if choice == 1:
            possible_symbols = digits
        elif choice == 2:
            possible_symbols = ascii_letters
        elif choice == 3:
            possible_symbols = digits + ascii_letters
        elif choice == 4:
            possible_symbols = digits + ascii_letters + punctuation
        else:
            print("Something wrong... What symbols did you use????")
        # print(possible_symbols)
    except:
        print("Something wrong... What symbols did you use????")

    for pass_len in range(password_len[0], password_len[1] + 1):
        for password in itertools.product(possible_symbols, repeat=pass_len):
            password = "".join(password)
            print(password)
            opened_doc = client.Dispatch("Excel.Application")

            try:
                opened_doc.Workbooks.Open(

                )
            except:
                pass


def main():
    brute_excel_doc()







if __name__ == '__main__':
    main()