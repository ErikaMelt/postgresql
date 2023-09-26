
## Transport Order Data Generation

**Introduction**

The transport order system involves managing orders with different statuses: 'Pending,' 'In Transit,' and 'Delivered.' Changes to these orders are recorded in the transport_order_audit table.

This README provides insights into the data generation process and explains how the provided query was enhanced to ensure more realistic and accurate data.

**Prerequisites**

Before running the query, ensure that:

- PostgreSQL installed and configured.
- A database named 'interview' has been created. 
- Transport_order_audit table is created within the 'interview' database. 


### Data Generation Logic

#### Description of the characteristics of the table transport_order_audit 

##### Table Structure 

### Table Structure

- `id` (SERIAL): Auto-incrementing integer used as the primary key.
- `order_id` (INTEGER): Represents the order identifier associated with the `id` in the `transport_order` table.
- `customer_id` (INTEGER): Stores the customer's identifier for the order.
- `origin` (VARCHAR): Contains a string representing the origin of the transport order.
- `destination` (VARCHAR): Contains a string representing the destination of the transport order.
- `transport_status` (USER-DEFINED): Indicates the current status of the transport order. The data type appears to be user-defined, possibly for custom enum values.
- `change_type` (CHAR): Represents the type of change that occurred in the order. It's a single character, either 'I' for Insert, 'U' for Update, or 'D' for Delete.
- `change_timestamp` (TIMESTAMP WITH TIME ZONE): Records the timestamp when the change occurred. It defaults to the current timestamp.
- `user_id` (INTEGER): Stores the identifier of the user associated with the change.

### Constraints

- Primary Key: The primary key constraint is defined on the `id` column, ensuring each record is uniquely identified by its `id`.

### Indexes

- `idx_transport_order_audit_order_id`: An index is created on the `order_id` column, likely to optimize queries that filter or join based on order identifiers.
- `idx_transport_order_audit_customer_id`: An index is created on the `customer_id` column, likely to optimize queries related to customer-specific data.

The `transport_order_audit` table provides a structured and efficient way to track changes and maintain a comprehensive history of transport orders and their modifications.

Referential Integrity: The order_id column establishes a relationship with the main transport_order table to maintain referential integrity.


#### Initial Data Generation

- Initial records are generated for orders with a 'Pending' status and 'I' (Insert) change type.
- Customer IDs, origins, destinations, change timestamps, and other data are generated randomly.
- A controlled percentage of orders (e.g., 10%) are updated to 'D' (Delete) change type.  The assumption is that only an order with status 'Pending' can be deleted. 
- Change timestamps are calculated based on the current timestamp for insertions and random days in the past for historical changes.

#### Subsequent Data Generation

- Subsequent data records are generated for 'Pending' orders with 'I' change type, simulating updates.
- Orders progress from 'Pending' to 'In Transit' to 'Delivered' with realistic change timestamps.
- Randomized factors add variability to the data for realism.


#### Issues identified in the Provided Query

- The initial data generation doesn't ensure that 'Pending' orders with 'I' (Insert) change type are created.

- The change type for updates and deletes is generated randomly for both initial and subsequent records, making it difficult to track the order's history accurately.

- The transport status is generated randomly without considering the order's lifecycle. This could result in illogical status transitions.

- The change timestamps are randomly generated, which can lead to unrealistic and inconsistent date values.


#### Changes Made to the Provided Query

- 'Pending' orders with 'I' change type are created initially.

- Some 'Pending' orders are updated to 'D' (Delete) with a controlled probability (e.g., 10%) and maintain 'I' (Insert) change type for the rest, which accurately represents changes.

- Control the status transitions, starting with 'Pending' and moving to 'In Transit' and 'Delivered' sequentially, ensuring a logical order.

- Generate timestamps based on the current timestamp with some random adjustments, creating more realistic and consistent date values.


