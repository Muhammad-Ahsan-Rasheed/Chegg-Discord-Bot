# Chegg-Discord-Bot
As Chegg is one of the most emerging platform for student help so the purpose of this project is to Automate the process of providing solution. From receiving assignment link to providing file this all will be done by Bot. The benefit of this Project is now many people can use Chegg account as Chegg limit to only 2 Devices.  

This is the first version and has some issues:

1- There is not limit to number of Requests which can lead to Account Suspension.

Following things you must have:

1- Discord Bot Token

2- Active Chegg Account

### Installation Process
- Create An Virtual Environment after cloning this git repo
```python3
python -m venv venv
```
- Activate the Virtual Environment
```python3
#for linux or mac os
source venv/bin/activate

#for windows cmd
.\venv\\Scripts\\activate.bat

#for windows powershell
.\venv\\Scripts\\activate.ps1

#for bash shell of windows like git bash
source venv/Scripts/activate
```

- Install Dependecies With
```python3
pip3 install -r requirements.txt
```

- Setup the Env Variables in setting.json and Run
```bash
python main.py
```
