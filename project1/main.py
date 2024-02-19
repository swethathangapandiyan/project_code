from flask import Flask, redirect, url_for, render_template, request

app=Flask(__name__)

# @app.route('/')
# def index():
#     # return render_template('another_index.html', title='Welcome', content='Hai from the page')
#     return render_template('another_index.html')

# @app.route('/home')
# def home():
#     return "Hai"
#
# @app.route('/user/<name>')
# def user(name):
#     return "Haii {}".format(name)

# @app.route('/admin')
# def hai_admin():
#     return 'Haii admin'
# @app.route('/guest')
# def hai_guest():
#     return 'Haii welcome guest'
#
# @app.route('/user/<name>')
# def hello_user(name):
#     if name=='admin':
#         return redirect(url_for('hai_admin'))
#     else:
#         return redirect(url_for('hai_guest'))

@app.route('/')
def student():
    return render_template('Emp.html')

@app.route('/result',methods=['POST','GET'])
def result():
    if request.method=='POST':
        result=request.form
        return render_template('result.html',result=result)

if __name__=='__main__':
    app.run(debug=True)
