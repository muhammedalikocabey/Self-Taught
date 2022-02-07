package com.muhammedalikocabey.try_mvmm_kotlin.utilities

import com.muhammedalikocabey.try_mvmm_kotlin.data.FakeDatabase
import com.muhammedalikocabey.try_mvmm_kotlin.data.FakeQuoteDao
import com.muhammedalikocabey.try_mvmm_kotlin.data.QuoteRepository
import com.muhammedalikocabey.try_mvmm_kotlin.ui.quotes.QuotesViewModelFactory

object InjectorUtils {

    fun provideQuotesViewModelFactory(): QuotesViewModelFactory {
        val quoteRepository = QuoteRepository.getInstance(FakeDatabase.getInstance().quoteDao)
        return QuotesViewModelFactory(quoteRepository)
    }

}