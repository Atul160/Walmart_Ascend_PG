package com.naveen.testing.employeedao;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

import java.util.List;

import org.junit.jupiter.api.Test;
// this comment is for another testing branch..... 
class MockitWithList {

	@Test
	void test() {
		List<String> mockList = mock(List.class); 
		when(mockList.get(0)).thenReturn("Naveen");
		
		assertEquals("Naveen", mockList.get(0));
	}

}
