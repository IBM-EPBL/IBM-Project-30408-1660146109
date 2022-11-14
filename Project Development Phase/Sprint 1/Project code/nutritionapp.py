# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 19:40:29 2022

@author: admin
"""

from flask import Flask,render_template,request,url_for,redirect
import ibm_db
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import requests



app=Flask(__name__)

@app.route("/")
def home():
    return render_template('Home.html')

@app.route("/reg")
def reg():
    return render_template('Registration.html')

@app.route("/register",methods=["POST","GET"])
def register():
     if request.method == 'POST' :
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        global email
        email = request.form['email']
        phoneNumber = request.form['phoneNumber']
        password = request.form['password']
        message = Mail(from_email='nutriaux04@gmail.com',to_emails=email,subject="NutriAux - Registration",html_content='<b>NutriAux welocmes you</b><br/><p>Your account has been registered successfully</p>')
        try:
            sg=SendGridAPIClient('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')
            response=sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)
        return redirect(url_for('personaldetails'))
    



@app.route("/personaldetails")
def personaldetails():
    return render_template("personaldetails.html")

@app.route("/addpersonaldetails",methods=["POST","GET"])
def addpersonaldetails():
    if request.method == 'POST' :
        age=float(request.form.get('age'))
        gender=request.form.get('Gender')
        weight=float(request.form.get('weight'))
        height=float(request.form.get('height'))
        activity=request.form.get('activity')
        print(age,gender,weight,height,activity)
        if(gender == 'male'and activity == "1"):
            totalCalories = 1.2 * (66.5 + (13.75 * weight) + (5.003 * height) - (6.755 * age))
        elif(gender == 'male' and activity == "2"):
            totalCalories = 1.375 * (66.5 + (13.75 * weight) + (5.003 * height) - (6.755 * age))
        elif (gender == 'male' and activity == "3"):
            totalCalories = 1.55 * (66.5 + (13.75 * weight) + (5.003 * height) - (6.755 * age))
        elif(gender == 'male' and activity == "4"):
            totalCalories = 1.725 * (66.5 + (13.75 * weight) + (5.003 * height) - (6.755 * age))
        elif(gender == 'male' and activity == "5"): 
            totalCalories = 1.9 * (66.5 + (13.75 * weight) + (5.003 * height) - (6.755 * age))
        elif(gender == 'female' and activity == "1"):
            totalCalories = 1.2 * (655 + (9.563 * weight) + (1.850 * height) - (4.676 * age))
        elif(gender == 'female' and activity == "2"):
            totalCalories = 1.375 * (655 + (9.563 * weight) + (1.850 * height) - (4.676 * age))
        elif(gender == 'female' and activity == "3"):
            totalCalories = 1.55 * (655 + (9.563 * weight) + (1.850 * height) - (4.676 * age))
        elif(gender == 'female' and activity == "4"):
            totalCalories = 1.725* (655 + (9.563 * weight) + (1.850 * height) - (4.676 * age))
        else: 
            totalCalories = 1.9 * (655 + (9.563 * weight) + (1.850 * height) - (4.676 * age))
        print(int(totalCalories))
        BMI = (weight / (height/100)**2 )
        if BMI <= 18.5:  
            BMI_message="underweight"  
        elif BMI <= 24.9:  
            BMI_message="healthy"  
        elif BMI <= 29.9:  
            BMI_message="overweight"
        else:
            BMI_message="obese"   
        print(BMI)
    return redirect(url_for('login'))


@app.route("/login")
def login():
    return render_template("login.html",message="")

@app.route("/verify",methods=["POST","GET"])
def verify():
    email = request.form.get("email")
    password = request.form.get("password")
    return render_template("login.html",message="")


if __name__ == '__main__':
    app.run(debug=True)
