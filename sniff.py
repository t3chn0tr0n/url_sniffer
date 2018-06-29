#! usr/bin/python3
import sys
import re
import os


def sniff(string):
    result = []
    word_list = string.split(" ")

    http_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+] | [! * \(\),] | (?: %[0-9a-fA-F][0-9a-fA-F]))+.*'
    www_regex = 'www.(?:[a-zA-Z]|[0-9]|[$-_@.&+] | [! * \(\),] | (?: %[0-9a-fA-F][0-9a-fA-F]))+.*'
    mail_regex = "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}"

    for word in word_list:
        temp = re.findall(http_regex, word)
        if len(temp) == 0:
            temp = re.findall(www_regex, word)
            if len(temp) == 0:
                temp = re.findall(mail_regex, word)
        result += temp
    return result


def sniff_urls(path):
    result = []
    with open(path, 'r') as file:
        for line in file:
            urls = sniff(line)
            result += urls
    return result


def main(path):
    result = sniff_urls(path)
    if len(result) >= 1:
        choice = input("Do You want to save the urls in a file? (Y/n) ")
        if choice == 'Y' or choice == 'y':
            out_path = input("Enter file name, with desired path: ")
            if os.path.isdir(out_path):
                print("Enter path lands in a directory")
                print("Saving as url_sniffer_output.txt in the directory")
                out_path += "/url_sniffer_output.txt"
            with open(out_path, 'w') as file:
                line = 1
                for url in result:
                    print(line, url)
                    file.write(str(line) + " " + url + '\n')
                    line += 1
        else:
            line = 1
            for url in result:
                print(line, url)
                line += 1
    else:
        print("No recognisable url found!")


def get_path(path=""):
    while True:
        if path is not None:
            path = input("Feed the path to file: ")
        if os.path.isfile(path):
            main(path)
            break
        else:
            print("No file found at the Path give!")


try:
    if len(sys.argv) == 1:
        get_path()

    else:
        path2file = sys.argv[1]
        get_path(path2file)
    print("\nOperation completed!\n")
except:
    print("\nERROR! Operation could not be completed!\n")
