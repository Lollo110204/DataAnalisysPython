package com.prette.ecommerce.ecommerce.services;

import org.springframework.stereotype.Service;

import com.prette.ecommerce.ecommerce.entities.Utente;

@Service
public interface UtenteService {

    Utente findUser(String username,String password);
    Utente findUserName(String username);
    Utente addUser(Utente u);

    
}