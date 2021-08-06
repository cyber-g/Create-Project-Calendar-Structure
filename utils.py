from odf.table import TableCell, TableRow
from odf.text import P

import numpy as np

def addEmptyCells(row,emptycellnumber):
    """
    Adds empty cells
    """
    for cellcount in range(emptycellnumber):
        # create empty cell
        cell = TableCell()
        # add content to cell
        cell.addElement(P())
        # add cell to row
        row.addElement(cell)

def generateRowText(cells_strings,column_position,last_column):
    """
    Generates a row positioning each string at each given position
    """
    if len(cells_strings)==len(column_position):
        pass
    else:
        raise Exception('Number of strings does not match number of positions')
    
    column_position_extended = np.append(column_position,last_column)

    # Instanciate 1 row
    row = TableRow()

    for index in range(len(cells_strings)):
        text_str    = cells_strings[index]
        col_start   = column_position_extended[index]
        col_end     = column_position_extended[index+1]-1
        ### instanciate 1st cell
        # create empty cell
        cell = TableCell(numbercolumnsspanned=int(col_end-col_start+1))
        # add content to cell
        cell.addElement(P(text=text_str))
        # add cell to row
        row.addElement(cell)
        ### add empty cells
        addEmptyCells(row, col_end-col_start)
    return row

def generateRowNumeric(cells_values,column_position,last_column):
    """
    Generates a row positioning each string at each given position
    """
    if len(cells_values)==len(column_position):
        pass
    else:
        raise Exception('Number of strings does not match number of positions')
    
    column_position_extended = np.append(column_position,last_column)

    # Instanciate 1 row
    row = TableRow()

    for index in range(len(cells_values)):
        cell_value  = cells_values[index]
        col_start   = column_position_extended[index]
        col_end     = column_position_extended[index+1]-1
        ### instanciate 1st cell
        # create empty cell
        # cell = TableCell(value=cell_value,valuetype='float',stylename="Accent 3",numbercolumnsspanned=int(col_end-col_start+1))
        cell = TableCell(value=cell_value,valuetype='float',numbercolumnsspanned=int(col_end-col_start+1))
        # add cell to row
        row.addElement(cell)
        ### add empty cells
        addEmptyCells(row, col_end-col_start)
    return row

def applyStyle(row,style_object):
    for cell in row.getElementsByType(TableCell):
        cell.setAttribute('stylename', style_object.getAttribute('name'))

def addRowStyle(table,row,style):
    """
    Apply style and add row to table
    """
    # Apply style
    applyStyle(row,style)
    # Add row to table
    table.addElement(row)
