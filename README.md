# Simbrief-autoprint-flightplan-to-POS
A python script that continuously monitors a folder and automatically prints new flight plan files to your default windows printer. 



Using SIMBREIF DOWNLOADER as soon as you generate the flight on simbrief it automatically prints the flight plan to the default printer, specially configured for POS printers, simbrief downloader settings for unatended auto download bellow.



By default the script stops printing when it encounters the marker [OFP] in the text, so it doesn´t print unnecessary information wasting paper. It can be customized to stop wherever you want by editing said marker.



Edit the script and change:

folder_to_monitor = r"C:\Temp" to your desired folder or just create a folder called Temp in your C:\ directory
other settings can be edited such as font size, spacing, print stop position, and sleep time

It uses Leonardo MD80 ACARS format within simbrief downloader



Requirements
os	
time	
pywin32 win32print win32printing pypiwin32



Examples of the flightplan layout and further instructions:

Flightplan layout:
                                       
                                          



<img width="464" height="590" alt="github" src="https://github.com/user-attachments/assets/8cd5fa02-df24-4ccc-8683-e8b8ac344bbd" />

![d9e490](https://github.com/user-attachments/assets/c457a3c1-f808-43a6-9863-d6537df39c63)

Recommended settings simbrief downloader:






<img width="639" height="601" alt="Screenshot_1" src="https://github.com/user-attachments/assets/2e8123e8-e3ed-49e2-9b1f-6973338bccef" />


<img width="924" height="253" alt="Screenshot_2" src="https://github.com/user-attachments/assets/e8ef2c7d-0bd0-4468-8244-e54a0e246318" />

<img width="924" height="253" alt="Screenshot_2" src="https://github.com/user-attachments/assets/3282f9e7-a814-4a63-968e-9db4545ab4b1" />


Terminal output

<img width="956" height="228" alt="Screenshot_3" src="https://github.com/user-attachments/assets/88fbdfe4-2d31-408e-9e76-c3ea2bc58da3" />
