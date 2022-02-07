package com.muhammedalikocabey.try_livedata_kotlin

import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel

class MainViewModel : ViewModel() {

    private var count: Int = 0

    val countLiveData: MutableLiveData<Int> by lazy() {
        MutableLiveData<Int>()
    }

    fun getCount() {
        count++
        countLiveData.value = count
    }

}