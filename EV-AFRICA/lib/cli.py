import click
from helpers import (
    create_vehicle, delete_vehicle, list_vehicles, find_vehicle_by_model,
    create_customer, delete_customer, list_customers, find_customer_by_email,
    create_order, delete_order, list_orders
)

@click.group()
def cli():
    """EV Market Africa CLI"""
    pass

# [Add all your CLI commands here]

if __name__ == '__main__':
    cli()