# -*- coding: utf-8 -*-
from typing import Any, List, Optional

def make_table(raw_data: List[List[Any]],rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """

    row_count = len(raw_data)
    columns = len(raw_data[0])
    table = ""
    max_length = [0]*columns;
    
    for i in range(columns):
        if labels != None:
            if max_length[i] < len(str(labels[i])):
                max_length[i] = len(str(labels[i]))

        for j in range(row_count):
            try:
                if max_length[i] < len(str(raw_data[j][i])):
                    max_length[i] = len(str(raw_data[j][i]))

            except:
               continue;

    for i in range(row_count):
        for j in range(columns):
            curr_len = len(str(raw_data[i][j]))
            extra_space = max_length[j] - curr_len +1
            remainder = extra_space - int(extra_space/2) - 1
            if centered:
                intermediate = " "*(remainder + 1)+ str(rows[i][j])+" "*(max_length[j] - curr_len + 1 - remainder)+"│"

            else:
                intermediate = " "+ str(rows[i][j])+" "*extra_space+"│"

            if j == 0 and i == 0 and labels == None:
                table += top_bottom_borders(True, columns, max_length)
            elif j == 0 and i == 0 and labels != None:
                table += label_borders(labels,max_length,columns,row_count,centered)

            if j == 0:
                table +="│"+ intermediate              
            elif i == columns -1:
                table += intermediate
            else :
                table +=  intermediate

            if j == columns - 1 and i == row_count - 1:
                table += top_bottom_borders(False, columns, max_length)

        table += "\n"
    return table
    
def top_bottom_borders(top,column_size,max_length = []):
    table = ""
    for j in range(column_size):
        if top:
                if j == 0 :
                    table += "┌"+"─"*(max_length[j]+2)
                    
                elif j != 0 and j != column_size -1:
                     table +="┬"+"─"*(max_length[j]+2) 

                if j == column_size -1 and column_size != 1:
                    table += "┬"+"─"*(max_length[j]+2)+ "┐\n"
                    
                elif j == column_size -1 and column_size == 1:
                    table += "┐\n"
                     
        else:
                if j == 0:
                    table += "\n"
                    table += "└"+"─"*(max_length[j]+2)

                elif j != 0 and j != column_size -1:
                    table +=  "┴"+"─"*(max_length[j]+2)
                    
                if j == column_size - 1 and column_size != 1:
                    table +="┴"+"─"*(max_length[j]+2)+ "┘"

                elif j == column_size -1 and column_size == 1:
                    table += "┘"
                        
    return table


def label_borders(labels,max_length,columns,rows, centered = False):
    table = ""
    table2 = ""
    table += top_bottom_borders(True, columns, max_length)
    for j in range(columns):
        curr_len = len(str(labels[j]))
        extra_space = max_length[j] - curr_len +1
        remainder = extra_space - int(extra_space/2) - 1
        if j != columns -1:
            if centered:
                table +=  "│"+" "*(remainder + 1)+ str(labels[j])+" "*(max_length[j] - curr_len + 1 - remainder)
            else :
                table += "│ "+ str(labels[j])+" "*extra_space
        else:
            if centered:
                table +=  "│"+" "*(remainder + 1) + str(labels[j])+" "*(max_length[j] - curr_len + 1 - remainder)+"│"
            else:
                table +=  "│ "+ str(labels[j])+" "*extra_space+"│"

        if j == 0 and columns  -1 != 0:
            table2 +=  "├"+"─"*(max_length[j]+2) +"┼"
        elif j==0:
            table2 +=  "├"+"─"*(max_length[j]+2)
            
        if j != 0 and j != columns - 1 and columns -1 != 0:
            table2 +=  "─"*(max_length[j]+2)+"┼"
        elif j == columns - 1 and columns-1 == 0:
            table2+="┤"
        elif j == columns-1 :
            table2 +=  "─"*(max_length[j]+2)+"┤"
            
    table += "\n"
    table += table2
    table += "\n"
    return table
                

