# Google winter of code,GDSC,SVNIT
## Team Name: Pheonix
## Team members: Jay Kadel, Akash singh, Gaurav Singh, Biren Gami
# Project Description
### Adworks is website for Advertisement Needs. Adworks Helps Brands Establish And Enhance Their Social Media Presence. This website contains home page,our services page,About Us page and contact Us page. It is a complete Responsive Websites.
Website is made using python so you will require [python](https://www.python.org/downloads/) on your device.

## Libraries required to be installed are: virtualenv, pymongo and flask
## After cloning the repo you will have to open vscode with vscode here in the cloned folder and install the given libraries.
### commands for installation of this libraries are given below:
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar. 

```bash
pip install virtualenv
```
## After installing virtualenv you will need to setup virtual environment with the help of the following steps:
1.run the following code in the terminal in VS code
```bash
virtualenv env
```
2.activate the virtual environment
```bash
.\env\Scripts\activate.ps1 
```
3.after this you can install the following libraries
```bash
pip install pymongo
```
```bash
pip install flask
```

## You can run the website by running the instruction in terminal in VS code
```bash
python .\app.py
```
### You will need to add your email in line number 19 of app.py file in 'email_receiver' variable in order to receive the emails from contact us form to your account
