package com.muhammedalikocabey.try_mvmm_java.viewmodel;

import android.text.TextUtils;
import android.util.Patterns;

import androidx.databinding.BaseObservable;
import androidx.databinding.Bindable;

import com.muhammedalikocabey.try_mvmm_java.BR;
import com.muhammedalikocabey.try_mvmm_java.model.Model;

public class AppViewModel extends BaseObservable {

    // creating object of Model Class
    private Model model;

    // String variables for Toast Messages
    private String successMessage = "Login Successfull";
    private String errorMessage = "Email or Password is not valid";


    // String variable for Toast Message
    @Bindable
    private String toastMessage = null;


    // Getter and Setter methods for Toast Message
    public String getToastMessage() {
        return toastMessage;
    }

    private void setToastMessage(String toastMessage) {
        this.toastMessage = toastMessage;
        notifyPropertyChanged(BR.toastMessage);
    }

    // Getter and Setter methods for Email varible
    @Bindable
    public String getUserEmail() {
        return model.getEmail();
    }

    public void setUserEmail(String email) {
        model.setEmail(email);
        notifyPropertyChanged(BR.userEmail);
    }


    // Getter and Setter MEthods for Password Variable
    @Bindable
    public String getUserPassword() {
        return model.getPassword();
    }

    public void setUserPassword(String password) {
        model.setPassword(password);
        notifyPropertyChanged(BR.userPassword);
    }


    // Constructor of ViewModel Class
    public AppViewModel() {
        model = new Model("", "");
    }


    // Actions to be performed when User clicks the Login Button
    public void onButtonClicked() {
        if(isValid()) {
            setToastMessage(successMessage);
        } else {
            setToastMessage(errorMessage);
        }
    }


    // Method to kep a check that variable fields must not kept empty by user
    public boolean isValid() {
        return !TextUtils.isEmpty(getUserEmail()) && Patterns.EMAIL_ADDRESS.matcher(getUserEmail()).matches() && getUserPassword().length() > 5;
    }


}
