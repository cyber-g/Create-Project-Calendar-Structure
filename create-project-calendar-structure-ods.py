# Compute key elements
import datetime
from dateutil.relativedelta import relativedelta

# datetime.date(year, month, day)
# Attention, ce script a été concu avec l'hypothèse que le calendrier commence un 1er du mois ! 
DATE_START = datetime.date(2021, 10, 1)
TIME_SPAN  = 36 # months

number_of_columns = TIME_SPAN*2

# Generate HalfMonth cell array
halfmonth_cell_array = []
for monthindex in range(TIME_SPAN):
    halfmonth_cell_array.append('HM1')
    halfmonth_cell_array.append('HM2')

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
col_transition_num_month = np.arange(start=0,stop=number_of_columns,step=2)+1
# Quarters
month_values_mat = np.tile(np.array(month_values),(2,1))
month_values_vec = month_values_mat.ravel('F')
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
document.styles.addElement(mystyles.halfmonthstyle)

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
tr = generateRowText(halfmonth_cell_array, np.arange(number_of_columns)+1, number_of_columns+1)
addRowStyle(table,tr,mystyles.halfmonthstyle)


# Generate file
document.save("Planning.ods")

