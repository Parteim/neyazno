from urllib import request
import re
import random

href = "https://tenor.com"

def gifs():
    arr_link = []
    myUrl = "https://tenor.com/"
    file = 'html.txt'
    refil = "result.txt"

    op_file = open(file, mode="w", encoding="utf_8")
    resultsfil = open(refil, mode="w", encoding="utf_8")

    otvet = request.urlopen(myUrl)
    mytext1 = otvet.readlines()

    reference = r"/view/[\w-]+[0-9]"

    for line in mytext1:
        op_file.write(str(line))

    op_file.close()

    op_file = open(file, mode="r", encoding="utf_8")
    op = op_file.read()
    results = re.findall(reference, op)

    for number, i in enumerate(results, 1):
        arr_link.append(i)
        resultsfil.write(str(number) + " " + i + "\n")

    return (str(href) + str(random.choice(arr_link)))

