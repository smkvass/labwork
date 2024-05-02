import psycopg2
from config import host, user,port, password, db_name
import pandas as pd
table_name, limit, offset = 'users2', 2, 0


def query_data_with_pagination(table_name, limit, offset):
    # Connect to the database
    connection = psycopg2.connect(
        host=host,
        user=user,
        port=port,
        password=password,
        database=db_name
    )
    
    # Execute the query with pagination parameters
    cursor = connection.cursor()
    query = f"SELECT * FROM {table_name} LIMIT {limit} OFFSET {offset}"
    cursor.execute(query)
    rows = cursor.fetchall()
    
    # Create a DataFrame from the query result
    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(rows, columns=columns)
    
    # Export the DataFrame to an Excel file
    file_name = f"{table_name}_{offset}_{limit}.xlsx"
    df.to_excel(file_name, index=False)
    
    # Close the cursor and database connection
    cursor.close()
    connection.close()
    
    # Return the DataFrame
    return df