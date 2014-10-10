'''
Created on Jul 31, 2014

@author: naruto
'''
import re
import Conn_Exception
pattern='Device(-?|\s?)ID'
input_file='/home/naruto/Documents/WorkSpace/Cisco/conn_ssh/output.log'
delimiter_offset=1
def  parse_delimiter(str_delimiter):
    '''Hasta la hora la idea es tratar de buscar un nombre y un comando para crear el fichero
    en caso de que el delimitador falle con el parser se utiliza el modo manual, se levanta 
    la excepsion NameNotFound, se intercepta con el except y se ejecuta un metodo para forzar a 
    entrar manual'''
    assert type(str_delimiter) is str , 'delimiter must be an string'
    try:
        name=re.search('([0-9]+\.?)+', str_delimiter)
        if not name: raise Conn_Exception.NameNotFound()
        else: name=name.group()
        #raise Conn_Exception.NameNotFound() if not name else name=name.group()
        #name=name.groupif not name: raise Conn_Exception.NameNotFound()
    except Conn_Exception.NameNotFound as name_delimiter:
        name=name_delimiter._NameNotFound__mannually()
    command=re.search('([a-z]+\s)+', str_delimiter).group()
    return name, command

def main():
    """

    :rtype : this function does not return anything it only create a file in the same directory.
    """
    f1=open(input_file).readlines()
    delimiter=f1[delimiter_offset]
    print('delimiter: ', delimiter)
    output_file_host, output_file_command = parse_delimiter(delimiter)
    print("String to use as name for the output file: ", output_file_host, output_file_command)
    offset = []
    for (i, y) in enumerate(f1):
        if y == delimiter:
            offset.append(i)
    print('Between these offsets you have the important information', offset)
    f2=f1[offset[0]+1:offset[1]-1]
    heading_offset=[i for (i,ii) in enumerate(f2) if re.match(pattern, ii)]
    print('Use this offsets as the heading of the CSV table: ', heading_offset)
    str_heading, table=f2[heading_offset[0]].rstrip(), f2[heading_offset[0]+1:]
    heading=re.split('\s{2,3}', str_heading)
    heading=[i for i in heading if i]
    print('Heading of the CSV table ', heading)
    print('table: ', table)
    
def limits(input_file, pattern):
    return [i for (i, y) in enumerate(input_file) if y==pattern]
if __name__ == '__main__':
    main()