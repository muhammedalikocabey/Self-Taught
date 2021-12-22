package com.muhammedalikocabey.java_deneme;

public class Singleton {

    Landmark sentLandmark;

    private static Singleton singleton;

    private Singleton() {}

    public Landmark getSentLandmark() {
        return sentLandmark;
    }

    public void setSentLandmark(Landmark sentLandmark) {
        this.sentLandmark = sentLandmark;
    }

    public static Singleton getInstance() {
        if(singleton == null) {
            singleton = new Singleton();
        }
        return singleton;
    }


}
