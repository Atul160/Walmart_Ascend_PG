package com.telecom.service;

import com.telecom.model.Customer;
import java.util.ArrayList;
import java.util.List;

public class CustomerService {
    // Collection to store Customer instances
    private List<Customer> customers;

    // Constructor to initialize the collection
    public CustomerService() {
        customers = new ArrayList<>();
    }

    // 1. addCustomer(Customer c): To add a new Customer object into the collection
    public void addCustomer(Customer c) {
        customers.add(c);
        System.out.println("Customer added successfully: " + c.getName());
    }

    // 2. searchByPlan(String plan): Search customers based on their plan and display the details
    public void searchByPlan(String plan) {
        boolean found = false;
        for (Customer c : customers) {
            if (c.getPlan().equalsIgnoreCase(plan)) {
                System.out.println("Customer found: ");
                displayCustomerDetails(c);
                found = true;
            }
        }
        if (!found) {
            System.out.println("No customers found with plan: " + plan);
        }
    }

    // 3. displayAllCustomers(): Print the details of all the customers
    public void displayAllCustomers() {
        if (customers.isEmpty()) {
            System.out.println("No customers to display.");
            return;
        }

        for (Customer c : customers) {
            displayCustomerDetails(c);
        }
    }

    // 4. getCustomerWithHighestBalance(): Find and display the customer with the highest balance
    public void getCustomerWithHighestBalance() {
        if (customers.isEmpty()) {
            System.out.println("No customers available.");
            return;
        }

        Customer highestBalanceCustomer = customers.get(0);
        for (Customer c : customers) {
            if (c.getBalance() > highestBalanceCustomer.getBalance()) {
                highestBalanceCustomer = c;
            }
        }

        // System.out.println("Customer with the highest balance:");
        displayCustomerDetails(highestBalanceCustomer);
    }

    // Helper method to display customer details
    private void displayCustomerDetails(Customer c) {
        System.out.println("Customer ID: " + c.getCustomerID());
        System.out.println("Name: " + c.getName());
        System.out.println("Plan: " + c.getPlan());
        System.out.println("Balance: $" + c.getBalance());
        System.out.println("Phone Number: " + c.getPhoneNumber());
        System.out.println("Email: " + c.getEmail());
        System.out.println();
    }
}
