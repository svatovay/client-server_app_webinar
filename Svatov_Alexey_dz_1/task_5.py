import subprocess
import locale

default_encoding = locale.getpreferredencoding()
subproc_ping_yandex = subprocess.Popen(args=('ping', '-c 5', 'yandex.ru'),
                                       stdout=subprocess.PIPE,
                                       encoding=default_encoding)
subproc_ping_youtube = subprocess.Popen(args=('ping', '-c 5', 'youtube.com'),
                                        stdout=subprocess.PIPE,
                                        encoding=default_encoding)
if __name__ == '__main__':
    for line in subproc_ping_yandex.stdout:
        print(line)
    print('-'*150)
    for line in subproc_ping_youtube.stdout:
        print(line)
