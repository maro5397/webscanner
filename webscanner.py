import sys
import scanfunc as scan
import subfunc as sub

def main():
    urlname = sys.argv[1]
    scan.webscan(urlname)
    scan.portscan(urlname)
    scan.dirscan(urlname)
    taglist = sub.maketaglist()
    scan.crawling(urlname, taglist)

if __name__ == '__main__':
    main()