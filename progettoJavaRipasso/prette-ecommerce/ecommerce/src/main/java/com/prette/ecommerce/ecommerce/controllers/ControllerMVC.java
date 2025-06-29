package com.prette.ecommerce.ecommerce.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

import jakarta.servlet.http.HttpSession;



@Controller
public class ControllerMVC {

    
    @GetMapping("/")
    public String home(HttpSession session) {
        if(session.getAttribute("utente") == null){
            return "redirect:/login";
        }
 
        return "home";
    }

    @GetMapping("/prodotti")
    public String getProdotti(HttpSession session) {
        if(session.getAttribute("utente") == null){
            return "redirect:/login";
        }
        return "prodotti";
    }

    @GetMapping("/login")
    public String login() {

    
        return "login";
    }

    @GetMapping("/singUp")
    public String singUp() {

    
        return "singUp";
    }


    


}
