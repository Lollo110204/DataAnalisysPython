package com.prette.ecommerce.ecommerce.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.prette.ecommerce.ecommerce.entities.Prodotto;
import com.prette.ecommerce.ecommerce.repo.ProdottoRepo;

@Service
public class ProdottoServiceImpl implements ProdottoService {

    @Autowired
    private ProdottoRepo repo;


    @Override
    public List<Prodotto> getAllProdotti() {
      return repo.findAll();
    }

    @Override
    public Prodotto getProdottoById(int id) {
        return repo.findById(id).orElse(null);
    }

    @Override
    public Prodotto addProdotto(Prodotto prodotto) {
        return repo.save(prodotto);
    }

    @Override
    public Prodotto updateProdotto(int id, Prodotto prodotto) {
      return repo.save(prodotto);
    }

    @Override
    public void deleteProdotto(int id) {
      repo.deleteById(id);
    }

}
