### Upwork project

This project is a part of the Upwork project. It is a simple, single script that is used to download all the content from the public Instagram page. If download is completed it checks only for the newest changes and downloads them.

Content is saved into a folder with change logs.

### How to install

```bash
git clone <repository_url>
```

#### For windows
```bash
python -m venv env # Create virtual environment (recommended)
. env/Scripts/activate # Activate virtual environment (if created)
pip install -r requirements.txt
```

#### For linux
```bash
python3 -m venv env # Create virtual environment (recommended)
. env/bin/activate # Activate virtual environment (if created)
pip3 install -r requirements.txt
```

### Run the script

#### For windows

```bash
. env/Scripts/activate # Activate virtual environment (if created)
python main.py
```

#### For linux

```bash
. env/bin/activate # Activate virtual environment (if created)
python3 main.py
```

```bash
(env) saba@saba:~/Desktop/instadown$ python3 -u "/home/saba/Desktop/instadown/app.py"
Enter Instagram username: test_account
```


### Example

Downloading [**instagram**](https://www.instagram.com/instagram/) account content

```bash
(env) saba@saba:~/Desktop/instadown$ python3 -u "/home/saba/Desktop/instadown/app.py"
Enter Instagram username: instagram
Stored ID 25025320 for profile instagram.
instagram/2022-05-16_16-00-20_UTC_profile_pic.jpg 
Retrieving posts from profile instagram.
[   1/7558] instagram/2023-12-14_17-01-35_UTC.jpg [Skills 🌪️ ⁣  ⁣ #InTheMoment ⁣…] instagram/2023-12-14_17-01-35_UTC.mp4 json 
[   2/7558] instagram/2023-12-12_17-00-23_UTC.jpg [Shine on, you crazy disco blo…] instagram/2023-12-12_17-00-23_UTC.mp4 json 
[   3/7558] instagram/2023-12-11_17-00-55_UTC_1.jpg instagram/2023-12-11_17-00-55_UTC_2.jpg [“My main goal is to inspire o…] json 
[   4/7558] instagram/2023-12-09_19-36-34_UTC.jpg [Where there’s basketball, the…] instagram/2023-12-09_19-36-34_UTC.mp4 ^C
Saved resume information to instagram/iterator_ICRKNOZh.json.xz.
...
```

Result:

```bash
(env) saba@saba:~/Desktop/instadown$ tree -L 2
.
├── app.py
├── env
│   ├── bin
│   ├── include
│   ├── lib
│   ├── lib64 -> lib
│   └── pyvenv.cfg
├── instagram
│   ├── 2022-05-16_16-00-20_UTC_profile_pic.jpg
│   ├── 2023-12-09_19-36-34_UTC.jpg
│   ├── 2023-12-09_19-36-34_UTC.mp4.temp
│   ├── 2023-12-09_19-36-34_UTC.txt
│   ├── 2023-12-11_17-00-55_UTC_1.jpg
│   ├── 2023-12-11_17-00-55_UTC_2.jpg
│   ├── 2023-12-11_17-00-55_UTC.json.xz
│   ├── 2023-12-11_17-00-55_UTC.txt
│   ├── 2023-12-12_17-00-23_UTC.jpg
│   ├── 2023-12-12_17-00-23_UTC.json.xz
│   ├── 2023-12-12_17-00-23_UTC.mp4
│   ├── 2023-12-12_17-00-23_UTC.txt
│   ├── 2023-12-14_17-01-35_UTC.jpg
│   ├── 2023-12-14_17-01-35_UTC.json.xz
│   ├── 2023-12-14_17-01-35_UTC.mp4
│   ├── 2023-12-14_17-01-35_UTC.txt
│   ├── id
│   ├── instagram_25025320.json.xz
│   └── iterator_ICRKNOZh.json.xz
├── instagram_content
├── README.md
└── requirements.txt
```