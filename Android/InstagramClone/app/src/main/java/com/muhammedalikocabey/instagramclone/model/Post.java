package com.muhammedalikocabey.instagramclone.model;



public class Post {

    private String email;
    private String downloadUrl;
    private String comment;


    public Post(String email, String downloadUrl, String comment) {
        this.email = email;
        this.comment = comment;
        this.downloadUrl = downloadUrl;
    }



    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


    public String getDownloadUrl() {
        return downloadUrl;
    }

    public void setDownloadUrl(String downloadUrl) {
        this.downloadUrl = downloadUrl;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
}
