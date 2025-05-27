from contextlib import contextmanager
from models import Session, Vehicle, Customer, Order

@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        Session.remove()

def create_vehicle(model, price, battery_range, stock_quantity):
    with session_scope() as session:
        vehicle = Vehicle(
            model=model,
            price=price,
            battery_range=battery_range,
            stock_quantity=stock_quantity
        )
        session.add(vehicle)
        return vehicle.to_dict()

# ... [Implement all other helper functions with proper session handling] ...

def generate_sales_report():
    with session_scope() as session:
        report = {
            'total_sales': 0,
            'total_revenue': 0.0,
            'by_model': {},
            'by_customer': {}
        }
        
        # Aggregate data
        orders = session.query(Order).all()
        for order in orders:
            # Update model stats
            model_name = order.vehicle.model
            if model_name not in report['by_model']:
                report['by_model'][model_name] = {
                    'units_sold': 0,
                    'revenue': 0.0
                }
            report['by_model'][model_name]['units_sold'] += order.quantity
            report['by_model'][model_name]['revenue'] += order.calculate_total()
            
            # Update customer stats
            customer_name = order.customer.name
            if customer_name not in report['by_customer']:
                report['by_customer'][customer_name] = {
                    'orders': 0,
                    'total_spent': 0.0
                }
            report['by_customer'][customer_name]['orders'] += 1
            report['by_customer'][customer_name]['total_spent'] += order.calculate_total()
            
            # Update totals
            report['total_sales'] += order.quantity
            report['total_revenue'] += order.calculate_total()
        
        return report