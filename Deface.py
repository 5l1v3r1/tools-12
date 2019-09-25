MRLINKERRORSSYTEM MATERI DEFACE :V

Deface page creator menggunakan python
ok pasti udah tau kan fungsi nya buat apa :)

save code dibawah dengan  creator.py  , cara exekusi nya cukup mudah 

diwindows : buka cmd lalu masuk ke direktory tempat lo save as skript nya , lalu tinggal exekusi

contoh : lo save di d:\

langsung aja ketik D:\>creator.py

code :


#!/usr/bin/python

mess = """======================================================
         ----Deface Page Creator----
         --==Created By Mrlinkerrorsystem==--
            An TEAM HACKER CYBER ARMY  
                 THCA
======================================================"""

print mess
title = raw_input("Enter the Title : ")
heading = raw_input("Enter the heading : ")
imagelink = raw_input("Enter the image link : ")
bgimage = raw_input("Enter the Background image Link(Optional) : ")
message = raw_input("Enter the message(use <br> for next line) : ")
textcolor = raw_input("Enter the text color : ")
youtubeid = raw_input("Enter the youtube id(Just Enter ID) : ")


#Open a file
fo = open("c:\Hacked.html","w")

messagescript1 = """<HTML><HEAD><TITLE>"""

messagescript2 = title

messagescript3 = """</TITLE></HEAD>
<BODY>

<br>

<BODY BGCOLOR="#000000" background ="""

messagescript4 = bgimage

messagescript5 = """>
<center>
<h1><center><font color=\"red\">"""

messagescript6 = heading

messagescript7 = """<h1></font>
<img src="""

messagescript8 = imagelink

messagescript9 = """ width=550px height=440px>


<body onload="init()"></body>
<body>

<div id="bulle"></div>"""

messagescript10 = """
<script language=\"JavaScript\">
var i=0
var j=0
var texteNE, affiche
var texte=\"<br><br><br><br><br><font color="""

messagescript11 = textcolor

messagescript12 = """ size=4>"""

messagescript13 = message

messagescript14 = """<br><br></font><br></b>\"
var ie = (document.all);
var ne = (document.layers);
function init(){
texteNE='';
machine_a_ecrire();
}
function machine_a_ecrire(){
texteNE=texteNE+texte.charAt(i)
affiche='<font face=verdana size=1 color=#ffffff><strong>'+texteNE+'</strong></font>'
if (texte.charAt(i)=="<") {
j=1
}
if (texte.charAt(i)==">") {
j=0
}
if (j==0) {
if (document.getElementById) { // avec internet explorer
document.getElementById("bulle").innerHTML = affiche;
}
}
if (i<texte.length-1){
i++
setTimeout("machine_a_ecrire()",70)
}
else
return
}
</script><font face="verdana" size="1"><blink><span  style="color: rgb(255, 255, 255);"><b><font color=lime  size=4></font></b></u></blink><br></font></b>
</body>
<SCRIPT LANGUAGE=\"JavaScript\">
<!-- Disable
function disableselect(e){
return false
}

function reEnable(){
return true
}

//if IE4+
document.onselectstart=new Function (\"return false\")
document.oncontextmenu=new Function (\"return false\")
//if NS6
if (window.sidebar){
document.onmousedown=disableselect
document.onclick=reEnable
}
//-->
</script>

<!-- DEBUT DU SCRIPT --><style>
.spanstyle {
    position:absolute;
    visibility:visible;
    top:-50px;
    font-size:12pt;
    font-family:Arial;
      font-weight:bold;
    color:#0000FF;
}
</style>
<script language=JavaScript>

/*

Cursor Trailor Text- By Peter Gehrig (http://www.24fun.ch/)

SCRIPT EDITE SUR L'EDITEUR JAVASCRIPT
http://www.editeurjavascript.com
URL du script : http://www.editeurjavascript.com/scripts/scripts_textes_1_78.php

*/

var x,y
var step=20
var flag=0

var message='Owned St0x0 '
message=message.split("")

var xpos=new Array()
for (i=0;i<=message.length-1;i++) {
    xpos[i]=-50
}

var ypos=new Array()
for (i=0;i<=message.length-1;i++) {
    ypos[i]=-50
}
function handlerMM(e){
    x = (navigator.appName.substring(0,3) == \"Net\") ? e.pageX : event.x+document.body.scrollLeft;
       y = (navigator.appName.substring(0,3) == \"Net\") ? e.pageY : event.y+document.body.scrollTop;
    flag=1
}

function makesnake() {
    if (flag==1 && document.getElementById) {
        for (i=message.length-1; i>=1; i--) {
               xpos[i]=xpos[i-1]+step
            ypos[i]=ypos[i-1]
        }
        xpos[0]=x+step
        ypos[0]=y

        for (i=0; i<message.length-1; i++) {
            var thisspan = document.getElementById('span'+(i)).style;
            thisspan.left=xpos[i]
            thisspan.top=ypos[i]
        }
    }
        var timer=setTimeout(\"makesnake()\",30)
}

</script>
<SCRIPT LANGUAGE="JavaScript">
<!-- Disable
function disableselect(e){
return false
}

function reEnable(){
return true
}

//if IE4+
document.onselectstart=new Function (\"return false\")
document.oncontextmenu=new Function (\"return false\")
//if NS6
if (window.sidebar){
document.onmousedown=disableselect
document.onclick=reEnable
}
//-->
</script>
<br>
<br>
<br>
<br>
<br>
<br>

<br>
<br>

<iframe width="0" height="0" src="http://www.youtube.com/v/"""

messagescript15 = youtubeid

messagescript16 = """&autoplay=1" frameborder="0"></iframe>"""


fo.write(messagescript1)
fo.write(messagescript2)
fo.write(messagescript3)
fo.write(messagescript4)
fo.write(messagescript5)
fo.write(messagescript6)
fo.write(messagescript7)
fo.write(messagescript8)
fo.write(messagescript9)
fo.write(messagescript10)
fo.write(messagescript11)
fo.write(messagescript12)
fo.write(messagescript13)
fo.write(messagescript14)
fo.write(messagescript15)
fo.write(messagescript16)

raw_input("\nPage Created Successfully and saved in c:\Hacked.html");

fo.close()

.thx