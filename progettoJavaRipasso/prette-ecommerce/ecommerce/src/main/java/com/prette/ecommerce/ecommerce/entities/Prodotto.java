package com.prette.ecommerce.ecommerce.entities;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Getter;
import lombok.Setter;

@Entity
@Table(name = "prodotti")
public class Prodotto {

    @Id
    @Getter @Setter
    private int id;

    @Getter @Setter
    private String nome;
    @Getter @Setter
    private String categoria;

    @Getter @Setter
    private double prezzo;
    @Getter @Setter
    private String giacenza;

}
