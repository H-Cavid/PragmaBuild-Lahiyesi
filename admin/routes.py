from flask import render_template

from app import app
@app.route("/admin/")

def a_index():
   return render_template('admin/index.html')