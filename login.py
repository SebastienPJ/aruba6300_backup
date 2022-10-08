import validate
import time

def loginSwitch(tn, hostnme, username, passwrd, current_screen, server_ip, port):
    print(f'Logging into {hostnme}')
    formatted_hostnme = f'{hostnme}#'

    time.sleep(2)
    tn.write(b'\n')
    tn.write(b'\n')
    tn.write(b'\n')
    
    validate.saveCurrentScreen(tn, server_ip, port)
    prompt = validate.getCurrentPrompt(current_screen)


    while 'login:' not in prompt and formatted_hostnme not in prompt:
        tn.write(b'\n')

        validate.saveCurrentScreen(tn, server_ip, port)
        prompt = validate.getCurrentPrompt(current_screen)


    if formatted_hostnme not in prompt:

        tn.write(username)

        validate.saveCurrentScreen(tn, server_ip, port)
        prompt = validate.getCurrentPrompt(current_screen)

        tn.write(passwrd)

        validate.saveCurrentScreen(tn, server_ip, port)
        prompt = validate.getCurrentPrompt(current_screen)

        print(f'Logged into {hostnme} successfully')
    else:
        print(f'Already logged into {hostnme}')
    
