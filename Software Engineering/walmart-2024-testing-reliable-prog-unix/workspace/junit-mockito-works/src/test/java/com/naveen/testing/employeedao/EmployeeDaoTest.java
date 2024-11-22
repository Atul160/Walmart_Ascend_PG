package com.naveen.testing.employeedao;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import com.naveen.contracts.IEmployeeDAO;
import com.naveen.dao.EmployeeDAOMySQL;

class EmployeeDaoTest {

	@Test
	void employeeInsertRecordText_pass() {
		IEmployeeDAO dao = new EmployeeDAOMySQL(); 
		
		boolean flag = dao.insertEmployee(101, "Harish Kumar");
		
		assertEquals(true, flag);
	}

	@Test
	void employeeInsertRecordText_fail_name() {
		EmployeeDAOMySQL dao = new EmployeeDAOMySQL(); 
		
		boolean actual = dao.insertEmployee(101, "hari");
		
		assertEquals(false, actual);
	}
	
	@Test
	void employeeInsertRecordText_fail_empId() {
		EmployeeDAOMySQL dao = new EmployeeDAOMySQL(); 
		
		boolean actual = dao.insertEmployee(3, "Harish Kumar");
		
		assertEquals(true, actual);
	}

}
