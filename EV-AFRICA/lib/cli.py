import click
from helpers import *
from datetime import datetime
from tabulate import tabulate

@click.group()
@click.version_option("1.0.0")
def cli():
    """EV Market Africa - Command Line Interface"""
    pass

@cli.command()
@click.option('--model', prompt=True, help="Vehicle model name")
@click.option('--price', type=float, prompt=True, help="Price in USD")
@click.option('--range', 'battery_range', type=int, prompt=True, help="Battery range in km")
@click.option('--stock', type=int, prompt=True, help="Initial stock quantity")
def add_vehicle(model, price, battery_range, stock):
    """Add a new vehicle to inventory"""
    try:
        result = create_vehicle(model, price, battery_range, stock)
        click.echo(f"✅ Added: {result['model']} (ID: {result['id']})")
    except Exception as e:
        click.echo(f"❌ Error: {str(e)}", err=True)

# ... [Implement all other CLI commands with proper error handling] ...

@cli.command()
def sales_report():
    """Generate comprehensive sales report"""
    try:
        report = generate_sales_report()
        
        click.echo("\n📊 SALES REPORT")
        click.echo(f"Total Sales: {report['total_sales']} units")
        click.echo(f"Total Revenue: ${report['total_revenue']:,.2f}\n")
        
        click.echo("📈 By Model:")
        click.echo(tabulate(
            [(m, d['units_sold'], f"${d['revenue']:,.2f}") 
             for m, d in report['by_model'].items()],
            headers=["Model", "Units Sold", "Revenue"],
            tablefmt="pretty"
        ))
        
        click.echo("\n👥 By Customer:")
        click.echo(tabulate(
            [(c, d['orders'], f"${d['total_spent']:,.2f}") 
             for c, d in report['by_customer'].items()],
            headers=["Customer", "Orders", "Total Spent"],
            tablefmt="pretty"
        ))
    except Exception as e:
        click.echo(f"❌ Error generating report: {str(e)}", err=True)

if __name__ == '__main__':
    cli()