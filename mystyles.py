### Set styles
# Inspired by https://github.com/eea/odfpy/blob/master/examples/ods-currency.py
# list of properties is $HOME/.local/lib/python3.8/site-packages/odf/grammar.py
# example values 
#   - http://officeopenxml.com/WPstyleParStyles.php
#   - http://officeopenxml.com/WPtableCellProperties-verticalAlignment.php
# The bast way to define styles is to set it up in OpenOffice, save the document with the styles,
# unzip the ods file, and look at the styles.xml file
from odf.style import Style, TextProperties, TableCellProperties, ParagraphProperties

# Year style
yearstyle = Style(name="Year style", family="table-cell")
yearstyle.addElement(TextProperties(fontfamily="Arial", fontsize="15pt",fontweight="bold"))
yearstyle.addElement(TableCellProperties(verticalalign="middle",backgroundcolor="#dddddd",border="0.1pt solid #000000"))
yearstyle.addElement(ParagraphProperties(textalign="center"))

# quarter style
quarterstyle = Style(name="Quarter style", family="table-cell")
quarterstyle.addElement(TextProperties(fontfamily="Arial", fontsize="13pt",fontweight="bold"))
quarterstyle.addElement(TableCellProperties(verticalalign="middle",backgroundcolor="#dddddd",border="0.1pt solid #000000"))
quarterstyle.addElement(ParagraphProperties(textalign="center"))

# Month style
monthstyle = Style(name="Month style", family="table-cell")
monthstyle.addElement(TextProperties(fontfamily="Arial", fontsize="13pt"))
monthstyle.addElement(TableCellProperties(verticalalign="middle",backgroundcolor="#dddddd",border="0.1pt solid #000000"))
monthstyle.addElement(ParagraphProperties(textalign="center"))

# HalfMonth style
halfmonthstyle = Style(name="Half Month style", family="table-cell")
halfmonthstyle.addElement(TextProperties(fontfamily="Arial", fontsize="13pt"))
halfmonthstyle.addElement(TableCellProperties(verticalalign="middle",backgroundcolor="#eeeeee",border="0.1pt solid #000000"))
halfmonthstyle.addElement(ParagraphProperties(textalign="center"))