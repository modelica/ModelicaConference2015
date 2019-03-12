# coding=utf-8

import subprocess, sys

assert(sys.argv[1].startswith("proceedings/html"))
rel = ""
for i in range(2,sys.argv[1].count("/")):
  rel = rel + "../"

output = open(sys.argv[1]).read()
output = output.replace(' class="selected"', "").strip()
head = \
"""<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">

<html>
    <head>
        <title>The 11th International Modelica Conference 2015</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    </head>
    <body>
        <p>
            <a style="border-bottom: 0px solid #ccc;" href="https://www.modelica.org/events/modelica2015" target="_blank">
                <img src="%sstatic/images/Modelica2015.svg" alt="Modelica2015" />
            </a>
        </p>
        <hr />
                        <ul>
                            <li><a href="%sindex.html">Home</a></li>
                            <li><a href="%ssessions/index.html">Sessions</a></li>
                            <li><a href="%sauthors/index.html">Authors</a></li>
                            <li><a href="%sschedule.html">Schedule</a></li>
                            <li><a href="%smaterial.html">Further material</a></li>
                        </ul>

        <hr />""" % (rel,rel,rel,rel,rel,rel)

foot = \
"""<hr />
        <h2>Organized by:</h2>
        <p>
            <a style="border-bottom: 0px solid #ccc;" href="http://www.3ds.com/"><img style="padding:5px;height:32px;width:auto;" src="%sstatic/images/3ds_logo.svg" alt="Dassault Syst&#232;mes" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
            <a style="border-bottom: 0px solid #ccc;" href="https://liu.se/"><img style="padding:5px;height:32px;width:auto;" src="%sstatic/images/liu_primary_black.svg" alt="Link&ouml;ping University" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
            <a style="border-bottom: 0px solid #ccc;" href="http://www.modelica.org"><img style="padding:5px;height:32px;width:auto;" src="%sstatic/images/ModelicaLogo.svg" alt="Modelica" /></a>
        </p>
        <hr />
        <h2>Sponsored by:</h2>
        <p>
            <a style="border-bottom: 0px solid #ccc;" href="http://www.claytex.com/"><img style="padding:5px;height:32px;width:auto;" src="%sstatic/images/claytexlogo.svg" alt="Claytex Services Limited" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
            <a style="border-bottom: 0px solid #ccc;" href="http://www.maplesoft.com/"><img style="padding:5px;height:32px;width:auto;" src="%sstatic/images/Maplesoft_logo.svg" alt="Maplesoft Europe" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
            <a style="border-bottom: 0px solid #ccc;" href="http://www.modelon.com"><img style="padding:5px;height:32px;width:auto;" src="%sstatic/images/modelonlogo.svg" alt="Modelon AB" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
            <a style="border-bottom: 0px solid #ccc;" href="http://www.3ds.com/"><img style="padding:5px;height:32px;width:auto;" src="%sstatic/images/3ds_logo.svg" alt="Dassault Syst&#232;mes" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
            <a style="border-bottom: 0px solid #ccc;" href="http://www.altair.com/"><img style="padding:5px;height:32px;width:auto;" src="%sstatic/images/Altair_logo.svg" alt="Altair" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
            <a style="border-bottom: 0px solid #ccc;" href="http://www.xrg-simulation.de/"><img style="padding:5px;height:32px;width:auto;" src="%sstatic/images/xrglogo.svg" alt="XRG Simulation GmbH" /></a>
        </p>
    </body>
</html>""" % (rel,rel,rel,rel,rel,rel,rel,rel,rel)

#print(output)
#print(head)
#print(rel)

assert(head in output)
assert(foot in output)
output = output.replace(head, "").replace(foot, "")
output = output.strip()

mdfile = sys.argv[1].replace(".html",".md")
open(mdfile, "w").write(output)
subprocess.check_output(["git", "add", mdfile])
subprocess.check_output(["git", "rm", sys.argv[1]])
