package com.prette.ecommerce.ecommerce.repo;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.prette.ecommerce.ecommerce.entities.Utente;
@Repository
public interface UtenteRepo extends JpaRepository<Utente,Integer> {
  
    Utente findByUsernameAndPassword(String username, String password);
}
