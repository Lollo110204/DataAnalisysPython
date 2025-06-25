package com.prette.ecommerce.ecommerce.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;

import org.springframework.web.bind.annotation.PostMapping;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.prette.ecommerce.ecommerce.dto.UtentiDTO;
import com.prette.ecommerce.ecommerce.entities.Utente;
import com.prette.ecommerce.ecommerce.services.UtenteService;

import jakarta.servlet.http.HttpSession;


@RestController
@RequestMapping("/utente")
public class UtenteController {

    @Autowired
    UtenteService service;

    @PostMapping("/login")
    public ResponseEntity<?> login(@RequestParam String username, @RequestParam String password, HttpSession session) {
        Utente u = service.findUser(username, password);
        if (u != null) {
            UtentiDTO dto = new UtentiDTO();
            dto.setNome(u.getNome());
            dto.setCognome(u.getCognome());
            dto.setUsername(u.getUsername());
            dto.setMail(u.getMail());
            dto.setDataNascita(u.getDataNascita());

            session.setAttribute("utente", dto);
            return ResponseEntity.ok(dto);
        } else {
            return ResponseEntity.status(401).build();
        }
    }
}
