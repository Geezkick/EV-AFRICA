import click
from helpers import (
    create_vehicle, delete_vehicle, list_vehicles, find_vehicle_by_model, filter_vehicles_by_price,
    create_customer, delete_customer, list_customers, find_customer_by_email,
    create_order, delete_order, list_orders, find_order_by_id, list_orders_by_customer, generate_sales_report
)

MENU_OPTIONS = (
    ("add-vehicle", "Add a new vehicle"),
    ("remove-vehicle", "Delete a vehicle"),
    ("list-vehicles", "List all vehicles"),
    ("find-vehicle", "Find vehicle by model"),
    ("filter-vehicles", "Filter vehicles by price range"),
    ("add-customer", "Add a new customer"),
    ("remove-customer", "Delete a customer"),
    ("list-customers", "List all customers"),
    ("find-customer", "Find customer by email"),
    ("add-order", "Add a new order"),
    ("remove-order", "Delete an order"),
    ("list-orders", "List all orders"),
    ("find-order", "Find order by ID"),
    ("list-customer-orders", "List orders for a customer"),
    ("sales-report", "Generate sales report")
)

@click.group()
def cli():
    """EV Market Africa CLI: Manage electric vehicle inventory and customer orders."""
    pass

@cli.command()
@click.option('--model', prompt='Vehicle model', help='Model of the electric vehicle')
@click.option('--price', prompt='Price', type=float, help='Price in USD')
@click.option('--battery_range', prompt='Battery range (km)', type=int, help='Battery range in kilometers')
@click.option('--stock_quantity', prompt='Stock quantity', type=int, help='Number of vehicles in stock')
def add_vehicle(model, price, battery_range, stock_quantity):
    """Add a new vehicle to the inventory."""
    try:
        vehicle = create_vehicle(model, price, battery_range, stock_quantity)
        click.echo(f"Vehicle added: {vehicle}")
    except Exception as e:
        click.echo(f"Error: {e}")

@cli.command()
@click.option('--id', prompt='Vehicle ID', type=int, help='ID of the vehicle to delete')
def remove_vehicle(id):
    """Delete a vehicle from the inventory."""
    if delete_vehicle(id):
        click.echo(f"Vehicle ID {id} deleted")
    else:
        click.echo(f"Vehicle ID {id} not found")

@cli.command()
def list_vehicles_cmd():
    """List all vehicles in the inventory."""
    vehicles = list_vehicles()
    if vehicles:
        for vehicle in vehicles:
            click.echo(vehicle)
    else:
        click.echo("No vehicles found")

@cli.command()
@click.option('--model', prompt='Model', help='Model to search for')
def find_vehicle(model):
    """Find a vehicle by model."""
    vehicle = find_vehicle_by_model(model)
    if vehicle:
        click.echo(vehicle)
    else:
        click.echo(f"No vehicle found with model {model}")

@cli.command()
@click.option('--min_price', prompt='Minimum price', type=float, help='Minimum price in USD')
@click.option('--max_price', prompt='Maximum price', type=float, help='Maximum price in USD')
def filter_vehicles(min_price, max_price):
    """Filter vehicles by price range."""
    vehicles = filter_vehicles_by_price(min_price, max_price)
    if vehicles:
        for vehicle in vehicles:
            click.echo(vehicle)
    else:
        click.echo(f"No vehicles found between ${min_price} and ${max_price}")

@cli.command()
@click.option('--name', prompt='Customer name', help='Name of the customer')
@click.option('--email', prompt='Customer email', help='Email of the customer')
def add_customer(name, email):
    """Add a new customer."""
    try:
        customer = create_customer(name, email)
        click.echo(f"Customer added: {customer}")
    except Exception as e:
        click.echo(f"Error: {e}")

@cli.command()
@click.option('--id', prompt='Customer ID', type=int, help='ID of the customer to delete')
def remove_customer(id):
    """Delete a customer."""
    if delete_customer(id):
        click.echo(f"Customer ID {id} deleted")
    else:
        click.echo(f"Customer ID {id} not found")

@cli.command()
def list_customers_cmd():
    """List all customers."""
    customers = list_customers()
    if customers:
        for customer in customers:
            click.echo(customer)
    else:
        click.echo("No customers found")

@cli.command()
@click.option('--email', prompt='Email', help='Email to search for')
def find_customer(email):
    """Find a customer by email."""
    customer = find_customer_by_email(email)
    if customer:
        click.echo(customer)
    else:
        click.echo(f"No customer found with email {email}")

@cli.command()
@click.option('--customer_id', prompt='Customer ID', type=int, help='ID of the customer')
@click.option('--vehicle_id', prompt='Vehicle ID', type=int, help='ID of the vehicle')
@click.option('--quantity', prompt='Quantity', type=int, help='Number of vehicles ordered')
def add_order(customer_id, vehicle_id, quantity):
    """Add a new order."""
    try:
        order = create_order(customer_id, vehicle_id, quantity)
        click.echo(f"Order added: {order}")
    except Exception as e:
        click.echo(f"Error: {e}")

@cli.command()
@click.option('--id', prompt='Order ID', type=int, help='ID of the order to delete')
def remove_order(id):
    """Delete an order."""
    if delete_order(id):
        click.echo(f"Order ID {id} deleted")
    else:
        click.echo(f"Order ID {id} not found")

@cli.command()
def list_orders_cmd():
    """List all orders."""
    orders = list_orders()
    if orders:
        for order in orders:
            click.echo(order)
    else:
        click.echo("No orders found")

@cli.command()
@click.option('--id', prompt='Order ID', type=int, help='ID of the order to find')
def find_order(id):
    """Find an order by ID."""
    order = find_order_by_id(id)
    if order:
        click.echo(order)
    else:
        click.echo(f"No order found with ID {id}")

@cli.command()
@click.option('--customer_id', prompt='Customer ID', type=int, help='ID of the customer')
def list_customer_orders(customer_id):
    """List all orders for a customer."""
    orders = list_orders_by_customer(customer_id)
    if orders:
        for order in orders:
            click.echo(order)
    else:
        click.echo(f"No orders found for customer ID {customer_id}")

@cli.command()
def sales_report():
    """Generate a sales report."""
    report = generate_sales_report()
    if report:
        click.echo("Sales Report:")
        for model, data in report.items():
            click.echo(f"Model: {model}, Total Orders: {data['total_orders']}, Total Revenue: ${data['total_revenue']:.2f}")
    else:
        click.echo("No sales data available")

if __name__ == '__main__':
    cli()