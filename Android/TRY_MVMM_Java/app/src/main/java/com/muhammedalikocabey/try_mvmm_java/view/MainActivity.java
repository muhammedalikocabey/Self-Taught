package com.muhammedalikocabey.try_mvmm_java.view;

import androidx.appcompat.app.AppCompatActivity;
import androidx.databinding.BindingAdapter;
import androidx.databinding.DataBindingUtil;

import android.os.Bundle;
import android.view.View;
import android.widget.Toast;

import com.muhammedalikocabey.try_mvmm_java.R;
import com.muhammedalikocabey.try_mvmm_java.databinding.ActivityMainBinding;
import com.muhammedalikocabey.try_mvmm_java.viewmodel.AppViewModel;

public class MainActivity extends AppCompatActivity {

    private ActivityMainBinding binding;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // ViewModel updates the Model after observing changes in the View

        // Model will also Update the View via the ViewModel

        binding = DataBindingUtil.setContentView(this, R.layout.activity_main);
        binding.setViewModel(new AppViewModel());
        binding.executePendingBindings();
    }

    // Any change in toastMessage attribute defined on the Button with bind prefix invokes this method
    @BindingAdapter({"toastMessage"})
    public static void runMe(View view, String message) {
        if(message != null) {
            Toast.makeText(view.getContext(), message, Toast.LENGTH_SHORT).show();
        }
    }
}