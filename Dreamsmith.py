#This code imports the necessary modules.

from flask import Flask, request, render_template, send_file, session
import random
import os
from collections import defaultdict
import re
from unidecode import unidecode
from string import digits
import datetime

#This code configures the web app.

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'pgojaeopatreraiern'

@app.route('/', methods=['POST', 'GET'])
def dreamquery():

    return render_template('dreamquery.html')

@app.route('/dreamresultprose', methods=['POST', 'GET'])
def dreamresultprose():

    textchunk = request.form["prosechunk"]

    right_now = datetime.datetime.now().isoformat()
    list = []

    for i in right_now:
        if i.isnumeric():
            list.append(i)

    time = ("".join(list))
   
    try:

        sublst = textchunk.split()

    except:

        print("Unicode failure.")

    wdlst = []

    for elem in sublst:

        elem2 = elem.strip()

        if elem2[0] != "." and elem2[0] != "!" and elem2[0] != "?":

            wdlst.append(elem2)

    subl = []

    bigl = []

    sub2 = []

    lam = len(wdlst)

    for x in range(20):
        y = random.randrange(lam)
        adstr = wdlst[y]
        if len(adstr) > 5:
            sub2.append(wdlst[y])

    sennum = 0

    for elem in wdlst:
        if len(subl) > 0:

            subl.append(elem)

        if len(subl) == 0:

            elem2 = elem[0].upper() + elem[1:]
            subl.append(elem2)

        if elem.endswith(".") or elem.endswith("!") or elem.endswith("?") :
            flg = 0
            for elem3 in subl:
                if elem3 in sub2:
                    flg += 1
            if flg > 0:
                bigl.append(subl)
                sennum += 1
                parran = random.randrange(5)
                if parran > 3 and sennum > 4 and len(subl) > 4:
                    bigl.append('\n')
                    bigl.append('\n')
                    sennum = 0

            subl = []

    ctr = len(bigl)

    if ctr > 300:
        ctr = 300

    lim = ctr - 5

    polst = []

    for x in range (ctr):
        lin = random.randrange(lim)

        rem = random.randrange(1,3)

        for y in range(rem):

            polst.append(bigl[lin + y])

        polst.append("")

    bigstr = ""


    for elem in polst:
        for elem2 in elem:

            if elem != '\n':

                bigstr += elem2 + " "


            if elem == '\n':

                bigstr += elem2 

    endstr = unidecode(bigstr)

    #endstr2 = endstr.replace("THE CASTLE", "")
    #endstr5 = endstr2.replace("ANOTHER VERSION", "")
    #remove_digits = str.maketrans('', '', digits)
    #endstr5 = endstr3.translate(remove_digits)

    ounm = "Short_Prose_Dream_" + time + ".txt"

    oun = "Short Prose Dream " + time 

    session['textfile'] = ounm

    outfile = open(ounm, "w")

    outfile.write(oun + '\n')

    outfile.write( '\n')

    try:
        outfile.write(endstr + '\n')
    except:
        print("")
        print("Unicode error")

    outfile.close()       

    return render_template('dreamresultprose.html', textfile = ounm )

@app.route('/dreamresultpoetry', methods=['POST', 'GET'])
def dreamresultpoetry():


    textchunk = request.form["poetrychunk"]

    
    right_now = datetime.datetime.now().isoformat()
    list = []

    for i in right_now:
        if i.isnumeric():
            list.append(i)

    time = ("".join(list))
   
    try:

        sublst = textchunk.split()

    except:

        print("Unicode failure.")

    wdlst = []

    for elem in sublst:

        elem2 = elem.strip()

        if elem2[0] != "." and elem2[0] != "!" and elem2[0] != "?":

            wdlst.append(elem2)

    subl = []

    bigl = []

    sub2 = []

    lam = len(wdlst)

    for x in range(20):
        y = random.randrange(lam)
        adstr = wdlst[y]
        if len(adstr) > 5:
            sub2.append(wdlst[y])

    sennum = 0

    for elem in wdlst:
        if len(subl) > 0:

            subl.append(elem)

        if len(subl) == 0:

            elem2 = elem[0].upper() + elem[1:]
            subl.append(elem2)

        if elem.endswith(".") or elem.endswith("!") or elem.endswith("?") :
            flg = 0
            for elem3 in subl:
                if elem3 in sub2:
                    flg += 1
            if flg > 0:
                bigl.append(subl)
                sennum += 1
                parran = random.randrange(5)
                if parran > 3 and sennum > 4 and len(subl) > 4:
                    bigl.append('\n')
                    bigl.append('\n')
                    sennum = 0

            subl = []

    ctr = len(bigl)

    if ctr > 300:
        ctr = 300

    lim = ctr - 5

    polst = []

    for x in range (ctr):
        lin = random.randrange(lim)

        rem = random.randrange(1,3)

        for y in range(rem):

            polst.append(bigl[lin + y])

        polst.append("")

    bigstr = ""


    for elem in polst:
        for elem2 in elem:

            if elem != '\n':

                bigstr += elem2 + " "


            if elem == '\n':

                bigstr += elem2 

    endstr = unidecode(bigstr)

    #endstr2 = endstr.replace("THE CASTLE", "")
    #endstr5 = endstr2.replace("ANOTHER VERSION", "")
    #remove_digits = str.maketrans('', '', digits)
    #endstr5 = endstr3.translate(remove_digits)

    ounm = "Short_Poetic_Dream_" + time + ".txt"

    oun = "Short Poetic Dream " + time 

    session['textfile'] = ounm

    outfile = open(ounm, "w")

    outfile.write(oun + '\n')

    outfile.write( '\n')

    try:
        outfile.write(endstr + '\n')
    except:
        print("")
        print("Unicode error")

    outfile.close()       

    return render_template('dreamresultpoetry.html', textfile = ounm )

@app.route('/download', methods=['POST', 'GET'])
def download():
    st5 = session['textfile']
    return send_file(st5, attachment_filename=st5, as_attachment=True)

    ## THE GHOST OF THE SHADOW ##

if __name__ == "__main__":
    app.run()