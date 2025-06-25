package com.prette.ecommerce.ecommerce.repo;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.prette.ecommerce.ecommerce.entities.Prodotto;

@Repository
public interface ProdottoRepo extends JpaRepository<Prodotto,Integer> {

    List<Prodotto> findByCategoria(String categoria);

}
