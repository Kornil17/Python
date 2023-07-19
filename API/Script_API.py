import requests
import pytest

class test_1:

    def test_get_requests():
        results = list()

        with open('requests_for_python.txt', 'r') as f:
            count = 0
            for i in f:
                count += 1
                print(f"Запрос номер : {count}")
                url = requests.get(i)
                print(url.text, "\n")
                print(url.status_code, "\n")
                results.append("Number of request : " + str(count))
                results.append(url.text)
                results.append("Status code - " + str(url.status_code))
            f.close()

        with open('result.txt', 'w') as f:
            f.write(str("API testing Report "))
            for i in range(len(results)):
                f.write(str("\n") + str(results[i]) + str("\n"))
            f.close()


if __name__ == "__main__":
    test_py.py()
