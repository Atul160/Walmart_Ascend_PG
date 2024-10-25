package com.telecom.model;

public class Customer {
    // Private members of the Customer class
    private String customerID;   // Customer ID
    private String name;         // Customer name
    private String plan;         // Subscription plan
    private float balance;       // Account balance
    private String phoneNumber;  // Phone number
    private String email;        // Email address

    // Public parameterized constructor to initialize the Customer object
    public Customer(String customerID, String name, String plan, float balance, String phoneNumber, String email) {
        this.customerID = customerID;
        this.name = name;
        this.plan = plan;
        this.balance = balance;
        this.phoneNumber = phoneNumber;
        this.email = email;
    }

    // Getters for private members
    public String getCustomerID() {
        return customerID;
    }

    public String getName() {
        return name;
    }

    public String getPlan() {
        return plan;
    }

    public float getBalance() {
        return balance;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public String getEmail() {
        return email;
    }

    // Setters for private members (if needed)
    public void setCustomerID(String customerID) {
        this.customerID = customerID;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setPlan(String plan) {
        this.plan = plan;
    }

    public void setBalance(float balance) {
        this.balance = balance;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public void setEmail(String email) {
        this.email = email;
    }
}
