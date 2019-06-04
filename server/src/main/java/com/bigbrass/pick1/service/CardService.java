package com.bigbrass.pick1.service;

import com.bigbrass.pick1.model.Card;
import com.bigbrass.pick1.repository.CardRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import javax.transaction.Transactional;
import java.util.List;

@Service
public class CardService {

    @Autowired
    private CardRepository cardRepository;

    @Transactional
    public List<Card> getAll() {
        return cardRepository.findAll();
    }
}
