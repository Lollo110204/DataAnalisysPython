package com.prette.ecommerce.ecommerce.entities;

import java.sql.Date;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Getter;
import lombok.Setter;

@Entity
@Table(name = "utente")
public class Utente {

    @Id
    @Getter @Setter
    private int id ;

    @Getter @Setter
    private String nome;
    @Getter @Setter
    private String cognome;
    @Getter @Setter
    private String username;
    @Getter @Setter
    private String password;
    @Getter @Setter
    private String mail;
    @Getter @Setter
    @Column(name = "data_nascita")
    private Date dataNascita;



}
