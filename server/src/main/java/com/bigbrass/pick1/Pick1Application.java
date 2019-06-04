package com.bigbrass.pick1;

import com.bigbrass.pick1.service.CardService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Pick1Application implements CommandLineRunner {

	@Autowired
	CardService cardService;

	public static void main(String[] args) {
		SpringApplication.run(Pick1Application.class, args);
	}

	@Override
	public void run(String... args) throws Exception {
		System.out.println(cardService.getAll());
	}
}
