import odf.table

print('Table object has the following children\n')
table = odf.table.Table()
table_children = table.allowed_children
table_children_str = [str(element) for element in table_children]
table_children_str_print = "\n".join(table_children_str)
print(table_children_str_print)

print('\n\nTableCell object has the following children\n')
tablecell = odf.table.TableCell()
tablecell_children = tablecell.allowed_children
tablecell_children_str = [str(element) for element in tablecell_children]
tablecell_children_str_print = "\n".join(tablecell_children_str)
print(tablecell_children_str_print)

print('\n\nTableColumn object has the following children\n')
tablecolumn = odf.table.TableColumn()
tablecolumn_children = tablecolumn.allowed_children
tablecolumn_children_str = [str(element) for element in tablecolumn_children]
tablecolumn_children_str_print = "\n".join(tablecolumn_children_str)
print(tablecolumn_children_str_print)

print('\n\nTableColumns object has the following children\n')
tablecolumns = odf.table.TableColumns()
tablecolumns_children = tablecolumns.allowed_children
tablecolumns_children_str = [str(element) for element in tablecolumns_children]
tablecolumns_children_str_print = "\n".join(tablecolumns_children_str)
print(tablecolumns_children_str_print)

print('\n\nTableRow object has the following children\n')
tablerow = odf.table.TableRow()
tablerow_children = tablerow.allowed_children
tablerow_children_str = [str(element) for element in tablerow_children]
tablerow_children_str_print = "\n".join(tablerow_children_str)
print(tablerow_children_str_print)


print('\n\nTableRows object has the following children\n')
tablerows = odf.table.TableRows()
tablerows_children = tablerows.allowed_children
tablerows_children_str = [str(element) for element in tablerows_children]
tablerows_children_str_print = "\n".join(tablerows_children_str)
print(tablerows_children_str_print)





