import os
import subprocess


def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0




def get_media(list_Drives,movie_extension):
    media_count = 0
    media_list  = []
    for rootDir in list_Drives:
        for dirName,subdirList,fileList in os.walk(rootDir):
            for fname in fileList:
                for extension in movie_extension:
                    if fname.endswith(extension):      
                        path = os.path.join(rootDir,dirName,fname)
                        stats_path = os.stat(path)
                        
                        typ = convert_bytes(stats_path.st_size)
                        a,b = typ.split()
                    
                        for s in ['MB','GB','TB']:
                            if b in s:
                                media_count += 1
                                media_list.append({'name':fname,'size':a,'in':s})        
                            else:
                                pass
                    else:
                        pass
    print(media_count)
    return media_list

    
if __name__ == '__main__':

    movie_extension = ['avi','wmv','mp4','mkv','vob']
    driveStr =  subprocess.check_output("fsutil fsinfo drives")
    driveStr = driveStr.decode("utf-8")
    list_Drives=driveStr.strip().lstrip("Drives:").split()
    media = get_media(list_Drives,movie_extension)
    print(media)
    print(len(media))

   
