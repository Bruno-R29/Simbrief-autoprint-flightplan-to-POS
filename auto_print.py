import os
import time
import win32print
import win32ui
import win32con

folder_to_monitor = r"C:\Temp"  ###### Replace with the path of simbrief download path, or create folder in C: called Temp, setting simbrief autodownload to that specific folder

def print_to_printer(content):
    try:
        
        printer_name = win32print.GetDefaultPrinter()   ### default printer change if needed
        print(f"Printing to: {printer_name}")

        printer_dc = win32ui.CreateDC()
        printer_dc.CreatePrinterDC(printer_name)

        printer_dc.StartDoc("Print Job")  
        printer_dc.StartPage()  

        font = win32ui.CreateFont({
            "name": "Arial",
            "height": 26,  ###  increase or dec font size
        })
        printer_dc.SelectObject(font)

        y_position = 100  ### Y

        lines = content.split('\n')
        for line in lines:
            if '[OFP]' in line:
                print("Found '[OFP]', stopping print.") ###! stop print after 
                break  
            printer_dc.TextOut(100, y_position, line)  
            y_position += 25  ### spacing

        printer_dc.EndPage()  
        printer_dc.EndDoc()  
        printer_dc.DeleteDC()
    except Exception as e:
        print(f"Error during printing: {e}") ## *

def check_new_files():
    known_files = set(os.listdir(folder_to_monitor))  ###3 continuuos print, meaning the script continues scanning the folder for new files 
    print(f"Monitoring folder: {folder_to_monitor}")
    print(f"Initial files: {known_files}")

    while True:
        try:
            time.sleep(2)  ### wait in sec
            current_files = set(os.listdir(folder_to_monitor))
            new_files = current_files - known_files  

            for new_file in new_files:
                file_path = os.path.join(folder_to_monitor, new_file)
                print(f"New file detected: {file_path}")
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()

                    if content:
                        print("Content read successfully, sending to printer...")
                        print_to_printer(content)  
                    else:
                        print("The file is empty.")
                except PermissionError as e:
                    print(f"PermissionError: {e} - Unable to access the file.")
                except Exception as e:
                    print(f"Error: {e}")

                known_files.add(new_file)

        except KeyboardInterrupt:
            print("Monitoring stopped by user.")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    if not os.path.exists(folder_to_monitor):
        print(f"Error: The folder '{folder_to_monitor}' does not exist.")
    else:
        check_new_files()
