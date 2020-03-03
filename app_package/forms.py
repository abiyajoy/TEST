


from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,IntegerField,FloatField
from wtforms.validators import DataRequired,EqualTo
from app_package.model import User

class LoginForm(FlaskForm):
    username=StringField("Username: ",validators=[DataRequired()])
    password=PasswordField("Password:",validators=[DataRequired()])
    
    remember_me=BooleanField("Remember me")
    submit=SubmitField("Sign in")
   
            
            
class AddUserForm(FlaskForm):
    name=StringField("Name: ",validators=[DataRequired()])
    age=IntegerField("Age: ",validators=[DataRequired()])
    email=StringField("Email: ",validators=[DataRequired()])
    mobile=StringField("Mobile: ",validators=[DataRequired()])
    clocation=StringField("CurrentLocation: ",validators=[DataRequired()])
    accno=IntegerField("AccountNumber: ",validators=[DataRequired()])
    priority=StringField("Priority: ",validators=[DataRequired()])
    balance=FloatField("Balance: ",validators=[DataRequired()])
    submit=SubmitField("Add Account")


    
    
class DeleteUserForm(FlaskForm):
    accno=IntegerField("accno of the Employee to be deleted: ",validators=[DataRequired()])
    submit=SubmitField("Delete Confirm")
class DeleteUserFormConfirm(FlaskForm):
    accno=IntegerField("accno of the Employee to be deleted: ",validators=[DataRequired()])
    balance=FloatField("Balance: ",validators=[DataRequired()])
    submit=SubmitField("Delete Account")


class DepositMoneyForm(FlaskForm):
    id=IntegerField("Id of the Employee to be modified: ",validators=[DataRequired()])
    #accno=IntegerField("AccountNumber: ",validators=[DataRequired()])
    #balance=IntegerField("Balance: ",validators=[DataRequired()])
    credit=FloatField("credit : ",validators=[DataRequired()])
    submit=SubmitField("Money Deposited")

class WithdrawMoneyForm(FlaskForm):
    id=IntegerField("Id of the Employee to be modified: ",validators=[DataRequired()])
    #accno=IntegerField("AccountNumber: ",validators=[DataRequired()])
    #balance=IntegerField("Balance: ",validators=[DataRequired()])
    debit=FloatField("debit : ",validators=[DataRequired()])
    submit=SubmitField("Money Withdrawed")






