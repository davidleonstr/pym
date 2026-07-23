# Server config
from pym.server.config import SERVER

import time
from datetime import date

def log(*args, type: str = 'info', addtime: bool = True) -> None:
    """
    Function to add logs in logs file definite in server config if logs are enabled.

    Args:
        type (str): Log type. 
            Choices:
                alert: Show alert.
                critical: Shows critical.
                info: Shows information.
                important: Show important information.
                warning: Shows warning.
                error: Shows error.
                var: Show any type of information.
        
        addtime (bool): Add datetime tag at the end of line.
    """
    # Log time
    ts = time.time()

    # Default log types
    tags = {
        'alert': '[ALERT]',
        'critical': '[CRITICAL]',
        'important': '[IMPORTANT]',
        'info': '[INFO]',
        'warning': '[WARNING]',
        'error': '[ERROR]',
        'var': '[VAR]'
    }

    # If logs are enabled
    if SERVER['logs']:
        # Open the file as file
        with open(SERVER['logs-file'], 'a') as file:
            text = ''.join(str(a) for a in args)

            # If it needs time
            if addtime:
                local = time.localtime(ts)
                ms = int((ts % 1) * 100)
                text += ' '
                text += f"[{date.today()} {time.strftime('%H:%M:%S', local) + f'.{ms:02}'}]"
            
            # Add tag to text
            file.write(tags[type] + ' ' + text + '\n')