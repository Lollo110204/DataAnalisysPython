package com.prette.ecommerce.ecommerce.dto;

import java.sql.Date;

import jakarta.persistence.Column;
import lombok.Getter;
import lombok.Setter;

public class UtentiDTO {

    @Getter @Setter
    private String nome;
    @Getter @Setter
    private String cognome;
    @Getter @Setter
    private String username;
    @Getter @Setter
    private String mail;
    @Getter @Setter
    @Column(name = "data_nascita")
    private Date dataNascita;


}
