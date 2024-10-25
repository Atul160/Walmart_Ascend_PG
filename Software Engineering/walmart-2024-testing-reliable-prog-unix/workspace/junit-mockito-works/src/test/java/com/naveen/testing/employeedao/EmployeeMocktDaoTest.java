package com.naveen.testing.employeedao;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import com.naveen.contracts.IEmployeeDAO;

// my comments in testing-code branch
class EmployeeMocktDaoTest {

	IEmployeeDAO dao = null;

	@BeforeEach
	public void setUp() {
		dao = mock(IEmployeeDAO.class);
		when(dao.insertEmployee(101, "Harish Kumar")).thenReturn(true);
	}

	@Test
	void employeeDaoMockTest_pass() {
		assertEquals(true, dao.insertEmployee(101, "Harish Kumar"));
	}

	@Test
	void employeeDaoMockTest_fail_case_employee_id() {
		assertEquals(false, dao.insertEmployee(201, "Harish Kumar"));
	}
	
	@Test
	void employeeDaoMockTest_fail_case_employee_naveen() {
		assertEquals(false, dao.insertEmployee(101, "Naveen Kumar"));
	}
}
