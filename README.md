

This project includes a Python program that reads data from `orders.csv` and performs the following tasks:
1. Computes the total revenue generated by the online store for each month in the dataset.
2. Computes the total revenue generated by each product in the dataset.
3. Computes the total revenue generated by each customer in the dataset.
4. Identifies the top 10 customers by revenue generated.

Additionally, the project includes tests for the code and is Dockerized to run the application and tests in separate services.


## Getting Started

### Clone the Repository

git clone https://github.com/shivaKhanduri/task
cd task


run docker commands

    docker-compose build
   
    docker-compose up

## Files and Structure

1. analysis.py: The main Flask application file.
2. orders.csv: The CSV file containing the order data.
3. Dockerfile: Dockerfile to build the application container.
4. Dockerfile.test: Dockerfile to build the test container.
5. docker-compose.yml: Docker Compose configuration file.
6. test_analysis.py: Python script containing unit tests for the analysis functions.


## Running the Application

1. To run the application using Docker Compose, execute the following command:

    docker-compose build
   
    docker-compose up
   
This will build and start the application service, which reads the orders.csv file and performs the specified tasks.

## Running the tests

1. To run the tests using Docker Compose, execute the following command:

    docker-compose run test
   
<img width="1440" alt="Screenshot 2024-07-28 at 9 51 03 AM" src="https://github.com/user-attachments/assets/0df73084-3071-4980-9ade-889ea73eadda">

For a user-friendly approach from the above screenshot, we can also expect to see the result using the port visible in docker after running the application
this was created using Flask.

Incase the port is busy on a different machine and an error is presented the resut will still be displayed on the terminal screen of docker due to the use of logging statements.



<img width="1440" alt="Screenshot 2024-07-28 at 9 53 41 AM" src="https://github.com/user-attachments/assets/94a725b8-9574-4f9e-b1f1-fd369da993bc">



# Output Screenshot:




<img width="1440" alt="Screenshot 2024-07-28 at 11 06 22 AM" src="https://github.com/user-attachments/assets/79187e56-22bc-4e6d-b7ca-cb55b0da797f">



<img width="1440" alt="Screenshot 2024-07-28 at 11 06 37 AM" src="https://github.com/user-attachments/assets/5a23fbe7-840b-4ae6-a3f5-929abb92a4b0">


<img width="1378" alt="Screenshot 2024-07-28 at 11 07 16 AM" src="https://github.com/user-attachments/assets/4d2e46b6-7c5a-4102-9bd9-ee4494c10968">

