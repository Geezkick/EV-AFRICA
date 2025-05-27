cat << EOF > README.md
# EV Africa

EV Africa is a command-line interface (CLI) application designed to manage an electric vehicle (EV) dealership in African markets. It enables dealership managers to efficiently handle vehicle inventory, customer information, and orders, leveraging a SQLite database with SQLAlchemy for object-relational mapping (ORM) and Click for a user-friendly CLI. The application supports advanced features like price-based vehicle filtering and sales reporting, tailored to address real-world challenges in EV sales, such as stock management and customer tracking in regions with growing EV adoption.

## Installation

1. Clone the repository:
   \`\`\`bash
   git clone <your-repo-url>
   cd ev_market_africa
   \`\`\`

2. Install dependencies using Pipenv:
   \`\`\`bash
   pipenv install
   pipenv shell
   \`\`\`

3. Create the database:
   \`\`\`bash
   python lib/debug.py
   \`\`\`

4. Run the CLI:
   \`\`\`bash
   python lib/cli.py
   \`\`\`

## Usage

The CLI offers a comprehensive set of commands to manage vehicles, customers, and orders. Run \`python lib/cli.py --help\` to view all commands. Example commands:
- Add a vehicle: \`python lib/cli.py add-vehicle\`
- List all vehicles: \`python lib/cli.py list-vehicles\`
- Filter vehicles by price: \`python lib/cli.py filter-vehicles\`
- Add a customer: \`python lib/cli.py add-customer\`
- Create an order: \`python lib/cli.py add-order\`
- View orders for a customer: \`python lib/cli.py list-customer-orders\`
- Generate a sales report: \`python lib/cli.py sales-report\`

## Files

- **lib/cli.py**: Implements the CLI using Click, providing commands for CRUD operations, price filtering, and sales reporting. It handles user input and displays informative feedback.
- **lib/helpers.py**: Contains helper functions that bridge the CLI and ORM models, implementing business logic like stock updates and sales reporting using lists and dictionaries.
- **lib/models/__init__.py**: Configures the SQLite database connection and imports model classes for seamless ORM integration.
- **lib/models/vehicle.py**: Defines the \`Vehicle\` class with attributes (model, price, battery_range, stock_quantity) and ORM methods for CRUD operations, with property-based validation.
- **lib/models/customer.py**: Defines the \`Customer\` class with attributes (name, email) and ORM methods, linked to orders via a one-to-many relationship.
- **lib/models/order.py**: Defines the \`Order\` class with attributes (customer_id, vehicle_id, order_date, quantity) and ORM methods, managing stock updates and relationships.
- **lib/debug.py**: Initializes the database tables using SQLAlchemy.

## Data Model

- **Vehicle**: Represents an electric vehicle (e.g., model: "Tesla Model Y", price: 50000, battery_range: 500, stock_quantity: 10). Stored in the \`vehicles\` table.
- **Customer**: Represents a customer (e.g., name: "John Doe", email: "john@example.com"). Stored in the \`customers\` table.
- **Order**: Links a customer to a vehicle order (e.g., customer_id: 1, vehicle_id: 1, order_date: "2025-05-27", quantity: 2). Stored in the \`orders\` table.
- **Relationships**:
  - One \`Customer\` can have many \`Order\`s (one-to-many).
  - One \`Vehicle\` can be part of many \`Order\`s (one-to-many).

## Dependencies

- \`sqlalchemy\`: Handles ORM and database interactions, mapping Python objects to SQLite tables.
- \`click\`: Provides a user-friendly CLI interface with command options and prompts.

## Advanced Features

- **Price Filtering**: Filter vehicles by a price range to help users find affordable EVs.
- **Sales Report**: Generates a dictionary-based report of total orders and revenue per vehicle model.
- **Stock Management**: Automatically updates vehicle stock when orders are created or deleted, with validation to prevent overselling.
- **Input Validation**: Robust error handling ensures invalid inputs (e.g., negative prices, invalid emails) are caught with clear messages.

## Notes

- The application is designed for African markets, emphasizing battery range and stock management to address infrastructure and supply chain challenges.
- Code follows OOP best practices, with separation of concerns (UI, data persistence, business logic), modular design, and clear naming conventions.
- Lists are used for query results, dictionaries for sales reports, and tuples for menu options, demonstrating proficiency with Python data structures.
- The project is thoroughly tested for valid and invalid inputs to ensure robustness.