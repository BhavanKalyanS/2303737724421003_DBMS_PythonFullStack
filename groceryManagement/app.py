from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Vishak46?'
app.config['MYSQL_DB'] = 'grocery_db'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inventory')
def inventory():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM inventory")  
    records = cur.fetchall()
    cur.close()
    return render_template('inventory.html', records=records)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        item_name = request.form['item_name']
        category = request.form['category']
        quantity = int(request.form['quantity'])
        unit_price = float(request.form['unit_price'])
        supplier_name = request.form['supplier_name']
        entry_time = datetime.now()

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO inventory (item_name, category, quantity, unit_price, supplier_name,entry_time ) "
            "VALUES (%s, %s, %s, %s, %s, %s)",
            (item_name, category, quantity, unit_price, supplier_name, entry_time),
        )
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('inventory'))
    return render_template('add_item.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_item(id):
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        item_name = request.form['item_name']
        category = request.form['category']
        quantity = int(request.form['quantity'])
        unit_price = float(request.form['unit_price'])
        supplier_name = request.form['supplier_name']
        entry_time = datetime.now()

        cur.execute(
            "UPDATE inventory SET item_name=%s, category=%s, quantity=%s, unit_price=%s, "
            "supplier_name=%s, entry_time=%s WHERE id=%s",
            (item_name, category, quantity, unit_price, supplier_name, entry_time, id),
        )
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('inventory'))
    
    cur.execute("SELECT * FROM inventory WHERE id=%s", (id,))
    record = cur.fetchone()
    cur.close()
    return render_template('update_item.html', record=record)

@app.route('/delete/<int:id>', methods=['GET'])
def delete_item(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM inventory WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('inventory'))

if __name__ == '__main__':
    app.run(debug=True)
