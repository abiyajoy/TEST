#404:http ststus code.page not found.500 is a internal server eror.the error page is designed or modified.




from flask import render_template
from app_package import app,db
@app.errorhandler(404)
def not_found_error(error):
    return render_template("404_error.html"),404

@app.errorhandler(500)
def internal_error(error):
    db.session.close()
    #we should close db inorder to clean up.before running
    return render_template("500_error.html"),500
    
