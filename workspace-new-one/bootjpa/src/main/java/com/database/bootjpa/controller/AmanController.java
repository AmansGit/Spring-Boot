package com.database.bootjpa.controller;
import com.database.bootjpa.dao.AmanRepo;
import com.database.bootjpa.model.AmanBrand;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class AmanController {
    @Autowired
    AmanRepo repo;

    @RequestMapping("/")
    public String home(){
        return "home.jsp";
    }

    @RequestMapping("/addAmanBrand")
    public String addAmanBrand(AmanBrand aman){
        repo.save(aman);
        return "home.jsp";
    }
}