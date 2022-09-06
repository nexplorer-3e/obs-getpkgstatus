import requests
from bs4 import BeautifulSoup
import csv
from config import *


def read():
    plist=[]
    kv={}
    for i in projRepoUrl:
        html = requests.get(projRepoUrl[i]).text
        b = BeautifulSoup(html, "html.parser").table.tbody
        _arch = dict(eval(b["data-tableinfo"]))[i]
        plist.append(i)
        d = eval(b["data-statushash"])[i][_arch]
        # rearrange dict struct
        for j in d:
            if j not in kv:
                kv[j]={i:d[j]["code"]}
            else:
                kv[j].update({i:d[j]["code"]})
    return kv, plist


def main():
    kv, rlist = read()
    with open(csvName, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([""] + rlist)
        for pname in kv:
            st = []
            for i in rlist:
                if i not in kv[pname]:
                    st+=[""]
                else:
                    st+=[kv[pname][i]]
            writer.writerow([pname]+st)



if __name__ == '__main__':
    main()
