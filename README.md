# APPLICATION FOR TELKOM TEST

Aplikasi ini berbasis CLI yang berfungsi untuk mengambil file log dari system linux pada folder yang diinginkan. 

## Cara setting project 
1. Git clone project ini.
2. Kemudian setup python interpreter dengan menginstall requirements.txt
3. Sesuaikan isi file .env dengan directory default yang diinginkan.
4. 



## Contoh penggunaan:
- Mengkonversi menjadi file json\
$ python3 main.py [ DIR_FILE_LOGS ] -t json


- Mengkonversi menjadi file text\
$ python3 main.py [ DIR_FILE_LOGS ] -t text


- Mengkonversi menjadi file json dengan file output pada custom directory\
$ python3 main.py [ DIR_FILE_LOGS ] -t json -o [ DIR_FILE_TUJUAN ]


- Mengkonversi menjadi file text dengan file output pada custom directory\
$ python3 main.py [ DIR_FILE_LOGS ] -t text -o [ DIR_FILE_TUJUAN ]


- Munculkan Help\
$ python3 main.py -h