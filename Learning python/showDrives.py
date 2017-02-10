import os
import subprocess
from _thread  import start_new_thread,allocate_lock
from threading import Thread

#lock = allocate_lock()
media_count = 0
media_list = []

def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
    #for x in ['KB', 'MB', 'GB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0




def get_media(rootDir,movie_extension):
    global media_count,media_list
    for dirName, subdirList, fileList in os.walk(rootDir):
        for fname in fileList:
            for extension in movie_extension:
                if fname.endswith(extension):
                    path = os.path.join(rootDir, dirName, fname)
                    stats_path = os.stat(path)
                    typ = convert_bytes(stats_path.st_size)
                    a,b = typ.split()
                    
                    for s in ['MB', 'GB', 'TB']:
                        if b in s:
                            #lock.acquire()
                            media_count += 1
                            media_list.append({'name': fname, 'size': a, 'in': s})
                            #lock.release()
                        else:
                            pass
                else:
                    pass

    #print(media_list,media_count)
    
if __name__ == '__main__':
    movie_extension = ['avi', 'wmv', 'mp4', 'mkv', 'vob']
    driveStr =  subprocess.check_output("fsutil fsinfo drives")
    driveStr = driveStr.decode("utf-8")
    list_Drives=driveStr.strip().lstrip("Drives:").split()
    threads = []
        
    for drive in list_Drives:
        thread = Thread(target = get_media,args=(drive,movie_extension))
        threads.append(thread)
        thread.start()
        print(thread)
    

    for thread in threads:
        thread.join()

        
    print(media_list)
    print(media_count)
