import telnetlib
import login
import time
import cleanup
import pandas as pd


begin = time.perf_counter()

def recursiveBackup(args_array):
    if len(args_array) == 0:
        print('Base case reached!')
        return
    
    current_input = args_array[0]

    consoleServerIP = current_input[0]
    portNumber = current_input[1]
    hostnme = current_input[2]
    usrname = current_input[3]
    passwrd = current_input[4]

    endLine = f'{hostnme}#  !!!!!!!!!!'

    
    saved_screen = f'SavedScreens/SavedScreen_{consoleServerIP}_{portNumber}.txt'

    tn = telnetlib.Telnet(consoleServerIP, portNumber)

    login.loginSwitch(tn, hostnme, usrname, passwrd, saved_screen, consoleServerIP, portNumber)

    print(f'Writing backup commands to {hostnme}')

    tn.write(b'\n')
    tn.write(b'\n')
    tn.write(b'no page\n show run\n show run int\n show environment\n show interface transceiver\n show interface transceiver detail\n show module\n show system\n show power\n write memory\n !!!!!!!!!!\n')


    recursiveBackup(args_array[1:])

    print(f'Waiting until commands finish for {hostnme}')
    output = tn.read_until(endLine.encode('ascii')).decode('ascii')
    print(f'Endline match for {hostnme}, starting to write to file unprocessed')


    with open(f'BackupOutput/Unprocessed/{hostnme}_{consoleServerIP}_{portNumber}_Backup.txt', 'w') as backup_file:
        backup_file.write(output)
        backup_file.close()
    
    print(f'Unprocessed file created for {hostname}, begin removing empty lines')

    cleanup.removeSpaces(f'BackupOutput/Unprocessed/{hostnme}_{consoleServerIP}_{portNumber}_Backup.txt', hostnme)

    print(f'Empty lines removed from {hostname} file')








df_inputs = pd.read_excel('Aruba6300_Data_Inputs.xlsx')

args = []

for data_row in range(len(df_inputs)):

    console_server_IP = df_inputs.iloc[data_row]['SERVER IP']

    ### PORT is a numby.int64 data type, must convert to native pyton type with the item() method from numpy
    port = df_inputs.iloc[data_row]['PORT'].item()
    hostname = f'{df_inputs.iloc[data_row]["HOSTNAME"]}'
    username = f'{df_inputs.iloc[data_row]["USERNAME"]}\n'.encode('ascii')
    password = f'{df_inputs.iloc[data_row]["PASSWORD"]}\n'.encode('ascii')

    if password == b' \n':
        password = '\n'.encode('ascii')


    inputs = [console_server_IP, port, hostname, username, password]

    args.append(inputs)




recursiveBackup(args)

end = time.perf_counter()
print(f'code takes {end - begin} seconds')
