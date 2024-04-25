import os
from Controllers import ProductionController, EmployeeController, SectionController
from flask import Flask, jsonify, request, send_from_directory
import Util

app = Flask(__name__)
app.config['EmployeeImages'] = 'EmployeeImages'  # folder name


############### Production Controller
@app.route('/api/Production/AddRawMaterial', methods=['POST'])
def add_raw_material():
    response = ProductionController.add_raw_material(request.args.get('name'))
    return response


@app.route('/api/Production/UpdateRawMaterial', methods=['PUT'])
def update_raw_material():
    response = ProductionController.update_raw_material(request.get_json())
    return response


@app.route('/api/Production/GetAllRawMaterials', methods=['GET'])
def get_all_raw_materials():
    response = ProductionController.get_all_raw_materials()
    return response


@app.route('/api/Production/AddProduct', methods=['POST'])
def add_product():
    data = request.get_json()
    response = ProductionController.add_product(data)
    return response


@app.route('/api/Production/GetAllProducts', methods=['GET'])
def get_all_products():
    response = ProductionController.get_all_products()
    return response


@app.route('/api/Production/GetLinkedProducts', methods=['GET'])
def get_linked_products():
    response = ProductionController.get_linked_products()
    return response


@app.route('/api/Production/GetUnlinkedProducts', methods=['GET'])
def get_unlinked_products():
    response = ProductionController.get_unlinked_products()
    return response


@app.route('/api/Production/LinkProduct', methods=['POST'])
def link_product():
    data = request.get_json()
    response = ProductionController.link_product(data)
    return response


@app.route('/api/Production/AddStock', methods=['POST'])
def add_stock():
    data = request.get_json()
    response = ProductionController.add_stock(data)
    return response


@app.route('/api/Production/AddBatch', methods=['POST'])
def add_batch():
    data = request.get_json()
    response = ProductionController.add_batch(data)
    return response


@app.route('/api/Production/GetAllBatches', methods=['GET'])
def get_all_batches():
    product_number = request.args.get('product_number')
    response = ProductionController.get_all_batches(product_number)
    return response


@app.route('/api/Production/GetBatchDetails', methods=['GET'])
def get_batch():
    batch_number = request.args.get('batch_number')
    response = ProductionController.get_batch_details(batch_number)
    return response


@app.route('/api/Production/GetFormulaOfProduct', methods=['GET'])
def get_formula_of_product():
    product_number = request.args.get('product_number')
    response = ProductionController.get_formula_of_product(product_number)
    return response


@app.route('/api/Production/GetAllInventory', methods=['GET'])
def get_all_inventory():
    response = ProductionController.get_all_inventory()
    return response


@app.route('/api/Production/GetStockDetailOfRawMaterial', methods=['GET'])
def get_detail_of_raw_material():
    raw_material_id = request.args.get('id')
    raw_material_id = int(raw_material_id)
    response = ProductionController.get_detail_of_raw_material(raw_material_id)
    return response


@app.route('/api/Production/GetAllDefectedImages', methods=['GET'])
def get_all_defected_images():
    product_number = request.args.get('product_number')
    folder_path = f'defected_items\\{product_number}'
    response = ProductionController.get_defected_images(folder_path)
    return response


@app.route('/api/Production/GetDefectedImagesOfBatch', methods=['GET'])
def get_defected_images():
    product_number = request.args.get('product_number')
    batch_number = request.args.get('batch_number')
    folder_path = f'defected_items\\{product_number}\\{batch_number}'
    response = ProductionController.get_defected_images(folder_path)
    return response


############################SectionController#############################
@app.route('/api/Section/InsertSection', methods=['POST'])
def insert_section():
    data = request.get_json()
    response = SectionController.insert_section(data)
    return response


@app.route('/api/Section/GetAllSections', methods=['GET'])
def get_all_section():
    status = request.args.get('status')
    response = SectionController.get_all_sections(int(status))
    return response


@app.route('/api/Section/GetSectionDetail', methods=['GET'])
def get_section_detail():
    section_id = request.args.get('section_id')
    response = SectionController.get_section_detail(section_id)
    return response


@app.route('/api/Section/UpdateSection', methods=['PUT'])
def update_section():
    data = request.get_json()
    response = SectionController.update_section(data)
    return response

@app.route('/api/Section/ChangeSectionAcitivityStatus', methods=['GET'])
def change_section_activity_status():
    section_id = request.args.get('section_id')
    response = SectionController.change_section_activity_status(section_id)
    return response

@app.route('/api/Section/GetAllRule', methods=['GET'])
def get_all_rules():
    response = SectionController.get_all_rules()
    return response


#####################  Employee Controller  #################################
@app.route('/api/Employee/Login', methods=['GET'])
def login():
    response = EmployeeController.login(username=request.args.get('username'), password=request.args.get('password'))
    return response


@app.route('/api/Employee/AddEmployee', methods=['POST'])
def add_employee():
    if 'files' not in request.files:
        return jsonify({'message': 'No files part'}), 500
    files = request.files.getlist('files')
    if not files:
        return jsonify({'message': 'No files selected'}), 500
    name = request.form.get('name')
    salary = request.form.get('salary')
    username = request.form.get('username')
    password = request.form.get('password')
    job_role = request.form.get('job_role_id')
    job_type = request.form.get('job_type')
    gender = request.form.get('gender')
    section_id = request.form.get('section_id')
    data = {'name': name, 'salary': salary, 'job_role_id': job_role, 'job_type': job_type, 'gender': gender,
            'section_id': section_id, 'username': username, 'password': password, 'images': files}
    response = EmployeeController.add_employee(data)
    return response

@app.route('/api/Employee/GetAllJobRoles', methods=['GET'])
def get_all_job_roles():
    response = EmployeeController.get_all_job_roles()
    return response

@app.route('/api/Employee/GetAllSupervisors', methods=['GET'])
def get_all_supervisors():
    response = EmployeeController.get_all_supervisors()
    return response



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
