import ezodf
import argparse
import numpy as np
import os

def main():
    
    scriptname = 'off2np' 
    parser = argparse.ArgumentParser()

    # Main Arguments
    parser.add_argument('odsin', type = str, nargs = '+', help = 'Name of the ods.')
    parser.add_argument('-h','--head', type = str, default = '/lustre/ap/litv-exp/2021-05-00_E143_TwoPhotonDeday_ssanjari/NTCAP/iq/IQ_2021-05-10_00-14-45/', nargs = '?', help = 'Path')
    parser.add_argument('-t','--tail', type = str, default = '.iq.tdms', nargs = '?', help = 'Extension')

    args = parser.parse_args()

    controller(args.odsin[0],  args.head, args.tail)

    
def controller(odsin, head, tail):
    
    try:
        with open(odsin, 'r') as f:
            pass
    except FileNotFoundError:
        print(f'File not found: {odsin}')
    except PermissionError:
        print(f'Permission denied: cannot read {odsin}')
    except Exception as e:
        print('Error reading file:', e)
        
    # Open the .ods file    
    odsinfo = ezodf.opendoc(odsin)
    # Get the first sheet
    sheet = odsinfo.sheets[0]
    array = np.array([])
    for row in range(1, sheet.nrows()):
        for col in range(sheet.ncols()):
            cell = sheet[row, col].value
            if col == 0:
                if cell is None: break
                array = np.append(array, int(cell))
            elif col == 1:
                if cell is None:
                    cell = array[-2]
                if len(str(cell)) < 7:
                    cell = head + str(int(cell)).zfill(7) + tail
                array = np.append(array, cell)
    offset_list = np.reshape(array, (sheet.nrows() - 1 - 2 -2, 2))
    return offset_list

if __name__ == '__main__':
    main()
