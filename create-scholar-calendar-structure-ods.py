# Compute key elements
import datetime
from dateutil.relativedelta import relativedelta

# https://stackoverflow.com/questions/985505/locale-date-formatting-in-python
# https://stackoverflow.com/questions/14547631/python-locale-error-unsupported-locale-setting
import locale
locale.setlocale(locale.LC_TIME, "fr_FR.utf-8")

# datetime.date(year, month, day)
# Attention, ce script a été concu avec l'hypothèse que le calendrier commence un 1er du mois ! 
DATE_START = datetime.date(2021, 8, 1)
TIME_SPAN  = 13 # months
DATE_END   = DATE_START+relativedelta(months=+TIME_SPAN)
DAYS_SPAN = DATE_END-DATE_START
number_of_columns = DAYS_SPAN.days

# Generate days cell array
days_cell_array = []
for daysindex in range(number_of_columns):
    # https://stackoverflow.com/questions/546321/how-do-i-calculate-the-date-six-months-from-the-current-date-using-the-datetime
    date_incremented = DATE_START+relativedelta(days=+daysindex)
    date_str = date_incremented.strftime("%A %d %b %Y")
    days_cell_array.append(date_str)

# Generate Month cell array
month_cell_array = []
for monthindex in range(TIME_SPAN):
    # https://stackoverflow.com/questions/546321/how-do-i-calculate-the-date-six-months-from-the-current-date-using-the-datetime
    date_incremented = DATE_START+relativedelta(months=+monthindex)
    # https://www.studytonight.com/python-howtos/how-to-get-month-name-from-month-number-in-python
    month_name = date_incremented.strftime("%b")
    # print("Short name: ",month_name)
    month_cell_array.append(month_name)

# Generate Quarter cell array
month_values = []
for monthindex in range(TIME_SPAN):
    date_incremented = DATE_START+relativedelta(months=+monthindex)
    month_values.append(date_incremented.month)

import numpy as np
quarter_values_vec = np.floor((np.array(month_values[::3])-1)/3).astype(int)+1

quarter_cell_array = []
for q_val in quarter_values_vec:
    quarter_cell_array.append('T'+str(q_val))

# Generate Year cell array
year_values = []
for monthindex in range(TIME_SPAN):
    date_incremented = DATE_START+relativedelta(months=+monthindex)
    year_values.append(date_incremented.year)

# year_values_uniq = np.unique(np.array(year_values)).astype('str')
year_values_uniq = np.unique(np.array(year_values))

# Generate Column transitions
# Months
# col_transition_num_month = np.arange(start=0,stop=number_of_columns,step=2)+1
col_transition_num_month = []
for monthindex in range(TIME_SPAN):
    # https://stackoverflow.com/questions/546321/how-do-i-calculate-the-date-six-months-from-the-current-date-using-the-datetime
    date_incremented = DATE_START+relativedelta(months=+monthindex)
    delta = date_incremented-DATE_START
    col_transition_num_month.append(delta.days+1)

# Quarters
month_values_mat = []
for daysindex in range(number_of_columns):
    # https://stackoverflow.com/questions/546321/how-do-i-calculate-the-date-six-months-from-the-current-date-using-the-datetime
    date_incremented = DATE_START+relativedelta(days=+daysindex)
    month_values_mat.append(date_incremented.month)

month_values_vec = np.array(month_values_mat)
quarter_values_vec_expanded = np.floor((month_values_vec-1)/3).astype(int)+1
col_transition_num_quarter = np.nonzero(np.diff(quarter_values_vec_expanded))[0]+2
col_transition_num_quarter = np.insert(col_transition_num_quarter, 0, 1)
# years
col_transition_num_year = np.nonzero(np.diff(np.floor(month_values_vec/12))==-1)[0]+2
col_transition_num_year = np.insert(col_transition_num_year, 0, 1)

################################################################
# Create table
################################################################

from odf.opendocument import OpenDocumentSpreadsheet
from odf.table import Table, TableRow, TableCell, CellAddress
from odf.text import P
from utils import addEmptyCells, generateRowText, generateRowNumeric, addRowStyle
# Inpsired by https://stackoverflow.com/questions/63667613/merge-cells-with-odfpy

import mystyles

# Basic document structure
document = OpenDocumentSpreadsheet()
table = Table(name="Table1")
document.spreadsheet.addElement(table)

# Add styles to document
document.styles.addElement(mystyles.yearstyle)
document.styles.addElement(mystyles.quarterstyle)
document.styles.addElement(mystyles.monthstyle)
document.styles.addElement(mystyles.daystyle)

# Instanciate Year row
tr = generateRowNumeric(year_values_uniq, col_transition_num_year, number_of_columns+1)
addRowStyle(table,tr,mystyles.yearstyle)

# Instanciate Quarter row
tr = generateRowText(quarter_cell_array, col_transition_num_quarter, number_of_columns+1)
addRowStyle(table,tr,mystyles.quarterstyle)

# Instanciate Month row
tr = generateRowText(month_cell_array, col_transition_num_month, number_of_columns+1)
addRowStyle(table,tr,mystyles.monthstyle)

# Instanciate HalfMonth row
tr = generateRowText(days_cell_array, np.arange(number_of_columns)+1, number_of_columns+1)
addRowStyle(table,tr,mystyles.daystyle)


# Generate file
document.save("Planning.ods")

