# Advent of code working directories creator
# IMPORTANT Remember to edit the USER_SESSION_ID & author values with yours
# uses requests module. If not present use pip install requests
# Author = Alexe Simon
# Date = 06/12/2018

import os
from shutil import copy2
import glob
try:
    import requests
except ImportError:
    sys.exit("You need requests module. Install it by running pip install requests.")

# USER SPECIFIC PARAMETERS
base_pos = "./"            # Folders will be created here. If you want to make a parent folder, change this to ex "./adventofcode/"
USER_SESSION_ID = "53616c7465645f5f81ae720ff248fbb5f6c9d4041a64961b5fb07d1a7333fe7d71b8b2f3baeb4968968a29b24c732a76a890bbd7ede88134b61d03874f65e92a"       # Get your session by inspecting the session cookie content in your web browser while connected to adventofcode and paste it here as plain text in between the ". Leave at is to not download inputs.
DOWNLOAD_STATEMENTS = False # Set to false to not download statements. Note that only part one is downloaded (since you need to complete it to access part two)
DOWNLOAD_INPUTS = True     # Set to false to not download inputs. Note that if the USER_SESSION_ID is wrong or left empty, inputs will not be downloaded.
MAKE_CODE_TEMPLATE = True  # Set to false to not make code templates. Note that even if OVERWRITE is set to True, it will never overwrite codes.
MAKE_URL = False            # Set to false to not create a direct url link in the folder.
author = "Rajesh M R"               # Name automatically put in the code templates.
OVERWRITE = False          # If you really need to download the whole thing again, set this to true. As the creator said, AoC is fragile; please be gentle. Statements and Inputs do not change. This will not overwrite codes.

# DATE SPECIFIC PARAMETERS
date = "December 2023"              # Date automatically put in the code templates.
starting_advent_of_code_year = 2024 # You can go as early as 2015.
last_advent_of_code_year = 2024     # The setup will download all advent of code data up until that date included
last_advent_of_code_day = 3       # If the year isn't finished, the setup will download days up until that day included for the last year
# Imports

# Code
MAX_RECONNECT_ATTEMPT = 2
years = range(starting_advent_of_code_year, last_advent_of_code_year+1)
days = range(1,26)
link = "https://adventofcode.com/" # ex use : https://adventofcode.com/2017/day/19/input
USER_AGENT = "adventofcode_working_directories_creator"


print("Setup will download data and create working directories and files for adventofcode.")
if not os.path.exists(base_pos):
    os.mkdir(base_pos)
for y in years:
    print("Year "+str(y))
    if not os.path.exists(base_pos+str(y)):
        os.mkdir(base_pos+str(y))
    year_pos = base_pos + str(y)
    for d in (d for d in days if (y < last_advent_of_code_year or d <= last_advent_of_code_day)):
        print("    Day "+str(d))
        day_pos = f"{d:02}"  # Zero padding for day
        print("day_pos: "+day_pos)
        print("year_pos: "+year_pos)
        print(str(year_pos + '/day_' + day_pos))
        if not os.path.exists(year_pos + "/day_" + day_pos):
            os.mkdir(year_pos + "/day_" + day_pos)

        # if MAKE_CODE_TEMPLATE and not os.path.exists(day_pos+"/code.py"):
        #     code = open(day_pos+"/code.py", "w+")
        #     code.write("# Advent of code Year "+str(y)+" Day "+str(d)+" solution\n# Author = "+author+"\n# Date = "+date+"\n\nwith open((__file__.rstrip(\"code.py\")+\"input.txt\"), 'r') as input_file:\n    input = input_file.read()\n\n\n\nprint(\"Part One : \"+ str(None))\n\n\n\nprint(\"Part Two : \"+ str(None))")
        #     code.close()
        if MAKE_CODE_TEMPLATE and not (os.path.exists(year_pos + "/day_" + day_pos + "/puzzle.py") and glob.glob(year_pos + "/day_" + day_pos + "/test_puzzle_day_*.py")):
            # Copy puzzle.py and test_puzzle_day_.py from template folder
            # template_path = os.path.join(year_pos, "template")
            template_path = os.path.join(os.getcwd(), "template")  
            print("template path: "+template_path)
            copy2(os.path.join(template_path, "puzzle.py"), os.path.join(year_pos + "/day_" + day_pos, "puzzle.py"))
            copy2(os.path.join(template_path, "test_puzzle_day_.py"), os.path.join(year_pos + "/day_" + day_pos, f"test_puzzle_day_{d}.py"))                
        if DOWNLOAD_INPUTS and (not os.path.exists(year_pos + "/day_" + day_pos + "/input.txt") or OVERWRITE)and USER_SESSION_ID != "":
            done = False
            error_count = 0
            while(not done):
                try:
                    with requests.get(url=link+str(y)+"/day/"+str(d)+"/input", cookies={"session": USER_SESSION_ID}, headers={"User-Agent": USER_AGENT}) as response:
                        if response.ok:
                            data = response.text
                            input = open(year_pos + "/day_" + day_pos + "/input.txt", "w+")
                            input.write(data.rstrip("\n"))
                            input.close()
                        else:
                            print("        Server response for input is not valid.")
                    done = True
                except requests.exceptions.RequestException:
                    error_count += 1
                    if error_count > MAX_RECONNECT_ATTEMPT:
                        print("        Giving up.")
                        done = True
                    elif error_count == 0:
                        print("        Error while requesting input from server. Request probably timed out. Trying again.")
                    else:
                        print("        Trying again.")
                except Exception as e:
                    print("        Non handled error while requesting input from server. " + str(e))
                    done = True
        if DOWNLOAD_STATEMENTS and (not os.path.exists(year_pos + "/day_" + day_pos + "/statement.html") or OVERWRITE):
            done = False
            error_count = 0
            while(not done):
                try:
                    with requests.get(url=link+str(y)+"/day/"+str(d), cookies={"session": USER_SESSION_ID}, headers={"User-Agent": USER_AGENT}) as response:
                        if response.ok:
                            html = response.text
                            start = html.find("<article")
                            end = html.rfind("</article>")+len("</article>")
                            end_success = html.rfind("</code>")+len("</code>")
                            statement = open(year_pos + "/day_" + day_pos + "/statement.html", "w+")
                            statement.write(html[start:max(end, end_success)])
                            statement.close()
                        done = True
                except requests.exceptions.RequestException:
                    error_count += 1
                    if error_count > MAX_RECONNECT_ATTEMPT:
                        print("        Error while requesting statement from server. Request probably timed out. Giving up.")
                        done = True
                    else:
                        print("        Error while requesting statement from server. Request probably timed out. Trying again.")
                except Exception as e:
                    print("        Non handled error while requesting statement from server. " + str(e))
                    done = True
        if MAKE_URL and (not os.path.exists(year_pos + "/day_" + day_pos + "/link.url") or OVERWRITE):
            url = open(year_pos + "/day_" + day_pos + "/link.url", "w+")
            url.write("[InternetShortcut]\nURL="+link+str(y)+"/day/"+str(d)+"\n")
            url.close()
print("Setup complete : adventofcode working directories and files initialized with success.")