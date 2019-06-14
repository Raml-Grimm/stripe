



			------=[ KARDER SOCIETY CHECKER ]=------


			Please install python first in your PC / CP and add to path

			For Windows:
				Download the latest Python 3 at python.org and install it (As Admin)
				* MAKE SURE TO ADD IT ON PATH, IT LOCATES ON LOWER DOWN AT THE FIRST PART OF INSTALLAING *

			For Linux / Termux / GNU Root Debian:

				Run this Following command
				$ apt-get update
				$ apt-get install python

				Now Check if it installed
				$ python --version

				IF IT HAS NO ERROR, THEN ITS OK

			NOW RUN THIS FOLLOWING COMMANDS TO INSTALL REQUIREMENTS

			For Windows:
				Open The Command Prompt
				Then change the directory on the checker folder

				CMD> cd path/to/checker
				CMD> pip install -r requirements.txt

			For Linux / Termux / GNU Root Debian:
				for first time install termux, run the command

				$ termux-setup-storage
				$ cd storage/shared

				(Then change dir to the checker)
				$ cd path/to/checker
				$ pip install -r requirements.txt



			NOW IF ITS ALL OK, PLACE NOW THE CREDIT CARDS TO CHECK IN cc.txt FILE
			
			For Windows:
				You can use Notepad.exe or any text editor

			For Linux / Termux / GNU Root Debian:
				In linux, use gedit or any text editor
				In android, Use Code Editor (DroidEdit in playstore or any code editor)


			*** IF YOU USE PROXY, PLACE IT IN proxies.txt AND REPEAT STEP FOR cc.txt ***


			NOW RUN THE checker.py BY RUNNING COMMAND
			(Both Windows / android / Linux / MacOS)

			$ python checker.py

			DIRECTIONS:

				It asks for Name, zipcode, and email

				If you dont use proxy, Just ignore or type 'N' when ask "Use Proxy?[y/n] "
				.- If You use a proxy, then type "y"
            '------ if your proxy has username and password for authentication, type "y" when ask "Proxy is Authenticated?[y/n] "
                    then type the credentials. If not, then enter 'n'



-------------------  KARDER SOCIETY  -------------------





