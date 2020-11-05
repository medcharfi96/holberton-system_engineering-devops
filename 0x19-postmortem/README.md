# Postmortem for web stack debugging

## Sumary
----------
September 11th, 2018 server began to spit out 500 error on the web. By checking the server status on the docker container there was an Apache server configuration file that has a typo.
- Timeline
___________

    - 08:15 - 500 error showing in server
    - 08:17 - Check status of server and shows its OK
    - 08:20 - Used strace to find issue by connecting Child process for Apache
    - 08:30 - Found issue in the wp-settings.php showing that file missing
    - 08:32 - Found file being misspelled in the settings file .php
    - 08:34 - Fixed file by changing the typo to .php
    - 08:35 - Restarte Apache
    - 08:36 - Server now running normally

## Root Cause and Resolution
------------------------

The main cause was a typographical error, because in one or more of the configuration files, a file with a wrong extension was requested; that is, instead of losing a php file, a file with a .phpp extension was requested.

The correction of the typographical error is made and by means of a puppet manifest the task is automated and the solution is given greater scalability in the server farm to guarantee high availability of the service.

## Corrective and Preventative Measures
---------------------------------
To avoid this type of case, it is necessary to standardize the testing phase, as it is too counterproductive for the company for the development team to implement changes in production without being tested.
