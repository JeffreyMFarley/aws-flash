# aws-flash
Study guide for AWS Certification

### Background

I created this repo to help me study for the Amazon Web Services - Solution Architect Certification.  I am not currently maintaining or updating the source code, but I will merge pull requests if you have changes

### Requirements

`python`

### Contents

|File|Contains|
|---|---|
|`Vagrantfile`|Useful if you want to run the application in a VM|
|`convert_raw.py`|Parses the `raw.txt` file into a format used by the exam|
|`exam.py`|The main module for running the exam|
|`questions.json`|The file containing the parsed and processed questions|
|`raw.txt`|A text file of all the questions I found on the internet while making this repo|

### Installation

```shell
git clone https://github.com/JeffreyMFarley/aws-flash.git
cd aws-flash
python convert_raw.py
```

### Usage
``` shell
python exam.py   # Provides a 40 question sample exam

python exam.py 10   # Provides a 10 question sample exam
```
