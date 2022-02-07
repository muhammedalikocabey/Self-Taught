package com.muhammedalikocabey.try_livedata_kotlin

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import com.muhammedalikocabey.try_livedata_kotlin.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    private lateinit var mainViewModel: MainViewModel
    private lateinit var binding: ActivityMainBinding


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        mainViewModel = ViewModelProvider(this@MainActivity).get(MainViewModel::class.java)

        mainViewModel.countLiveData.observe(this, Observer{
            binding.textView.text = "$it"
        })

        binding.button.setOnClickListener {
            mainViewModel.getCount()
        }

    }
}