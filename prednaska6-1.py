import json
import requests

if __name__ == "__main__":

    # data = {"jmeno": "Alice", "vek": 20}
    # print(data)
    # json_data = json.dumps(data)
    # print(json_data)
    # with open("data.txt", "w") as fp:
    #     fp.write(json_data)

    # with open("data.txt", "r") as fp:
    #     x = fp.read()
    # print(x)

    # xdata = json.loads(x)
    # print(xdata["jmeno"])

    r = requests.get("https://www.jcu.cz/xxx/")
    if r.status_code == 200:
        print(r.content)


    