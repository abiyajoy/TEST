









from flask import render_template,flash,redirect,url_for
from app_package import app,db,mongo
from app_package.forms import LoginForm,DeleteUserForm
from app_package.forms import AddUserForm,DepositMoneyForm,WithdrawMoneyForm,DeleteUserFormConfirm
#from app_package.forms import BalanceUserForm
from app_package.model import User
from flask_login import current_user,login_user,logout_user,login_required




emp_id=29
@app.route("/",methods=["GET","POST"])
def index():
    if current_user.is_authenticated:
        return redirect(url_for("menu"))
    else:
        form=LoginForm()#the details in the login form is placesd in the form
        if form.validate_on_submit():
            user=User.query.filter_by(username=form.username.data).first()
            if user is None or not user.check_password(form.password.data):
                flash("Invalid User")
                return redirect(url_for("index"))
            else:
                login_user(user,remember=form.remember_me.data)
                return redirect(url_for("menu"))
        else:
            return render_template("login.html",form=form)




@app.route("/menu")
@login_required
def menu():
    return render_template("menu.html")
   
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))
   
@app.route("/login")
def login():
    return render_template("authorized.html")
    
    
    
    
@app.route("/add_user",methods=["GET","POST"])
@login_required
def add_user():
    global emp_id
    form=AddUserForm()
    if form.validate_on_submit():
        fields=["_id","name","age","email","mobile","clocation","accno","priority","balance"]
        emp_id+=1
        values=[emp_id,form.name.data,form.age.data,form.email.data,form.mobile.data,form.clocation.data,form.accno.data,form.priority.data,form.balance.data]
        employee=dict(zip(fields,values))
        emp_col=mongo.db.employees
        tmp=emp_col.insert_one(employee)
        if tmp.inserted_id==emp_id:
            flash("User added")
            return redirect(url_for("menu"))
        else:
            flash("problem adding user")
            return redirect(url_for("logout"))
    else:
        return render_template("add_user.html",form=form)
            
    
@app.route("/display_users")    
@login_required
def display_users():
    emp_col=mongo.db.employees
    users=emp_col.find()
    return render_template("display_users.html",users=users)   
    
@app.route("/delete_user", methods=["GET","POST"])
@login_required
def delete_user():
    form=DeleteUserForm()
    if form.validate_on_submit():
        emp_col=mongo.db.employees
        query={"accno":form.accno.data}
        #emp_col.delete_one(query)
        flash("Confirm Employee to be deleted")
        cust1=emp_col.find(query)
        
        return redirect(url_for("delete_confirm_user",cust1=cust1,form=form))
    else:
        return render_template("delete_user.html",form=form)    
        
@app.route("/delete_confirm_user", methods=["GET","POST"])
@login_required
def delete_confirm_user():
    form=DeleteUserFormConfirm()
    if form.validate_on_submit():
        emp_col=mongo.db.employees
        query={"accno":form.accno.data}
        emp_col.delete_one(query)
        flash("Employee deleted")
        
        
        return redirect(url_for("menu.html",form=form))
    else:
        return render_template("delete_user.html",form=form)    
                
        
@app.route("/deposit_money", methods=["GET","POST"])
@login_required
def deposit_money():   
    form=DepositMoneyForm()
    if form.validate_on_submit(): 
       
        emp_col=mongo.db.employees
        query={"_id":form.id.data}
       
        cust=emp_col.find_one(query)
        bal=cust["balance"]
        new_balance=bal+form.credit.data
     
        new_data={"$set":{"balance":new_balance}}
        
        emp_col.update_one(query,new_data)
        flash("Money Deposited")
        return redirect(url_for("menu"))
    else:
        return render_template("deposit_money.html",form=form)        
        
@app.route("/withdraw_money", methods=["GET","POST"])
@login_required
def withdraw_money():   
    form=WithdrawMoneyForm()
    if form.validate_on_submit(): 
        emp_col=mongo.db.employees
        query={"_id":form.id.data}
       
        cust=emp_col.find_one(query)
        bal=cust["balance"]
        types=cust["priority"]
        new_balance=bal-form.debit.data
        if types=="priority" and new_balance<50000 or types=="ordinary" and new_balance<10000:
           flash("upon withdrawal min balance is not maintained")
           return redirect(url_for("menu"))
        else:

           new_data={"$set":{"balance":new_balance}}
           emp_col.update_one(query,new_data)
           flash("Money Withdrawed")
           return redirect(url_for("menu"))
    else:
        return render_template("withdraw_money.html",form=form)    
        
        


'''    

@app.route("/balance_money",methods=["GET","POST"])    
@login_required
def balance_money():
    form=BalanceUserForm()
    if form.validate_on_submit():
        emp_col=mongo.db.employees
        query={"accno":form.accno.data}
        users=emp_col.find(query)
        return render_template("balance_money.html",users=users)       
    
    
    '''
    
    
    
    
    
    
    
    
