package com.storehouse.inventory;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;

import java.util.Arrays;
import java.util.List;

class InventoryServiceTest {

    @Mock
    private ProductRepository productRepository;

    @InjectMocks
    private InventoryService inventoryService;

    private Product sampleProduct;

    @BeforeEach
    void init() {
        MockitoAnnotations.openMocks(this);
        sampleProduct = new Product(101, "Test Product", 25.0);
    }

    @Test
    void shouldSaveProductSuccessfully() {
        when(productRepository.save(sampleProduct)).thenReturn(sampleProduct);
        Product savedProduct = inventoryService.saveProduct(sampleProduct);
        assertNotNull(savedProduct);
        assertEquals("Test Product", savedProduct.getName());
        verify(productRepository, times(1)).save(sampleProduct);
    }

    @Test
    void shouldRetrieveProductById() {
        when(productRepository.findById(101)).thenReturn(sampleProduct);
        Product retrievedProduct = inventoryService.getProductById(101);
        assertNotNull(retrievedProduct);
        assertEquals(101, retrievedProduct.getId());
        verify(productRepository, times(1)).findById(101);
    }

    @Test
    void shouldDeleteProductById() {
        doNothing().when(productRepository).deleteById(101);
        inventoryService.deleteProductById(101);
        verify(productRepository, times(1)).deleteById(101);
    }

    @Test
    void shouldRetrieveAllProducts() {
        List<Product> allProducts = Arrays.asList(
                new Product(101, "Alpha Product", 20.0),
                new Product(102, "Beta Product", 30.0)
        );
        when(productRepository.findAll()).thenReturn(allProducts);

        List<Product> products = inventoryService.getAllProducts();
        assertEquals(2, products.size());
        verify(productRepository, times(1)).findAll();
    }
}
