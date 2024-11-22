package com.naveen.client;

import com.naveen.dao.EmployeeDAOMySQL;

public class App {
	public static void main(String[] args) {
		EmployeeDAOMySQL dao = new EmployeeDAOMySQL();

		if (dao.insertEmployee(200, "Naveen Kumar")) {
			System.out.println("success");
		} else {
			System.out.println("Failure");
		}

	}
}
