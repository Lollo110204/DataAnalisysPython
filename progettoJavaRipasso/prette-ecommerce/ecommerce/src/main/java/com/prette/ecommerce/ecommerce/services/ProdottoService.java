package com.prette.ecommerce.ecommerce.services;

import java.util.List;

import org.springframework.stereotype.Service;

import com.prette.ecommerce.ecommerce.entities.Prodotto;

@Service
public interface ProdottoService {

    List<Prodotto> getAllProdotti();
    Prodotto getProdottoById(int id);

    Prodotto addProdotto(Prodotto prodotto);
    Prodotto updateProdotto(int id, Prodotto prodotto);
    void deleteProdotto(int id);

}
