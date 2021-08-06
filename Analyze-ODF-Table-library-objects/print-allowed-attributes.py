import odf.table

print('Table object has the following attributes\n')
table = odf.table.Table()
table_attributes = table.allowed_attributes()
table_attributes_str = [str(element) for element in table_attributes]
table_attributes_str_print = "\n".join(table_attributes_str)
print(table_attributes_str_print)

print('\n\nTableCell object has the following attributes\n')
tablecell = odf.table.TableCell()
tablecell_attributes = tablecell.allowed_attributes()
tablecell_attributes_str = [str(element) for element in tablecell_attributes]
tablecell_attributes_str_print = "\n".join(tablecell_attributes_str)
print(tablecell_attributes_str_print)

print('\n\nTableColumn object has the following attributes\n')
tablecolumn = odf.table.TableColumn()
tablecolumn_attributes = tablecolumn.allowed_attributes()
tablecolumn_attributes_str = [str(element) for element in tablecolumn_attributes]
tablecolumn_attributes_str_print = "\n".join(tablecolumn_attributes_str)
print(tablecolumn_attributes_str_print)

print('\n\nTableColumns object has the following attributes\n')
tablecolumns = odf.table.TableColumns()
tablecolumns_attributes = tablecolumns.allowed_attributes()
tablecolumns_attributes_str = [str(element) for element in tablecolumns_attributes]
tablecolumns_attributes_str_print = "\n".join(tablecolumns_attributes_str)
print(tablecolumns_attributes_str_print)

print('\n\nTableRow object has the following attributes\n')
tablerow = odf.table.TableRow()
tablerow_attributes = tablerow.allowed_attributes()
tablerow_attributes_str = [str(element) for element in tablerow_attributes]
tablerow_attributes_str_print = "\n".join(tablerow_attributes_str)
print(tablerow_attributes_str_print)


print('\n\nTableRows object has the following attributes\n')
tablerows = odf.table.TableRows()
tablerows_attributes = tablerows.allowed_attributes()
tablerows_attributes_str = [str(element) for element in tablerows_attributes]
tablerows_attributes_str_print = "\n".join(tablerows_attributes_str)
print(tablerows_attributes_str_print)





