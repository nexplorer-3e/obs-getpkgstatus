import csv

import requests
from bs4 import BeautifulSoup

from config import *


def getGiteeData(plist):
    # todo: show specific branch status not only newest commit
    # get git source data, copied from src-oe-verinfo
    for pkg in plist:
        # print ('obs package', pkg)
        for s in projRepoUrl:
            service_url = projRepoUrl[s].replace("project/monitor", "package/view_file") + '{}/_service'.format(pkg)
            service_resp = requests.get(service_url, auth=HTTPBasicAuth(account['user'], account['password']))
            service_data = service_resp.text
        # print ('service_data', service_data)
        git_pattern = '<param name="url">.*</param>'
        revision_pattern = '<param name="revision">.*</param>'
        try:
            gitinfo = re.search(git_pattern, service_data).group()
            revision = re.search(revision_pattern, service_data).group()
            # print (gitinfo)
            # print (revision)
            gitinfo = re.search('>.*<', gitinfo).group()[1:-1]
            revision = re.search('>.*<', revision).group()[1:-1]
            if len(revision) == 0:
                revision = 'None'
            # print ('git', gitinfo)
            # print ('revision', revision)
        except:
            gitinfo = 'None'
            revision = 'None'
            print('Cannot get url and revision!')

    for p in plist:

    pass


def read():
    # todo: auto get branched packages status
    plist = []
    kv = {}
    for i in projRepoUrl:
        html = requests.get(projRepoUrl[i]).text
        b = BeautifulSoup(html, "html.parser").table.tbody
        _arch = dict(eval(b["data-tableinfo"]))[i]
        plist.append(i)
        d = eval(b["data-statushash"])[i][_arch]
        # rearrange dict struct
        for j in d:
            if j not in kv:
                kv[j] = {i: d[j]["code"]}
            else:
                kv[j].update({i: d[j]["code"]})
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
                    st += [""]
                else:
                    st += [kv[pname][i]]
            writer.writerow([pname] + st)


if __name__ == '__main__':
    main()
