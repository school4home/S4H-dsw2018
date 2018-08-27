package com.school4home;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

//Significa que é uma controller REST
@RestController

//Mapeia a rota base pra chamar os endpoints
@RequestMapping("/teste")

//Significa quais origens podem acessar o endpoint, no caso está definido como todas.
@CrossOrigin("*")
public class EndPointTestController {

    //Caso não mapeie a rota, ele vai acessar pela url padrão da controller e o tipo da requisição. Neste caso, get.
    @GetMapping
    public String returnSucessOrFail(){
        return "Sucesso";
    }

    @GetMapping(value = "/mapeada")
    public String returnSucessOrFailMappedRoute(){
        return "Sucesso";
    }
}
