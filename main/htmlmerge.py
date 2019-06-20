from bs4 import BeautifulSoup


def double_shape(filenumber,filename):
    fnum="*"
    for i in range(filenumber-1):
        if i%2==1:
            fnum=fnum+",*"
    fname=""
    for i in range(len(filename)):
        if i%2==0:
            fname=fname+"<frameset cols=*,*>"
        fname=fname+"<frame src="+str(filename[i])+">"
        if i%2==1:
            fname=fname+"</frameset>"            

    print(fname)
                
    html_doc = "<html><frameset rows="+fnum+">"+fname+"</frameset>"
        
    q=BeautifulSoup(html_doc, 'html.parser')
    open('thing.html', "w").write(str(q))
def row_shape(filenumber,filename):
    fnum="*"
    for i in range(filenumber-1):
        if i%2==1:
            fnum=fnum+",*"
    fname=""
    for i in range(len(filename)):
        fname=fname+"<frame src="+str(filename[i])+">"

    print(fname)
                
    html_doc = "<html><frameset rows="+fnum+">"+fname+"</frameset>"
        
    q=BeautifulSoup(html_doc, 'html.parser')
    open('thing.html', "w").write(str(q))
def col_shape(filenumber,filename):
    fnum="*"
    for i in range(filenumber-1):
        if i%2==1:
            fnum=fnum+",*"
    fname=""
    for i in range(len(filename)):
        fname=fname+"<frame src="+str(filename[i])+">"

    print(fname)
                
    html_doc = "<html><frameset cols="+fnum+">"+fname+"</frameset>"
        
    q=BeautifulSoup(html_doc, 'html.parser')
    open('thing.html', "w").write(str(q))
