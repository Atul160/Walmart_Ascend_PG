package com.telecom.util;

import com.telecom.model.Customer;
import com.telecom.service.CustomerService;
import com.telecom.exception.InvalidCustomerException;

import java.util.Scanner;

public class CustomerUtil {
    
    // Method to validate the customer information
    public static void validateCustomer(String customerID, String plan, float balance, String phoneNumber) throws InvalidCustomerException {
        // Check if plan is valid
        if (!plan.equalsIgnoreCase("Prepaid") && !plan.equalsIgnoreCase("Postpaid") && !plan.equalsIgnoreCase("Family")) {
            throw new InvalidCustomerException("Invalid plan. Plan must be 'Prepaid', 'Postpaid', or 'Family'.");
        }

        // Check if balance is non-negative
        if (balance < 0) {
            throw new InvalidCustomerException("Invalid balance. Balance cannot be negative.");
        }

        // Check if customerID is valid (starts with 'C' and is 5 characters long)
        if (customerID.length() != 5 || !customerID.startsWith("C")) {
            throw new InvalidCustomerException("Invalid customerID. It must start with 'C' and be exactly 5 characters long.");
        }

        // Check if phoneNumber is valid (exactly 10 digits)
        if (phoneNumber.length() != 10 || !phoneNumber.matches("\\d+")) {
            throw new InvalidCustomerException("Invalid phone number. It must be a 10-digit number.");
        }
    }

    public static void main(String[] args) {
        // Create an instance of CustomerService
        CustomerService customerService = new CustomerService();

        // Scanner for reading user input
        Scanner scanner = new Scanner(System.in);

        // Read data for 3 Customer objects
        for (int i = 1; i <= 3; i++) {
            try {
                System.out.println("\nEnter details for Customer " + i + ":");

                // Read customer ID
                System.out.print("Customer ID: ");
                String customerID = scanner.nextLine();

                // Read name
                System.out.print("Name: ");
                String name = scanner.nextLine();

                // Read plan
                System.out.print("Plan (Prepaid/Postpaid/Family): ");
                String plan = scanner.nextLine();

                // Read balance
                System.out.print("Balance: ");
                float balance = scanner.nextFloat();
                scanner.nextLine();  // Consume the newline

                // Read phone number
                System.out.print("Phone Number: ");
                String phoneNumber = scanner.nextLine();

                // Read email
                System.out.print("Email: ");
                String email = scanner.nextLine();

                // Validate customer data
                validateCustomer(customerID, plan, balance, phoneNumber);

                // If validation passes, create and add customer to the collection
                Customer customer = new Customer(customerID, name, plan, balance, phoneNumber, email);
                customerService.addCustomer(customer);

            } catch (InvalidCustomerException e) {
                System.out.println("Error: " + e.getMessage());
            }
        }

        // After adding valid customers, perform operations

        // Search customers by plan
        System.out.print("\nEnter the plan to search customers: ");
        String searchPlan = scanner.nextLine();
        customerService.searchByPlan(searchPlan);

        // Display all customer details
        System.out.println("\nDisplaying all customer details:");
        customerService.displayAllCustomers();

        // Find and display the customer with the highest balance
        System.out.println("\nCustomer with the highest balance:");
        customerService.getCustomerWithHighestBalance();

        // Close the scanner
        scanner.close();
    }
}
