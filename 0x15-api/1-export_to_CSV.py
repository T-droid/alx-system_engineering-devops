#!/usr/bin/python3
"""exports data to csv file"""

import requests
import sys
import csv

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "user/{}".format(sys.argv[1])).json()
    username = user.get("username")
    to_do = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    with open("{}.csv".format(sys.argv[1]), "w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        [writer.writerow(
            [sys.argv[1], username, task.get("completed"), task.get("title")]
            ) for task in to_do]