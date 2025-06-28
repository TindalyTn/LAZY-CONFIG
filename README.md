This Python script is used to scan websites for sensitive configuration files like .env or wp-config.php. It tries to access these files and checks if they contain keywords such as "DB_HOST".
If found, it saves the URL in a file.
This type of script can be used in ethical hacking or malicious attacks to find exposed credentials or database info.
Use : python config.py targets.txt 
