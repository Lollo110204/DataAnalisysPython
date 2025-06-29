package com.prette.ecommerce.ecommerce.services;


import org.mindrot.jbcrypt.BCrypt;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.prette.ecommerce.ecommerce.entities.Utente;
import com.prette.ecommerce.ecommerce.repo.UtenteRepo;

@Service
public class UtenteServiceImpl implements UtenteService {
    @Autowired
    UtenteRepo repo;
    // Aggiorna il metodo findUser per confrontare la password criptata
    @Override
    public Utente findUser(String username, String password) {
        Utente utente = repo.findByUsername(username);
        if (utente != null && BCrypt.checkpw(password, utente.getPassword())) {
            return utente;
        }
        return null;
    }

    @Override
    public Utente addUser(Utente u) {
       if (repo.findByUsername(u.getUsername())!=null){
        return null;
       }else{
        String passwordChiara = u.getPassword();
        String passwordHashata = BCrypt.hashpw(passwordChiara, BCrypt.gensalt());
        u.setPassword(passwordHashata);
        return repo.save(u);
       }
    }

    @Override
    public Utente findUserName(String username) {
       return repo.findByUsername(username);
    }

}
