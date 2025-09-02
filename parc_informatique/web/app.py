from flask import Flask, render_template, request, redirect, url_for
from database.init_db import init_db
from Models.models import (
    add_employee, list_employees, delete_employee, modify_employee_department as modify_employee,
    add_device, list_devices, delete_device,
    add_maintenance, list_maintenance_by_device
)

app = Flask(__name__)
init_db()

@app.route("/")
def index():
    return redirect(url_for("employees"))

@app.route("/employees", methods=["GET", "POST"])
def employees():
    if request.method == "POST":
        emp_id = request.form["id"]
        name = request.form["name"]
        dept = request.form["department"]
        add_employee(emp_id, name, dept)
        return redirect(url_for("employees"))
    emps = list_employees(return_data=True)
    return render_template("employees.html", employees=emps)

@app.route("/employees/delete/<int:emp_id>")
def delete_emp(emp_id):
    delete_employee(emp_id)
    return redirect(url_for("employees"))

@app.route("/employees/modify/<int:emp_id>", methods=["POST"])
def modify_emp(emp_id):
    dept = request.form["department"]
    modify_employee(emp_id, dept)
    return redirect(url_for("employees"))

@app.route("/devices", methods=["GET", "POST"])
def devices():
    if request.method == "POST":
        dtype = request.form["dtype"]
        brand = request.form["brand"]
        serial = request.form["serial"]
        emp_id = request.form["employee_id"]
        add_device(dtype, brand, serial, int(emp_id) if emp_id else None)
        return redirect(url_for("devices"))
    devs = list_devices(return_data=True)
    return render_template("devices.html", devices=devs)

@app.route("/devices/delete/<int:dev_id>")
def delete_dev(dev_id):
    delete_device(dev_id)
    return redirect(url_for("devices"))

@app.route("/maintenance")
def maintenance():
    devices = list_devices(return_data=True)
    return render_template("maintenance.html", devices=devices)

@app.route("/maintenance/add", methods=["POST"])
def add_maintenance_route():
    device_id = request.form["device_id"]
    date = request.form["date"]
    desc = request.form["description"]
    add_maintenance(device_id, date, desc)
    return redirect(url_for("maintenance"))

@app.route("/maintenance/<int:device_id>")
def maintenance_by_device(device_id):
    maints = list_maintenance_by_device(device_id, return_data=True)
    return render_template("maintenance_by_device.html", maints=maints, device_id=device_id)

if __name__ == "__main__":
    app.run(debug=True)
