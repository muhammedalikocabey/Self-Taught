package com.muhammedalikocabey.try_mvmm_kotlin.data

class FakeDatabase private constructor(){

    var quoteDao = FakeQuoteDao()
        private set

    companion object {
        @Volatile private var instance: FakeDatabase? = null

        fun getInstance() =
            instance ?: synchronized(lock = this) {
                instance ?: FakeDatabase().also { instance = it }
            }
    }

}