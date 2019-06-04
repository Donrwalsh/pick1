package com.bigbrass.pick1.model;

import javax.persistence.*;

@Entity
@Table(name = "cards")
public class Card {

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getSet_code() {
        return set_code;
    }

    public void setSet_code(String set_code) {
        this.set_code = set_code;
    }

    public Long getPicks() {
        return picks;
    }

    public void setPicks(Long picks) {
        this.picks = picks;
    }

    public Long getAppearances() {
        return appearances;
    }

    public void setAppearances(Long appearances) {
        this.appearances = appearances;
    }

    public String getLayout() {
        return layout;
    }

    public void setLayout(String layout) {
        this.layout = layout;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getImage_uri() {
        return image_uri;
    }

    public void setImage_uri(String image_uri) {
        this.image_uri = image_uri;
    }

    @Id
    @GeneratedValue(strategy= GenerationType.AUTO)
    private Long id;
    private String name;
    private String image_uri;
    private String set_code;
    private Long picks;
    private Long appearances;
    private String layout;

    @Override
    public String toString() {
        return String.format("Card [id=%s, name=%s, image_uri=%s set_code=%s, picks=%s, appearance=%s, layout=%s]",
                id, name, image_uri, set_code, picks, appearances, layout);
    }
}
