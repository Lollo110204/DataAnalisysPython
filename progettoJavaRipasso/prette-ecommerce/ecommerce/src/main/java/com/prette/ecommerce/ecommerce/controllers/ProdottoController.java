package com.prette.ecommerce.ecommerce.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.prette.ecommerce.ecommerce.entities.Prodotto;
import com.prette.ecommerce.ecommerce.services.ProdottoService;

@RestController
@RequestMapping("/prodotti")
public class ProdottoController {
    @Autowired
    private ProdottoService service;

    @GetMapping("/")
    public ResponseEntity<List<Prodotto>> getAllProdotti(){
        return new ResponseEntity<>(service.getAllProdotti(), HttpStatus.OK);
    }

    @GetMapping("/{id}")
    public ResponseEntity<Prodotto> getProdotto(@PathVariable int id){
        return new ResponseEntity<>(service.getProdottoById(id), HttpStatus.OK);
    }


}
