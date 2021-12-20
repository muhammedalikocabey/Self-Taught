package com.muhammedalikocabey.java_deneme;

import java.io.Serializable;

public class Landmark implements Serializable {
    String name;
    String country;
    int image;

    public Landmark(String name, String country, int image) {
        this.name = name;
        this.country = country;
        this.image = image;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public int getImage() {
        return image;
    }

    public void setImage(int image) {
        this.image = image;
    }

}
