cat << EOF > lib/helpers.py
from models import Vehicle, Customer, Order, Session

def create_vehicle(model, price, battery_range, stock_quantity):
    return Vehicle.create(model, price, battery_range, stock_quantity)

def delete_vehicle(id):
    return Vehicle.delete(id)

def list_vehicles():
    return Vehicle.get_all()

def find_vehicle_by_model(model):
    return Vehicle.find_by_model(model)

def filter_vehicles_by_price(min_price, max_price):
    return Vehicle.filter_by_price(min_price, max_price)

def create_customer(name, email):
    return Customer.create(name, email)

def delete_customer(id):
    return Customer.delete(id)

def list_customers():
    return Customer.get_all()

def find_customer_by_email(email):
    return Customer.find_by_email(email)

def create_order(customer_id, vehicle_id, quantity):
    return Order.create(customer_id, vehicle_id, quantity)

def delete_order(id):
    return Order.delete(id)

def list_orders():
    return Order.get_all()

def find_order_by_id(id):
    return Order.find_by_id(id)

def list_orders_by_customer(customer_id):
    return Order.get_by_customer(customer_id)

def generate_sales_report():
    session = Session()
    try:
        orders = session.query(Order).all()
        if not orders:
            return {}
        report = {}
        for order in orders:
            vehicle = session.query(Vehicle).get(order.vehicle_id)
            if vehicle:
                model = vehicle.model
                revenue = vehicle.price * order.quantity
                if model not in report:
                    report[model] = {"total_orders": 0, "total_revenue": 0.0}
                report[model]["total_orders"] += order.quantity
                report[model]["total_revenue"] += revenue
        return report
    finally:
        session.close()
EOF
