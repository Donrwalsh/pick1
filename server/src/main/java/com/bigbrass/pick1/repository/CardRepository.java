package com.bigbrass.pick1.repository;

import com.bigbrass.pick1.model.Card;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CardRepository extends JpaRepository<Card, Long> {

}
