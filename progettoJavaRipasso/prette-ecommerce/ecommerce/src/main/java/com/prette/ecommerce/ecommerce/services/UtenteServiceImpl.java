package com.prette.ecommerce.ecommerce.services;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.prette.ecommerce.ecommerce.entities.Utente;
import com.prette.ecommerce.ecommerce.repo.UtenteRepo;

@Service
public class UtenteServiceImpl implements UtenteService {
    @Autowired
    UtenteRepo repo;

    @Override
    public Utente findUser(String username, String password) {
        return repo.findByUsernameAndPassword(username,password);
    }

}
