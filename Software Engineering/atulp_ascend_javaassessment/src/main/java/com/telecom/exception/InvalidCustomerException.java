package com.telecom.exception;

public class InvalidCustomerException extends Exception {
    // Constructor that accepts a message
    public InvalidCustomerException(String message) {
        super(message);
    }
}