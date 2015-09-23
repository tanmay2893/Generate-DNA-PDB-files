import mechanize,os,urllib2,urllib,requests,time,random,string
from bs4 import BeautifulSoup
br=mechanize.Browser()

def getCode(length = 10, char = ['A','T','G','C']):
    return ''.join(random.choice( char) for x in range(length))

url='http://www.scfbio-iitd.res.in/software/drugdesign/bdna.jsp'
i=0
while i!=100:
    try:
        i+=1
        name=getCode() # or a specific DNA could be given
        print name
        res=br.open(url)
        br.select_form("form1")
        br.form['dna'] = ['BDNA']
        br.form['seq'] = name
        res=br.submit()
        content=res.read()
        x=content.find('<a href="http://www.scfbio-iitd.res.in/software/drugdesign/ABDNA/')
        y=content.find('>',x)
        link=(content[x:y])[9:-1]
        print link
        urllib.urlretrieve (link, name+'.pdb')
        print 'done'
        time.sleep(3)
    except:
        time.sleep(100)
