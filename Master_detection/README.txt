INSTALLATION
1:Open up your favorite command line workspace (cmd, powershell, Ipython console, terminal)
2(Optional):Use "pip" and "python" commands if you are unsure that you have these installed(you should have python at least)
2.5 MAKE SURE YOU HAVE 64 bit python version installed and 3.6
3:Use the "pip install pipenv" command to install pipenv
4:Navigate to the Master_detection folder and then run "pipenv install" to install dependencies and create a virtual environment for the application. IT IS CRUCIAL THAT YOU DO THIS FROM THE MASTER_DETECTION FOLDER AND NOT THE EMOTION-DETECTION FOLDER!
5:When the depencies is installed for the environment, run the "pipenv shell" command to activate it
6:Run the script of your choice from the Master_detection folder and provide the necessary arguments

RUNNING THE SCRIPTS
A copy-paste line is provided at the top of each script to just paste and run, provided you are using the original folder structure.
You can also use the "python scriptname.py -h" command to get information on arguments and provide them manually.

UNINSTALL
If you for some reason want to remove the virtual environment completely from the application,
navigate to the Master_detection folder and run the "pipenv --rm" command(you can always re-install by going back to step 4)
and then simply delete the folder.

EXTRA
The application will continue to output a window of the camera until either "q" key on keyboard is pressed or you close your terminal.
This information is also given in the "python scriptname.py -h" command info.

Enjoy!
