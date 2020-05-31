import subprocess
from rich import print


# If Chrome Browser is not installed on your local machine, 
# Prior command you should carry is "sh chrome_download.sh" on current directory.


# Relase Version Check

shell_cmd = subprocess.run(['google-chrome', '--version'],
                         stdout=subprocess.PIPE,
                         universal_newlines=True)
chrome_version = shell_cmd.stdout

if 'Google Chrome' in chrome_version:
    release_version = chrome_version.split('Google Chrome ')[1].split('.')[0]

else:
    subprocess.run(['sh', 'chrome_download.sh'], 
                stdout=subprocess.PIPE,
                universal_newlines=True)
    release_version = chrome_version.split('Google Chrome ')[1].split('.')[0]



# Get a download index of corresponding chrome driver

if release_version=='84':
    driver_index = 'https://chromedriver.storage.googleapis.com/84.0.4147.30/chromedriver_linux64.zip'


elif release_version=='83':
    driver_index = 'https://chromedriver.storage.googleapis.com/83.0.4103.39/chromedriver_linux64.zip'


elif release_version =='81':
    driver_index = 'https://chromedriver.storage.googleapis.com/81.0.4044.138/chromedriver_linux64.zip'


else:
    print('Release versions of 84.x, 83.x, 81.x are only supported currently'
            +', please upgrade or downgrade release version')




# Download chrome-driver on current directory and unzip it.

if driver_index:
    subprocess.run(['wget', '-N', driver_index],stdout=subprocess.PIPE,universal_newlines=True)
    subprocess.run(['unzip', 'chromedriver_linux64.zip'],stdout=subprocess.PIPE,universal_newlines=True)
    subprocess.run(['chmod', '+x', 'chromedriver'],stdout=subprocess.PIPE,universal_newlines=True)
    subprocess.run(['rm','chromedriver_linux64.zip'],stdout=subprocess.PIPE,universal_newlines=True)
else:
    None
